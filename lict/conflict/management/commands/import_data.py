# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from conflict.jobs.article import import_article
import logging
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--use-celery',
            action='store_true',
            dest='use_celery',
            default=False,
            help='Use Celery for article imports'
        ),
        make_option('--extract-conflict-data',
            action='store_true',
            dest='extract_conflict_data',
            default=False,
            help='Use NLTK to extract conflict of interest data'
        ),
    )

    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)


        file_list = args
        for filename in file_list:
            try:
                kwargs = {}
                kwargs['filename'] = filename
                kwargs['extract_conflict_data'] = options['extract_conflict_data']
                if options['use_celery']:
                    import_article.delay(**kwargs)
                else:
                    import_article(**kwargs)
            except UnicodeEncodeError as e:
                # When in doubt, wrap it all in a massive try/except for bonus insanity!
                logging.error(e)
