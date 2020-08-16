import pytest
from django.core.exceptions import ValidationError

from ai_image.models import Document
from .factories import DocumentFactory

# 全体のDB設計
pytestmark = pytest.mark.django_db

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


# @pytest.mark.django_db
def test_get_documents():
    documents = Document.objects.all()
    assert documents.count() == 0

def test_create_documents():
    for _ in range(10):
        DocumentFactory()

    documents = Document.objects.all()

    assert documents.count() == 10

@pytest.mark.parametrize('length',[0,256])
def test_description_fields(length):
    
    with pytest.raises(ValidationError) as excinfo:
        item = DocumentFactory()
        item.description = 'a' * length
        item.full_clean()
    # print(excinfo.value.messages)
    # assert 'message' in excinfo.value.messages