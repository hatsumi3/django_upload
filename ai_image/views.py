import time
import logging

from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import Document

logger = logging.getLogger(__name__)

def index(request):
    obj = Document.objects.all()
    if request.method == 'POST':
        logger.info('POST process start')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            time.sleep(3)
            logger.info('POST process end')
            return redirect('ai_image:post')
    else:
        form = DocumentForm()
    
    # logger test
    logger.debug('GET')
    logger.info('GET')
    logger.warning('GET')
    logger.error('GET')
    return render(request, 'ai_image/model_form_upload.html', {
        'form': form,
        'items': obj,
    })