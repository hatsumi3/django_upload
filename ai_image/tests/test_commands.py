from ai_image import models
import pytest

from config.local_settings import BASE_DIR
from io import StringIO
from django.core.management import call_command

from config import settings
from ai_image.models import Document

pytestmark = pytest.mark.django_db

def test_import_csv():
    out = StringIO()
    call_command('import_csv', f'{BASE_DIR}\\ai_image\\management\\commands\\sample_data.csv' ,stdout=out)

    # print(out.getvalue())
    # assert 'completed!' == out.getvalue()

    documents = Document.objects.all()
    assert documents.count() == 1

