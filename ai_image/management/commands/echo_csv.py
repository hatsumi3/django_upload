import os
import csv
from distutils.dir_util import copy_tree
import logging
from tkinter import image_types
from typing import Any, Optional
from pathlib import Path

from django.core.management.base import BaseCommand, CommandParser
from django.conf import settings
from django.utils import timezone
from PIL import Image

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

        try:
            csv_data = self.read_csv(options['csv'][0])
            logger.info('read_csv completed.')
            self.add_calc_parameters(csv_data)
            logger.info('add_calc_parameters completed.')
            create_objects, update_objects = self.initialize_objects(csv_data)
            logger.info('initialize_objects completed.')

            print(create_objects)
            print(update_objects)
            Document.objects.bulk_create(create_objects)
            Document.objects.bulk_update(update_objects,fields=[
                                        'description',
                                        'photo',
                                        'bw_photo',
                                        'sample_number',
                                        'uploaded_at',
                                        ])
            logger.info('objects_create completed.')
            copy_tree(f"{settings.BASE_DIR}/docs2/org/",f'{settings.MEDIA_ROOT}/{Document.photo.field.upload_to}')
            copy_tree(f"{settings.BASE_DIR}/docs2/org_bw/",f'{settings.MEDIA_ROOT}/{Document.bw_photo.field.upload_to}')
            logger.info('copy images completed.')


        except Exception as e:
            logger.error(e)
            logger.info('error:end batch')
            return

        logger.info('success:end batch')


    def read_csv(self, filepath):
        """csvファイルを読み込み

        Args:
            filepath ([type]): [description]

        Raises:
            FileNotFoundError: [description]
            FileNotFoundError: [description]
            KeyError: [description]
            ValueError: [description]
            ValueError: [description]

        Returns:
            [type]: [description]
        """
        csv_data = []
        row_i = 0
        try:
            with open(filepath, encoding='UTF-8') as f:
                reader = csv.DictReader(f)
                for row_i, row in enumerate(reader,start=2):
                    document = dict(
                        description=row['description'],
                        # uploadフォルダprefixを付与
                        photo=f"{settings.BASE_DIR}/docs2/org/{row['photo']}",
                        sample_number= int(row['sample_number'])
                    )
                    self.confirm_dict(row_i, document)
                    csv_data.append(document)

        except FileNotFoundError as e:
            if row_i:
                raise FileNotFoundError(f'ファイル\"{e}\"は存在しません。')
            else:
                raise FileNotFoundError(f'ファイル\"{filepath}\"は存在しません。')
        except KeyError as e:
            raise KeyError(f'csv headerに{e}が含まれていません。')
        except ValueError as e:
            if row_i:
                raise ValueError(f'{row_i}行目の入力内容を確認ください。{e}')
            else:
                raise ValueError(f'csvファイル形式で読み込めません。{e}')
        return csv_data                

    def confirm_dict(self, row_i, document):
        self.confirm_str_field('description', document['description'], max_length=255)
        self.confirm_str_field('photo', document['photo'])
        self.confirm_int_field('sample_number', document['sample_number'])
        self.confirm_filepath(filename=document['photo'])

    def confirm_filepath(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)

    def confirm_str_field(self, key, value,max_length=100):
        if len(value) > max_length:
            raise ValueError(f'{key}の最大文字数は{max_length}です。')

    def confirm_int_field(self, key, value, min_value=0, max_value=100):
        try:
            int_value = int(value)
        except Exception:
            raise ValueError(f'{key}:{value}は正数を入力してください。。')

        if not min_value <= int_value <= max_value:
            raise ValueError(f'{key}:{value}は{min_value}-{max_value}の範囲で入力してください。。')

    def add_calc_parameters(self,csv_data):
        for item in csv_data:
            self.make_bw_image(item['photo'])            
            # ファイル有無を確認したので、ファイルパスのみ配信先に変更
            item['photo'] = f"{Document.photo.field.upload_to}{os.path.basename(item['photo'])}"


    def make_bw_image(self, filepath):
        img = Image.open(filepath)
        gray_img = img.convert('L')
        gray_img.save(f'{settings.BASE_DIR}/docs2/org_bw/{os.path.basename(img.filename)}')


    def initialize_objects(self, csv_data):
        create_objects = []
        update_objects =[]
        for item in csv_data:
            if Document.objects.filter(photo__contains=os.path.basename(item['photo'])).exists():
                document = Document.objects.get(photo__contains=os.path.basename(item['photo']))
                document.description = item['description']
                document.photo = item['photo']
                document.sample_number = item['sample_number']
                document.uploaded_at = timezone.now()
                document.bw_photo = f"{Document.bw_photo.field.upload_to}{os.path.basename(item['photo'])}"
                update_objects.append(document)
            else:
                document = Document(
                    description=item['description'],
                    photo=item['photo'],
                    sample_number=0,
                )
                document.bw_photo = f"{Document.bw_photo.field.upload_to}{os.path.basename(item['photo'])}"
                create_objects.append(document)

        return create_objects, update_objects
