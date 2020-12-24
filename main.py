import requests
import lxml.etree
import lxml.html

p1 = "//p/a[not(preceding::a/. = .)]/@href[starts-with(.,'/wiki/') and contains(.,'_') and not(contains(.,':')) and not(contains(.,'(')) and not(contains(.,'#')) and not(contains(.,'.')) and not(contains(substring-after(., '_'), '_'))]"
p2 = "//p/a[not(preceding::a/. = .)]/@href[starts-with(.,'/wiki/') " \
     "and contains(.,'_') " \
     "and not(contains(substring-after(., '_'), '_')) " \
     "and not(contains(., 'International')) " \
     "and not(contains(., 'medal')) " \
     "and not(contains(., 'Cup')) " \
     "and not(contains(., 'Fighter')) " \
     "and not(contains(., 'language')) " \
     "and not(contains(., 'Open')) " \
     "and not(contains(., 'America')) and not(contains(., 'Africa')) and not(contains(., 'Asia')) and not(contains(., 'Antarctica')) and not(contains(., 'Europe')) and not(contains(., 'Australia'))" \
     "and not(contains(., 'Strings')) " \
     "and not(contains(., 'Serve')) " \
     "and not(contains(., 'Nike')) " \
     "and not(contains(., 'Inc.')) " \
     "and not(contains(., 'Masters')) " \
     "and not(contains(., 'Skyhook')) " \
     "and not(contains(., 'Ball')) " \
     "and not(contains(., 'Sports')) " \
     "and not(contains(., 'Bagel')) " \
     "and not(contains(., 'Indoors')) " \
     "and not(contains(., 'Finals')) " \
     "and not(contains(., 'Championships')) " \
     "and not(contains(., 'Smash')) " \
     "and not(contains(., 'brand')) " \
     "and not(contains(., 'Tweener')) and not(contains(., 'Award')) and not(contains(., 'Academy'))]"


def main():
    page = requests.get("https://en.wikipedia.org/wiki/Roger_Federer")
    # page = requests.get("https://en.wikipedia.org/wiki/Andy_Ram")
    doc = lxml.html.fromstring(page.content)
    urls = doc.xpath(p1)
    for url in urls:
        print(url)
    print(len(urls))


if __name__ == '__main__':
    main()

