from neo4jrestclient.client import GraphDatabase
from pyquery import PyQuery as pq
from lict_common import pubmed_ids
import logging

NEO4J_URL="http://localhost:7474/db/data/"
DESIRED_ARTICLE_TYPE="research-article"

gdb = GraphDatabase(NEO4J_URL)
one_index_to_rule_them_all = gdb.nodes.indexes.create("one_index_to_rule_them_all")


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
            logging.info("Processing article %d / %d" % (pmc, pmid))
            save_article_to_neo4j(article_doc)
        except Exception as e:
            # When in doubt, wrap it all in a massive try/except for bonus insanity!
            logging.error(e)
        

def save_article_to_neo4j(article_doc):
    # Which key? PMC
    (pmid, pmc) = pubmed_ids(article_doc)
    pmc_str = str(pmc)
    pmid_str = str(pmid)
    try:
        node = one_index_to_rule_them_all.get('pmc', pmc_str)[0]
    except IndexError:
        node = gdb.node()

    node['pmc'] = pmc
    node['pmid'] = pmid
    node['title'] = article_doc('article-title').text()

    one_index_to_rule_them_all.add('pmc', pmc_str, node)
    one_index_to_rule_them_all.add('pmid', pmid_str, node)

if __name__ == "__main__":
    import sys
    import glob

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    file_list = sys.argv[1:]
    import_stuff(file_list)
