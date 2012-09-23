import csv, urllib,urllib2
import lxml.html
import os, sys
from biopython_metadata_from_pmid import getmedline

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Need the input CSV as a param"
        sys.exit(0)
    # No buffering thanks
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    print 'Loading %s' % sys.argv[1]
    reader = csv.reader(open(sys.argv[1]))
    for row in reader:
        id = row[0]
        if  not id or os.path.exists("data/%s.medline" % id):
            print 'Skipping ID %s\r' %  id,
            continue
        print 'Loading ID %s\r' %  id,
        content = getmedline(id) 
        open("data/%s.medline" % id,"wb").write(content.strip())

