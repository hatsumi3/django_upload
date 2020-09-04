import csv
import logging
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from ai_image.models import Document

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """ Read csv and import data to database.
        python manage.py import_csv [csv file path]
        csv header need to contain 'description' and 'photo' columns.
        description(str): description 
        photo(str): file path 
     Args:
        BaseCommand ([type]): BaseCommand
    """
    # help message
    help = 'import csv file and create records.'

    def add_arguments(self, parser: CommandParser):
        """ argumetn csv"""
        parser.add_argument('csv', nargs='+', type=str)

    def handle(self, *args: Any, **options: Any):
        """handle setting. 

        Returns:
            Optional[str]: handle setting
        """
        logger.info('start batch')

        with open(options['csv'][0]) as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                document = Document(
                    description=row['description'],
                    photo=row['photo']
                )
                logger.info(f'logging:{i}, {document.description}')
            logger.info('logging:completed')
