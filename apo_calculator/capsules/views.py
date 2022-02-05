from django.views.generic import TemplateView
from .forms import UniformityForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, FileResponse
from . import models
from django.urls import reverse_lazy
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

#View for Capsules
class CapsFuncView(TemplateView):
    template_name = 'capsules/functions.html'
# Create your views here.

class CapsUnifListView(ListView):
    context_object_name = 'caps_list'
    model = models.Uniformity
    template_name = 'capsules/list.html'

class CapsUnifDetailView(DetailView):
    context_object_name = 'caps_detail'
    model = models.Uniformity
    template_name = 'capsules/detail.html'

def pdf_view(request, pk):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont('Helvetica', 14)
    prod = models.Uniformity.objects.get(id = pk)

    textobject.textLine(prod.caps_name)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    c.drawText(textobject)
    # Close the PDF object cleanly, and we're done.
    c.showPage()
    c.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class CapsUnifCreateView(CreateView):
    template_name = 'capsules/uniformity_form.html'
    model = models.Uniformity
    fields = (
        'caps_name',
        'mass_1_caps_empty',
        'mass_20_caps_full',
        'mass_max1',
        'mass_max2',
        'mass_max3',
        'mass_min1',
        'mass_min2',
        'mass_min3',
    )

class CapsUnifUpdateView(UpdateView):
    fields = (
        'caps_name',
        'mass_1_caps_empty',
        'mass_20_caps_full',
        'mass_max1',
        'mass_max2',
        'mass_max3',
        'mass_min1',
        'mass_min2',
        'mass_min3',
    )
    model = models.Uniformity

class CapsUnifDeleteView(DeleteView):
    context_object_name = 'uniformity'
    model = models.Uniformity
    success_url = reverse_lazy("capsules:list")
