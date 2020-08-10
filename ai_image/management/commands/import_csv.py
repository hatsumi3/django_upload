import csv
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from ai_image.models import Document

class Command(BaseCommand):
    # help message
    help = 'import csv file and create records.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv', nargs='+', type=str)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        with open(options['csv'][0]) as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                document = Document.objects.create(
                    description=row['description'],
                    photo=row['photo']
                )
                print(i, document)
            print('completed!')