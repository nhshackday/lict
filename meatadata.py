"""
Extract Metadata about Publications not in raw XML data.
"""

import sys
import ffs
import requests

here = ffs.Path().abspath

datadir = here + 'data'
outputs = datadir + 'meat'
idfile = datadir + 'ids'

def cull_meat(pmid):
    cookies = {
        'ncbi_sid': '396D70DE05DB2651_0096SID',
        'WebEnv': '1P9PyOxzawYGNlCcA01Q4vezB36qanWgdwDCdn7witYHUY9nMvcjabWL8pBPo5XQWshzRe6a3qcLXNiQjefPJezRbStShxzxXDmEEu%40396D70DE05DB2651_0096SID'
        }

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0 Iceweasel/11.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referrer': 'http://www.ncbi.nlm.nih.gov/pubmed?term={0}%5Buid%5D'.format(pmid),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-us,en;q=0.5'
        }

    resp =  requests.post(
        'http://www.ncbi.nlm.nih.gov/pubmed',
        cookies = cookies,
        headers = headers,
        data = {
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.SearchResourceList': 'pubmed',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.Term': '{0}[uid]'.format(pmid),
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.FeedLimit': '15',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.FeedName': '{0}[uid]'.format(pmid),
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.CurrDb': 'pubmed',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_PageController.PreviousPageName': 'results',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPresentation': 'medline',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FFormat': 'abstract',
            'email_format':  'abstract',
            'email_address': '',
            'email_subj': '{0}[uid] - PubMed'.format(pmid),
            'email_add_text': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileFormat':'abstract',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPresentation': 'abstract',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Presentation': 'medline',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize': '20',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPageSize': '20',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Sort': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastSort': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileSort': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Format': 'text',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastFormat':'',
            'CitationManagerStartIndex': '1',
            'CitationManagerCustomRange': 'false',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_ResultsController.ResultCount': '1',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_ResultsController.RunLastQuery': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Discovery_SearchDetails.SearchDetailsTerm': '{0}[uid]'.format(pmid),
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.HistoryDisplay.Cmd': 'displaychanged',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailReport': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailFormat':'',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailCount': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailStart': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailSort': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.Email': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailSubject': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailText': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailQueryKey': '',
            'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.QueryDescription': '',
            'EntrezSystem2.PEntrez.DbConnector.Db': 'pubmed',
            'EntrezSystem2.PEntrez.DbConnector.LastDb': 'pubmed',
            'EntrezSystem2.PEntrez.DbConnector.Term': '{0}[uid]'.format(pmid),
            'EntrezSystem2.PEntrez.DbConnector.LastTabCmd': '',
            'EntrezSystem2.PEntrez.DbConnector.LastQueryKey': '1',
            'EntrezSystem2.PEntrez.DbConnector.IdsFromResult': '',
            'EntrezSystem2.PEntrez.DbConnector.LastIdsFromResult': '',
            'EntrezSystem2.PEntrez.DbConnector.LinkName': '',
            'EntrezSystem2.PEntrez.DbConnector.LinkReadableName': '',
            'EntrezSystem2.PEntrez.DbConnector.LinkSrcDb': '',
            'EntrezSystem2.PEntrez.DbConnector.Cmd': 'displaychanged',
            'EntrezSystem2.PEntrez.DbConnector.TabCmd': '',
            'EntrezSystem2.PEntrez.DbConnector.QueryKey': '',
            'p$a': 'EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.SetDisplay',
            'p$l': 'EntrezSystem2',
            'p$st': 'pubmed'
            }
        )
    return resp.content

if __name__ == '__main__':
    with idfile.csv() as csv:
        for pmid, pmc in csv:
            print 'Fetching', pmid
            meatfile = outputs + '{0}.txt'.format(pmid)
            meatfile << cull_meat(pmid)
