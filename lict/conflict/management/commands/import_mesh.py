# -*- coding: UTF-8 -*-
import logging
from django.core.management.base import BaseCommand
from conflict.models import Mesh

class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        filename = args[0]
        with open(filename) as meshfile:
            Mesh.objects.all().delete()
            while True:
                line = meshfile.readline()
                stuff = line.split(',')
                jeff_id = int(stuff[0])
                name = ', '.join(stuff[1:])
                logging.info("Creating %s" % name)
                Mesh.objects.create(jeff_id=jeff_id, name=name)
