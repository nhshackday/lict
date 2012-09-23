#!/opt/nhshackday/wip/lict/bin/python
# vim: set sw=4 sts=4 ts=4 et:
from lict_common import *
import subprocess
import os
import pprint
import sys

NXMLDIR = "/mnt/nhshackday/je4d/pubmed-scrape/xml"

if __name__ == "__main__":
    if not sys.argv[1]:
        sys.exit(0)
    for i in sys.argv[1:]:
        for filename, doc in filter_by_article_type("research-article", xmldocs_in_dir(os.path.join(NXMLDIR, i))):
            try:
                pmid, pmc = pubmed_ids(doc)
                if pmid:
                    print "%s, %s" % (pmid, pmc)
            except Exception, e:
                    pass

