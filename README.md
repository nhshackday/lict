lict
====

Systematic bias favours products which are made by the company funding the research. Explanations 
include the selection of an inappropriate comparator to the product being investigated and publication
bias (http://www.ncbi.nlm.nih.gov/pubmed/12775614)
 
Conflict of interest (or competing interest) statements and medline metadata describe the funding 
of research and potential sources of bias.

We made a tool for visualising and tracking relationships between papers and their conflict of interests.

Later we might make a simple measure, the conflict of interest index, which describes the proportion of 
papers for a given drug treatment, that have received industry funding or declare a conflict of interest. 

It also might integrate with www.openbnf.org and www.burningyourmoney.org :-)

Conflict of interestz!

http://wiki.nhshackday.com/wiki/Conflict%20of%20interest

## Getting Started

### Get the code

```bash
$ git clone https://github.com/nhshackday/lict
$ cd lict
$ virtualenv $WHERE_YOU_LIKE_TO_KEEP_VIRTUALENVS/lict
$ . $WHERE_YOU_LIKE_TO_KEEP_VIRTUALENVS/lict/bin/activate
$ pip install -r requirements.txt
```

### Get the NLTK dependencies

```bash
$ python -m nltk.downloader maxent_treebank_pos_tagger words maxent_ne_chunker
```

### Sort out your data

```bash
$ python lict/manage.py syncdb --noinput
$ python lict/manage.py migrate
$ #TODO Integrate instructions from pubmed-download-HOWTO / medline-scrape-HOWTO
```
