from neo4jrestclient.client import GraphDatabase
from pyquery import PyQuery as pq
import logging

NEO4J_URL="http://localhost:7474/db/data/"
DESIRED_ARTICLE_TYPE="research-article"

gdb = GraphDatabase(NEO4J_URL)
one_index_to_rule_them_all = gdb.nodes.indexes.create("one_index_to_rule_them_all")


def import_stuff(file_list):
    for filename in file_list:
        doc = pq(filename=filename)
        try:
            article_tag = doc('article')
            article_type = article_tag.attr('article-type')
            if article_type != DESIRED_ARTICLE_TYPE:
                logging.debug("Skipping article of type %s" % article_type)
                continue
            pmc = int(doc('article-id[pub-id-type="pmc"]').text())
            pmid = int(doc('article-id[pub-id-type="pmid"]').text())
            logging.info("Processing article %d / %d" % (pmc, pmid))
            article = Article(pmc, pmid)
            article.from_pyquery_doc(doc)
            save_article_to_neo4j(article)
        except Exception as e:
            # When in doubt, wrap it all in a massive try/except for bonus insanity!
            print e
        

def save_article_to_neo4j(article):
    # Which key? PMC
    pmc_str = str(article.pmc)
    pmid_str = str(article.pmid)
    try:
        node = one_index_to_rule_them_all.get('pmc', pmc_str)[0]
    except IndexError:
        node = gdb.node()

    node['pmc'] = article.pmc
    node['pmid'] = article.pmid

    one_index_to_rule_them_all.add('pmc', pmc_str, node)
    one_index_to_rule_them_all.add('pmid', pmid_str, node)

class Article(object):
    def __init__(self, pmc, pmid):
        self.pmc = pmc
        self.pmid = pmid

    def from_pyquery_doc(self, doc):
        pass

if __name__ == "__main__":
    import sys
    import glob

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    file_list = sys.argv[1:]
    import_stuff(file_list)
