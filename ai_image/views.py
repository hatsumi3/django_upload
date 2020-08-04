from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import Document
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ai_image:post')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
    
    return render(request, 'ai_image/model_form_upload.html', {
        'form': form,
        'items': obj,
    })