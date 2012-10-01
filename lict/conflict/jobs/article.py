# -*- coding: UTF-8 -*-
import logging

from pyquery import PyQuery as pq
from lict.lib.lict_common import pubmed_ids
from conflict.models import Article, Organisation, Conflict
from lict.lib import extract_ci, nltk_hackery

DESIRED_ARTICLE_TYPE="research-article"

def import_article(filename=None):
    article_doc = pq(filename=filename)
    article_tag = article_doc('article')
    article_type = article_tag.attr('article-type')
    if article_type != DESIRED_ARTICLE_TYPE:
        logging.debug("Skipping article of type %s" % article_type)
        return
    (pmid, pmc) = pubmed_ids(article_doc)
    logging.info("Processing article with pmc %s / pmid %s" % (pmc, pmid))
    # Which key? PMC

    (article,_) = Article.objects.get_or_create(pmid=pmid)
    article.pmc = pmc
    article.pmid = pmid
    article.title = article_doc('article-meta article-title').text()[:200]
    article.save()

    conflict_raw = extract_ci.ci_info_list(article_doc)
    if conflict_raw:
        article.raw_conflict_text = ' '.join(conflict_raw)
        logging.info("Found conflict text for %d: %s" % (pmc, article.raw_conflict_text))
        organisation_names = nltk_hackery.extract_orgs(article.raw_conflict_text)
        logging.info("Extracted conflict organisations: %s" % str(organisation_names))

        for organisation_name in organisation_names:
            (organisation, organisation_created) = Organisation.objects.get_or_create(name=organisation_name)
            if organisation_created:
                logging.info("Created organisation %s" % organisation_name)
            (conflict, _) = Conflict.objects.get_or_create(article=article, organisation=organisation)
