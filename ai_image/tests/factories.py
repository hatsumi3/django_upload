from typing import Any, Sequence

from factory import DjangoModelFactory, Faker
import factory

from ai_image.models import Document

class DocumentFactory(DjangoModelFactory):
    """Document factory

    Args:
        DjangoModelFactory ([type]): [description]
    """

    description = Faker('sentence',nb_words=10)
    photo = factory.django.ImageField(color='blue')
    # photo = Faker('file_path', category='image', depth=2)

    class Meta:
        model = Document
