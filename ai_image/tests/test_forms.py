from ai_image.models import Document
from io import StringIO
import os

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from ai_image.forms import DocumentForm
from .factories import DocumentFactory

pytestmark = pytest.mark.django_db


# filefields test
# https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield

class TestDocumentForm:

    def test_documentfrom_is_valid(self):

        proto_document = DocumentFactory.build()
        image = SimpleUploadedFile(name='test_image.png',
                                   content=open(os.path.join(os.path.dirname(__file__),'test_image.png'), 'rb').read(),
                                   content_type='image/png')

        request_post = {
            'description': proto_document.description,
        }

        request_files = {
            'photo': image,
        }

        form = DocumentForm(request_post, request_files)

        assert form.is_valid()
        form.save()

        assert Document.objects.all().count() == 1

    def test_documentfrom_is_not_valid(self):

        proto_document = DocumentFactory.build()

        form = DocumentForm({
            'description': proto_document.description,
            'photo': proto_document.photo,
        })

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert 'photo' in form.errors
