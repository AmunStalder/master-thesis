from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import matplotlib.pyplot as plt
import base64
import numpy as np
np.set_printoptions(suppress=True)
from io import BytesIO

class UniformityCalculator:
    CAPS_THRESHOLD_UNIFORMITY   = 300
    CAPS_DIFF_BELOW_THRESHOLD   = 10
    CAPS_DIFF_ABOVE_THRESHOLD   = 7.5
    CAPS_THRESHOLD_BALANCE      = 10
    CAPS_AMOUNT_WEIGHED         = 20
    SUPPOS_AMOUNT_WEIGHED       = 10
    SUPPOS_DIFF                 = 5

    def __init__(self, gal_form, total_mass, mass_max1, mass_max2, mass_max3, mass_min1, mass_min2, mass_min3,
    mass_1_caps_empty=0):
        self.gal_form               = gal_form
        self.total_mass             = total_mass
        self.mass_1_caps_empty      = mass_1_caps_empty
        self.masses                 = [mass_max1-self.mass_1_caps_empty, mass_max2-self.mass_1_caps_empty, mass_max3-self.mass_1_caps_empty, mass_min1-self.mass_1_caps_empty, mass_min2-self.mass_1_caps_empty, mass_min3-self.mass_1_caps_empty]
        self.diff                   = self.get_diff()[1]
        self.diff_x2                = 2 * self.get_diff()[1]
        self.mean                   = self.get_diff()[0]
        self.plus_1_diff            = self.mean * (100+self.diff)/100
        self.plus_2_diff            = self.mean * (100+2*self.diff)/100
        self.minus_1_diff           = self.mean * (100-self.diff)/100
        self.minus_2_diff           = self.mean * (100-2*self.diff)/100
        self.counter_above_1_diff   = 0
        self.counter_above_2_diff   = 0
        self.release_note           = self.calculate()
        self.uniformity_plot        = self.get_plot()

    def get_diff(self):
        if self.gal_form == "caps":
            mean = self.total_mass/self.CAPS_AMOUNT_WEIGHED - self.mass_1_caps_empty
            if mean < self.CAPS_THRESHOLD_UNIFORMITY:
                diff = self.CAPS_DIFF_BELOW_THRESHOLD
            else:
                diff = self.CAPS_DIFF_ABOVE_THRESHOLD

        if self.gal_form  == "suppos":
            mean = self.total_mass/self.SUPPOS_AMOUNT_WEIGHED
            diff = self.SUPPOS_DIFF
        return [mean, diff]

    def calculate(self):
        for mass in self.masses:
            if mass < self.minus_2_diff or mass > self.plus_2_diff:
                self.counter_above_2_diff += 1
            elif (mass > self.plus_1_diff and mass <= self.plus_2_diff) or (mass < self.minus_1_diff and mass >= self.minus_2_diff):
                self.counter_above_1_diff += 1
        if self.counter_above_2_diff == 0 and self.counter_above_1_diff <= 2:
            self.result = True
        else:
            self.result = False
        return self.result
        # return self

    def get_graph(self):
        #create bytes buffer for image to be saved
        buffer = BytesIO()
        #create figure with BytesIO object as file
        plt.savefig(buffer, format='png')
        #set cursor to the beginning of the stream
        buffer.seek(0)
        #retrieve the entire content of the file
        image_png = buffer.getvalue()
        #use encoder that takes in a bytes-like object
        graph = base64.b64encode(image_png)
        #convert base64 to utf-8
        graph = graph.decode('utf-8')
        #free memory of buffer
        buffer.close()
        return graph

    def get_plot(self):
        # annotations=["-{}%".format(100*self.diff_x2), "-{}%".format(100*self.diff), "+{}%".format(self.mean),"+{}%".format(100*self.diff),"+{}%".format(100*self.diff_x2)]
        plt.switch_backend('AGG')
        plt.figure(figsize = (10,2))
        plt.title('Distribution of weights')
        X = self.masses
        Y = [0,0,0,0,0,0]
        plt.vlines(self.minus_2_diff, -0.5, 0.5, linestyles ="solid", colors ="red")
        plt.vlines(self.minus_1_diff, -0.5, 0.5, linestyles ="dotted", colors ="orange")
        plt.vlines(self.mean, -0.5, 0.5, linestyles="solid", colors = "green")
        plt.vlines(self.plus_1_diff, -0.5, 0.5, linestyles ="dotted", colors ="orange")
        plt.vlines(self.plus_2_diff, -0.5, 0.5, linestyles ="solid", colors ="red")
        plt.fill_between([self.mean * (1-4*self.diff/100), self.minus_2_diff] , -0.5, 0.5, color = "#ffe8e8")
        plt.fill_between([self.minus_2_diff, self.minus_1_diff] , -0.5, 0.5, color = "#ffdabf")
        plt.fill_between([self.minus_1_diff, self.plus_1_diff] , -0.5, 0.5, color = "#e7fae6")
        plt.fill_between([self.plus_1_diff, self.plus_2_diff] , -0.5, 0.5, color = "#ffdabf")
        plt.fill_between([self.plus_2_diff, self.mean * (1+4*self.diff/100)] , -0.5, 0.5, color = "#ffe8e8")
        plt.scatter(X,Y, marker='.')
        if self.gal_form == 'caps':
            x_label = 'Mean content [mg]'
        else:
            x_label = 'Weight [g]'
        plt.xlabel(x_label)
        plt.xlim([self.mean * (1-4*self.diff/100), self.mean * (1+4*self.diff/100)])
        plt.yticks([])
        # for i, label in enumerate(annotations):
        #     plt.annotate(label, (X[i], Y[i]))
        plt.tight_layout()
        graph = self.get_graph()
        return graph

