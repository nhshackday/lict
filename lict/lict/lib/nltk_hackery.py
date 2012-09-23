import nltk

DATA_FILE='/mnt/nhshackday/je4d/pubmed-scrape/xml/00/*'

def load_data(pathspec):
    import extract_ci
    from pyquery import PyQuery as pq
    import glob
    data = []

    file_list = glob.glob(pathspec)[:50]
    for filename in file_list:
        with open(filename) as f:
            article_doc = pq(filename=filename)
            text = ' '.join(extract_ci.ci_info_list(article_doc))
            data += [{'filename': filename, 'text': text}]

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
