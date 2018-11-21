import requests
from bs4 import BeautifulSoup
import csv
import os

def write_sitemap_to_xml(path, church):
    page = requests.get(path)
    print(page)
    if (page.status_code != 200):
        print('STEW MAYBE YOU SHOULD WRITE SOME CODE TO HANDLE A NON 200 RESPONSE')
        print(page.status_code)
    contents = page.content
    strContents = contents.decode('utf-8')
    strContents = strContents.replace(r'\r\n', '')
    strContents = strContents.replace(r'<?xml version="1.0" encoding="UTF-8"?>', '')

    siteMapName = church + 'Sitemap.xml'
    with open(siteMapName, "w") as text_file:
        text_file.write(strContents)



# TODO: Get Jonnathan to turn off the ssl stuff when we make these crawls.
print('writing lexington to xml')
write_sitemap_to_xml('http://midtownlexington.com/sitemap.xml', "Lexington")

print('writing downtown to xml')
# write_sitemap_to_xml('http://midtowndowntown.com/sitemap.xml', "Downtown")

print('writing columbia to xml')
write_sitemap_to_xml('http://midtowncolumbia.com/sitemap.xml', "Columbia")

print('writing twonotch to xml')
write_sitemap_to_xml('http://midtowntwonotch.com/sitemap.xml', "TwoNotch")









