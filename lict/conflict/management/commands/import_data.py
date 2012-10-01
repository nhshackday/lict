# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from conflict.jobs.article import import_article
import logging

class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)


        file_list = args
        for filename in file_list:
            try:
                import_article(filename=filename)
            except UnicodeEncodeError as e:
                # When in doubt, wrap it all in a massive try/except for bonus insanity!
                logging.error(e)
