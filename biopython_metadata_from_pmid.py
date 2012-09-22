from Bio import Entrez

def getmedline(id):
    Entrez.email = "drcjar@gmail.com"
    fetch_handle = Entrez.efetch(db="pubmed", id=id, rettype="medline", retmode="text")
    return fetch_handle.read()
