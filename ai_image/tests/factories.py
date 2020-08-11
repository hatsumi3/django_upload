from typing import Any, Sequence

from factory import DjangoModelFactory, Faker
import factory

from ai_image.models import Document

class DocumentFactory(DjangoModelFactory):

    description = Faker('sentence',nb_words=10)
    photo = factory.django.ImageField(color='blue')
    # photo = Faker('file_path', category='image', depth=2)

    class Meta:
        model = Document
