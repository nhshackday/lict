# -*- coding: UTF-8 -*-
import logging
from django.core.management.base import BaseCommand
from conflict.models import Article, Organisation, Conflict, Drug

class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        filename = args[0]
        with open(filename) as drugfile:
            Drug.objects.all().delete()
            while True:
                line = drugfile.readline()
                stuff = line.split(',')
                jeff_id = int(stuff[0])
                name = ', '.join(stuff[1:])
                logging.info("Creating %s" % name)
                Drug.objects.create(jeff_id=jeff_id, name=name)
