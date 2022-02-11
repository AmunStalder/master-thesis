import matplotlib.pyplot as plt
import base64
from io import BytesIO

class UniformityCalculator:
    CAPS_THRESHOLD_UNIFORMITY   = 0.3
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
        self.diff_x2                = 2 * self.diff
        self.mean                   = round(self.get_diff()[0], 4)
        self.plus_1_diff            = round(self.mean * (100+self.diff)/100,4)
        self.plus_2_diff            = round(self.mean * (100+2*self.diff)/100,4)
        self.minus_1_diff           = round(self.mean * (100-self.diff)/100,4)
        self.minus_2_diff           = round(self.mean * (100-2*self.diff)/100,4)
        self.counter_above_1_diff   = 0
        self.counter_above_2_diff   = 0
        self.release_note           = ""
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
            self.release_note = "Uniformity of mass passed"
        else:
            self.release_note = "Uniformity of mass not passed"
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
        plt.xlabel('weight [g]')
        plt.xlim([self.mean * (1-4*self.diff/100), self.mean * (1+4*self.diff/100)])
        plt.yticks([])
        # for i, label in enumerate(annotations):
        #     plt.annotate(label, (X[i], Y[i]))
        plt.tight_layout()
        graph = self.get_graph()
        return graph
