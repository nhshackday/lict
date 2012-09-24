# -*- coding: UTF-8 -*-

import logging
import tempfile
from django.core.management.base import BaseCommand
from urlparse import urljoin
import os
import requests

class Command(BaseCommand):
    help = """Downloads some sample data from http://pmc.jensenlab.org/. Pre-alpha with lots hard-coded, patches very welcomed."""

    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        BASE_URL = 'http://pmc.jensenlab.org/pmcid/'
        tmpdir = tempfile.mkdtemp('-conflict')

        # TODO Options...
        START_PMCID = 13900
        STOP_PMCID = 13924

        for pmcid in xrange(START_PMCID, STOP_PMCID):
            filename = '%d.nxml' % pmcid
            url = urljoin(BASE_URL, filename)
            r = requests.get(url)
            with open(os.path.join(tmpdir, filename), 'w') as f:
                f.write(r.text)
            logging.debug("Wrote %s" % filename)
        logging.info("Sample article data written to %s" % tmpdir)

