#!/opt/nhshackday/wip/lict/bin/python
# vim: set sw=4 sts=4 ts=4 et:
import re
from lxml import etree
from pyquery import PyQuery as pq
import urllib
import subprocess
import os
import sys

terms_fp = "/mnt/nhshackday/je4d/mesh-term-ids"
#/mnt/nhshackday/je4d/medline-scrape/data
if __name__ == "__main__":
    dir = sys.argv[1]

    terms = open(terms_fp, 'r')
    tmap = {}
    for term in terms.readlines():
        tid, tstr = term.split(",", 1)
        tmap[tstr.strip().lower()] = tid.strip()

    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        for fn in map(lambda x: os.path.join(dirname, x), filter(lambda f:f.endswith(".medline"), filenames)):
            f = open(fn, 'r')
            pmid = re.sub(".*/", "", fn.replace(".medline",""))
            tids=[]
            for line in f.readlines():
                try:
                    mkey, mdata = line.split("-", 1)
                    mkey = mkey.strip()
                    if mkey != "MH":
                        continue
                    mdata_list = mdata.split(",")
                    for mdata in mdata_list:
                        if mdata.find("*") == -1:
                            continue
                        mdata = mdata.strip().replace("*","")
                        try:
                            tids.append(tmap[mdata.lower()])
                        except KeyError, e:
                            continue
                except ValueError, e:
                    pass
            if tids:
                print "%s,%s" % (pmid, ','.join(tids))
