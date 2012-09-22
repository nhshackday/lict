import nltk

DATA_FILE='/opt/nhshackday/je4d/nhshackday/pmcid/competing-interest-statements-stripped'

def load_data(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            bits = line.split(':')
            data += [{'filename': bits[0], 'text': bits[1]}]

    return data

def extract_orgs(text):
    tokens = nltk.wordpunct_tokenize(text)
    tagged_text = nltk.pos_tag(nltk.Text(tokens))
    chunks = nltk.ne_chunk(tagged_text)
    def sub_leaves(tree, nodes):
        return [t.leaves() for t in tree.subtrees(lambda s: s.node in nodes)]
    list_of_list_of_tuples = sub_leaves(chunks, ('ORGANIZATION', 'PERSON'))
    return [' '.join([tag_tuple[0] for tag_tuple in list_of_tuples]) for list_of_tuples in list_of_list_of_tuples]

if __name__ == '__main__':
    data = load_data(DATA_FILE)
    for x in data:
        print "%s: %s" % (x['filename'], extract_orgs(x['text']))
