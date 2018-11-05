import urllib.request

def get_html(url):
    fp = urllib.request.urlopen(url)
    htmlbytes = fp.read()

    html = htmlbytes.decode("utf8", errors='replace')
    fp.close()
    return html
