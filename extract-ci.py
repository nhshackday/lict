#!/opt/nhshackday/wip/lict/bin/python
# vim: set sw=4 sts=4 ts=4 et:
from lict_common import *
import subprocess
import os
import pprint

NXMLDIR = "/opt/nhshackday/jeffram/nxml"
COMPETING_INTEREST_TITLES=["competing interests", "declaration of competing interests", "competing interest", "competing interests:", "competing interests."]

def ci_info_list(doc):
    ci_info = []
    ci_info += [pq(s)('p').text().encode('utf-8') for s in doc('sec') if pq(s)('title').text().encode('utf-8').strip().lower() in COMPETING_INTEREST_TITLES]
    ci_info += [' '.join(p.itertext()) for p in doc('p') if pq(p)('bold') and pq(p)('bold').text().encode('utf-8').strip().lower() in  COMPETING_INTEREST_TITLES]
    return ci_info

def competing_interest_declarations():
    for filename, doc in filter_by_article_type("research-article", xmldocs_in_dir(NXMLDIR)):
        try:
            pmid, pmc = pubmed_ids(doc)
            ci_info = ci_info_list(doc)
            if (len(ci_info) > 1):
                print "Warning: more than one ci_info for doc %s" % (str((pmid, pmc)))
            yield (pmid, pmc), ci_info

        except Exception, e:
            print "error with file %s: %s" % (filename, str(e))

if __name__ == "__main__":
    for ids, ci_info in competing_interest_declarations():
        print "%s, %s:" % ids
        for ci_str in ci_info:
            print "    %s" % ci_str