def myround(x, base=0.05):
    return base * round(x/base)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def firstNonNan(listfloats):
    counter = 0
    for item in listfloats:
        if np.isnan(item) == False:
            return [item, counter]
        counter = counter + 1

def calculate_price_per_ingredient(weight, substance_price):
    amounts = np.array([0.0001,0.001, 0.01, 0.1, 1, 10, 100, 500, 1000, 10000])
    division = []
    price_combo = []
    price = 0
    for amount in amounts:
        division.append(weight / amount)

    #if below 1 mg, take first non Nan
    if division[1] < 1:
        price_combo = firstNonNan(substance_price)
        price = price_combo[0]
        return price
    #if above or equal to 1000g:
    elif division[8] >= 1:
        substance_price = substance_price[::-1]
        price_combo = firstNonNan(substance_price)
        substance_price[::-1]
        price = price_combo[0]*division[9-price_combo[1]]
        return price
    #if between 1 and 1000 (excl. 1000):
    else:
        index = 0
        for div in division:
            if 1 <= div < 10:
                index = division.index(div)
        #two possibilities: is NaN or is not NaN
        #if NaN
        if np.isnan(substance_price[index]):
            #if NaN: price can be on the right...
            try:
                price_combo = firstNonNan(substance_price[index:])
                price = price_combo[0]
                return myround(price)
            # or on the left
            except:
                substance_price = substance_price[::-1]
                price_combo = firstNonNan(substance_price)
                substance_price[::-1]
                price = price_combo[0]*division[9-price_combo[1]]
                return myround(price)
        #if not NaN:
        else:
            if division[index]*substance_price[index] < substance_price[index+1] and not np.isnan(substance_price[index+1]):
                price = division[index]*substance_price[index]
                return myround(price)
            elif division[index]*substance_price[index] > substance_price[index+1] and not np.isnan(substance_price[index+1]):
                price = substance_price[index+1]
                return myround(price)
            else:
                price = division[index]*substance_price[index]
                return myround(price)

def price_per_ingredient(weight, substance):
    substance_price = [
        #For calculation purposes we add two None's in the beginning and the end
        None,
        substance.price_0_001_g_ml,
        substance.price_0_01_g_ml,
        substance.price_0_1_g_ml,
        substance.price_1_g_ml,
        substance.price_10_g_ml,
        substance.price_100_g_ml,
        substance.price_500_g_ml,
        substance.price_1000_g_ml,
        None,
        ]
    for i in range(0,len(substance_price)):
        if substance_price[i] == None:
            substance_price[i] = np.NaN
        else:
            pass
    return calculate_price_per_ingredient(weight, substance_price)
