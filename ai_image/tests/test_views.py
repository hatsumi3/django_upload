import os
import pytest
from django.contrib.auth.models import AnonymousUser
from django.http.response import Http404
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile

from ai_image.forms import DocumentForm
from .factories import DocumentFactory
from ai_image import views


pytestmark = pytest.mark.django_db

def test_get_index():
    rf = RequestFactory()
    request = rf.get('ai_image:post')
    response = views.index(request)

    assert response.status_code == 200


def test_post_index():
    rf = RequestFactory()
    proto_document = DocumentFactory.build()
    image = SimpleUploadedFile(name='test_image.png',
                            content=open(os.path.join(os.path.dirname(__file__),'test_image.png'), 'rb').read(),
                            content_type='image/png')
    data = {
        'description': proto_document.description,
        'photo': image,
    }
    request = rf.post('ai_image:post', data)
    response = views.index(request)

    assert response.status_code == 302
