# vim: set sw=4 sts=4 ts=4 et:
from lxml import etree
from pyquery import PyQuery as pq
import urllib
import subprocess
import os

def xmldocs_in_dir(d):
    for dirname, dirnames, filenames in os.walk(d):
        for fn in map(lambda x: os.path.join(dirname, x), filter(lambda f:f.endswith(".nxml"), filenames)):
            try:
                yield fn, pq(filename=fn)
            except Exception, e:
                pass

def filter_by_article_type(atype, docs):
    for filename, doc in docs:
        article_tag = doc('article')
        article_type = article_tag.attr('article-type')
        if article_type == atype:
            yield filename, doc

def pubmed_ids(doc):
    pmc = None
    pmid = None

    try:
        pmc = int(doc('article-id[pub-id-type="pmc"]').text())
    except:
        pass
    try:
        pmid = int(doc('article-id[pub-id-type="pmid"]').text())
    except:
        pass
    return pmid,pmc

