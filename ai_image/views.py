import time

from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import Document


def index(request):
    obj = None
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ai_image:post')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
    
    time.sleep(3)

    return render(request, 'ai_image/model_form_upload.html', {
        'form': form,
        'items': obj,
    })