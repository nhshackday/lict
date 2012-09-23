# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from conflict.models import Article

class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)


        file_list = args
        for filename in file_list:
            article_doc = pq(filename=filename)
            try:
                article_tag = article_doc('article')
                article_type = article_tag.attr('article-type')
                if article_type != DESIRED_ARTICLE_TYPE:
                    logging.debug("Skipping article of type %s" % article_type)
                    continue
                (pmid, pmc) = pubmed_ids(article_doc)
                logging.info("Processing article %s / %s" % (pmc, pmid))
                # Which key? PMC

                (article,_) = Article.objects.get_or_create(pmid=pmid)
                article.pmc = pmc
                article.pmid = pmid
                article.title = article_doc('article-title').text()[:200]
                article.save()

                if False:
                    conflict_raw = extract_ci.ci_info_list(article_doc)
                    if conflict_raw:
                        logging.debug("Found conflict text for %d" % pmc)
                        node['conflict_raw'] = ' '.join(conflict_raw)
                        handle_conflicts(node)

                    article_index.add('pmc', pmc_str, node)
                    article_index.add('pmid', pmid_str, node)
            except AssertionError as e:
                # When in doubt, wrap it all in a massive try/except for bonus insanity!
                logging.error(e)



####


from pyquery import PyQuery as pq
from lict.lib.lict_common import pubmed_ids
import logging
import lict.lib.extract_ci
import lict.lib.nltk_hackery

DESIRED_ARTICLE_TYPE="research-article"

def import_stuff(file_list):
    for filename in file_list:
        article_doc = pq(filename=filename)
        try:
            article_tag = article_doc('article')
            article_type = article_tag.attr('article-type')
            if article_type != DESIRED_ARTICLE_TYPE:
                logging.debug("Skipping article of type %s" % article_type)
                continue
            (pmid, pmc) = pubmed_ids(article_doc)
            logging.info("Processing article %s / %s" % (pmc, pmid))
            save_article_to_neo4j(article_doc)
        except AssertionError as e:
            # When in doubt, wrap it all in a massive try/except for bonus insanity!
            logging.error(e)

def save_article_to_neo4j(article_doc):
    # Which key? PMC
    (pmid, pmc) = pubmed_ids(article_doc)
    pmc_str = str(pmc)
    pmid_str = str(pmid)
    try:
        node = article_index.get('pmc', pmc_str)[0]
    except IndexError:
        node = gdb.node()

    node['type'] = 'article'
    node['pmc'] = pmc
    node['pmid'] = pmid
    node['title'] = article_doc('article-title').text()
    conflict_raw = extract_ci.ci_info_list(article_doc)
    if conflict_raw:
        logging.debug("Found conflict text for %d" % pmc)
        node['conflict_raw'] = ' '.join(conflict_raw)
        handle_conflicts(node)

    article_index.add('pmc', pmc_str, node)
    article_index.add('pmid', pmid_str, node)

def handle_conflicts(node):
    conflict_raw = node['conflict_raw']
    organisations = nltk_hackery.extract_orgs(conflict_raw)

    for organisation in organisations:
        org_node = organisation_index.get('name', organisation)[0]
        org_node['type'] = 'organisation'
        org_node['name'] = organisations
        organisation_index.add('name', organisation, org_node)

        # Relation-up
        rel = node.relationships.create('conflicts', org_node)
        rel['source'] = conflict_raw

