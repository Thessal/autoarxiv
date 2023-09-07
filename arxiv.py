
import urllib.request as libreq
import urllib
import feedparser

def get_arxiv(query):
    query = urllib.parse.quote(query, safe='/', encoding=None, errors=None)
    with libreq.urlopen(f'https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=1') as url:
        r = url.read()

    feed = feedparser.parse(r)
    item = feed["entries"][0]
    item_id = item["id"]
    item_title = item["title"]
    item_author = item["author"]
    item_pdf = None
    for x in item["links"]:
        if x['type'] == 'application/pdf':
            item_pdf = x['href']
            if not item_pdf.endswith(".pdf"):
                item_pdf += ".pdf"
            break
    
    if item_pdf : 
        result = {"id":item_id, "title":item_title, "author":item_author, "pdf":item_pdf}
    else :
        result = None
    return result
