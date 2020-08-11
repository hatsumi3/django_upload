import pytest

from ai_image.models import Document
from .factories import DocumentFactory

pytestmark = pytest.mark.django_db

# @pytest.mark.django_db
def test_get_documents():
    documents = Document.objects.all()
    assert documents.count() == 0

def test_create_document():
    DocumentFactory()
    documents = Document.objects.all()
    assert documents.count() == 1

def test_create_documents():
    for _ in range(10):
        DocumentFactory()

    documents = Document.objects.all()

    assert documents.count() == 10

