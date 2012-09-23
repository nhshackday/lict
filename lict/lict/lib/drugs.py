#!/opt/nhshackday/wip/lict/bin/python
# vim: set sw=4 sts=4 ts=4 et:
import re
from lxml import etree
from pyquery import PyQuery as pq
import urllib
import subprocess
import os
import sys
import pprint

drugs_fp = "/mnt/nhshackday/je4d/drugs"

def druglist():
    drugs_f = open(drugs_fp, 'r')
    dlist = []

    for drug in drugs_f.readlines():
        did, dstr = drug.split(",", 1)
        did = did.strip()
        dstr = dstr.strip().lower()
        dlist.append((did, dstr))
    return dlist

if __name__ == "__main__":
    pprint.pprint(druglist())
