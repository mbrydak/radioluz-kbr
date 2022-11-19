from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import urllib.parse as urlparse
import urllib.error
import os


url = "https://badaniaradiowe.pl/wyniki-sluchalnosci/dane-historyczne/"
req = requests.get(url)
soup = bs(req.text, "html.parser")

#get all links
def get_links():
    links = []
    for link in soup.find_all('a', class_="file_download"):
        links.append(link.get('href'))
    return links

# iterate through links and download files
for link in get_links():
    # get filename from url
    filename = os.path.basename(urlparse.urlsplit(link).path)
    filename_encoded = urlparse.quote(filename)

    # replace filename in url
    link = link.replace(filename, filename_encoded)

    fullfilename = os.path.join("data", filename)
    # download file
    try:
        print(f"Downloading {filename} to {fullfilename}")
        urllib.request.urlretrieve(link, fullfilename)
    except urllib.error.URLError as e:
        print(f"Error {e.code} while downloading {filename} from {link}")
