#!/opt/nhshackday/wip/lict/bin/python -u
# vim: set sw=4 sts=4 ts=4 et:
import re
from lxml import etree
from pyquery import PyQuery as pq
import urllib
import subprocess
import os
import sys
import drugs

terms_fp = "/mnt/nhshackday/je4d/mesh-term-ids"
#/mnt/nhshackday/je4d/medline-scrape/data
if __name__ == "__main__":
    dir = sys.argv[1]

    druglist = drugs.druglist()
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        for fn in map(lambda x: os.path.join(dirname, x), filter(lambda f:f.endswith(".nxml"), filenames)):
            """
            For each article.nxml, search it for each drugname in the drug list,
            and print a CSV line of "pmc_id,drug_id,drug_id,..." if any drugs
            were found
            """
            pmc = re.sub(".*/", "", fn.replace(".nxml",""))

            f = open(fn, 'r')
            fdata = f.read().lower()
            dids = []

            for did, dstr in druglist:
                if fdata.find(dstr) != -1:
                    dids.append(did)
            if dids:
                print "%s,%s" % (pmc, ','.join(dids))
