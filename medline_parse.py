import ffs
from neo4jrestclient.client import GraphDatabase

NEO4J_URL="http://localhost:7474/db/data/"
gdb = GraphDatabase(NEO4J_URL)
one_index_to_rule_them_all = gdb.nodes.indexes.create("one_index_to_rule_them_all")

datadir = ffs.Path(__file__).parent.abspath + 'medline/data'
datadir = "/mnt/nhshackday/je4d/medline-scrape/data"

def save_medline_to_neo4j(medliner):
    try:
        node = one_index_to_rule_them_all.get('pmid', medliner['pmid'])[0]
    except IndexError:
        node =  gdb.node()
    node.update(medliner)
    one_index_to_rule_them_all.add('pmid', str(medliner['pmid']), node)

def parse_medline_data():
    for medfile in datadir:
        meddic = {}
        for line in medfile:
            for key, val in line.split('-'):
                meddic[key.strip().lower().replace(' ', '')] = val.strip()

        save_medline_to_neo4j(meddic)


if __name__ == '__main__':
    parse_medline_data()
