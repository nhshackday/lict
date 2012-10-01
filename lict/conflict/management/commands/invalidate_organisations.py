# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

import logging
from conflict.models import Organisation
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """Marks Organisations as invalid (e.g. where we've extracted "PhD" from the conflict of interest declaration)"""

    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        count_invalidated = 0
        for organisation_name in args:
            try:
                org = Organisation.objects.get(name=organisation_name)
            except Organisation.DoesNotExist:
                logging.warning('Could not find organisation with name "%s"' % organisation_name)
                continue

            if not org.is_a_real_organisation:
                logging.warning('Organisation "%s" has already been invalidated' % organisation_name)
                continue

            org.is_a_real_organisation = False
            org.save()
            logging.info('Marked "%s" as invalid' % organisation_name)
            count_invalidated += 1
        logging.info("Marked %d organisations as invalid" % count_invalidated)

