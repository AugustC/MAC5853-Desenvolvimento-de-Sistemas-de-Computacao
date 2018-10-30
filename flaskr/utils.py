import urllib.request

def get_html(url):
    fp = urllib.request.urlopen(url)
    htmlbytes = fp.read()

    html = htmlbytes.decode("utf8")
    fp.close()
    return html
