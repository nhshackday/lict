import csv, urllib,urllib2
import lxml.html
import os, sys

params = {"EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.SearchResourceList":"pubmed",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.Term":"womble",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.FeedLimit":"15",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.FeedName":"womble",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_SearchBar.CurrDb":"pubmed",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_PageController.PreviousPageName":"results",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_Facets.FacetsUrlFrag":"filters=",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_Facets.FacetSubmitted":"false",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPresentation":"medline",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPageSize":"20",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sSort":"none",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FFormat":"docsum",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FSort":"",
"email_format":"docsum",
"email_sort":"",
"email_count":"20",
"email_start":"1",
"email_address":"",
"email_subj":"womble - PubMed",
"email_add_text":"",
"citman_count":"20",
"citman_start":"1",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileFormat":"docsum",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPresentation":"docsum",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Presentation":"medline",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize":"20",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPageSize":"20",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Sort":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastSort":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileSort":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Format":"text",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastFormat":"",
"CitationManagerStartIndex":"1",
"CitationManagerCustomRange":"false",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Entrez_Pager.cPage":"1",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Entrez_Pager.CurrPage":"1",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_ResultsController.ResultCount":"304814",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_ResultsController.RunLastQuery":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_RVDocSum.uid":"22995344",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Entrez_Pager.cPage":"1",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPresentation2":"docsum",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPageSize2":"20",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sSort2":"none",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FFormat2":"docsum",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FSort2":"",
"email_format2":"docsum",
"email_sort2":"",
"email_count2":"20",
"email_start2":"1",
"email_address2":"",
"email_subj2":"womble - PubMed",
"email_add_text2":"",
"citman_count2":"20",
"citman_start2":"1",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.TimelineAd.CurrTimelineYear":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_MultiItemSupl.RelatedDataLinks.rdDatabase":"rddbto",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Pubmed_MultiItemSupl.RelatedDataLinks.DbName":"pubmed",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.Discovery_SearchDetails.SearchDetailsTerm":'wombles"[MeSH Terms] OR "dogs"[All Fields] OR "dog"[All Fields]',
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.HistoryDisplay.Cmd":"displaychanged",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailReport":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailFormat":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailCount":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailStart":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailSort":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.Email":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailSubject":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailText":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.EmailQueryKey":"",
"EntrezSystem2.PEntrez.Pubmed.Pubmed_ResultsPanel.EmailTab.QueryDescription":"",
"EntrezSystem2.PEntrez.DbConnector.Db":"pubmed",
"EntrezSystem2.PEntrez.DbConnector.LastDb":"pubmed",
"EntrezSystem2.PEntrez.DbConnector.Term":"womble",
"EntrezSystem2.PEntrez.DbConnector.LastTabCmd":"",
"EntrezSystem2.PEntrez.DbConnector.LastQueryKey":"1",
"EntrezSystem2.PEntrez.DbConnector.IdsFromResult":"22990813",
"EntrezSystem2.PEntrez.DbConnector.LastIdsFromResult":"",
"EntrezSystem2.PEntrez.DbConnector.LinkName":"",
"EntrezSystem2.PEntrez.DbConnector.LinkReadableName":"",
"EntrezSystem2.PEntrez.DbConnector.LinkSrcDb":"",
"EntrezSystem2.PEntrez.DbConnector.Cmd":"displaychanged",
"EntrezSystem2.PEntrez.DbConnector.TabCmd":"",
"EntrezSystem2.PEntrez.DbConnector.QueryKey":"",}


def fetch_id(id):
    params['EntrezSystem2.PEntrez.DbConnector.IdsFromResult'] = str(id)
    data=urllib.urlencode(params)
    req=urllib2.Request("http://www.ncbi.nlm.nih.gov/pubmed", data)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    page=urllib2.urlopen(req).read()
    return page

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
        data = fetch_id(id)
        page = lxml.html.fromstring(data)
        content = page.cssselect('pre')[0].text_content()
        open("data/%s.medline" % id,"wb").write(content.strip())

