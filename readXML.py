from xml.dom import minidom
import searchResult
from pathlib import Path


def parse_xml(file, church, all_pages):
    my_file = Path(file)
    if (not my_file.is_file()):
        print(file + " doesn't exist, returning nothing")
        return

    myDoc = minidom.parse(file)
    urls = myDoc.getElementsByTagName('url')

    # build object for each url
    for url in urls:
        sr = searchResult.SearchResult()
        sr.church = church
        sr.resourceURL = url.getElementsByTagName('loc')[0].firstChild.data
        sr.lastmod = url.getElementsByTagName('lastmod')[0].firstChild.data
        if url.getElementsByTagName('image:title'):
            sr.title = url.getElementsByTagName('image:title')[0].firstChild.data
        else:
            # TODO: What do we do with urls that don't have an image title?
            # TODO: Could just use the last section of the url?
            sr.title = 'No Title Found'
        if url.getElementsByTagName('image:loc'):
            sr.thumbnailURL = url.getElementsByTagName('image:loc')[0].firstChild.data

        all_pages.append(sr)

    # print(srList[10].resourceURL)
    return all_pages
    # print(url.attributes['image'].value)


# TODO: Jonnathan fix downtown pls
all_pages = []
parse_xml('LexingtonSiteMap.xml', 'Lexington', all_pages)
parse_xml('DowntownSiteMap.xml', 'Downtown', all_pages)
parse_xml('TwoNotchSiteMap.xml', 'TwoNotch', all_pages)
parse_xml('ColumbiaSiteMap.xml', 'Columbia', all_pages)


print('Number of links included in all sitemaps: ' + str(len(all_pages)))
for obj in all_pages:
    if obj.thumbnailURL == '':
        print(obj)


for obj in all_pages[300:310]:
    print(obj)
# print(all_pages[500:505])