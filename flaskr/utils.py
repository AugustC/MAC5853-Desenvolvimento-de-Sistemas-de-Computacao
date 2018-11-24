from urllib.request import Request, urlopen

def get_html(url):
    q = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    htmlbytes = urlopen(q).read()

    html = htmlbytes.decode("utf8", errors='replace')
    return html
