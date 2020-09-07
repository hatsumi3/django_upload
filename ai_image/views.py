import time
import logging

from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import Document

logger = logging.getLogger(__name__)

def index(request):
    """Documentの一覧画面の表示を行う。
    post時には新規データの登録を行い、この画面にリダイレクトする。

    Args:
        request (request): request

    Returns:
        render(render):
            form: 入力にミスがあった場合は入力前の情報を、ミスがない場合は空のインスタンスを渡す。
            items: Documentデータ全件
    """
    obj = Document.objects.all()
    if request.method == 'POST':
        logger.info('POST process start')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.make_bw_image()
            item.save()
            time.sleep(2)
            logger.info('POST process end')
            return redirect('ai_image:post')
        for key, value in form.errors.as_data().items():
            for item in value:
                logger.warn(f'{key}:{item}')
        for error in form.non_field_errors():
            logger.warn(error)
    else:
        form = DocumentForm()
    
    return render(request, 'ai_image/model_form_upload.html', {
        'form': form,
        'items': obj,
    })