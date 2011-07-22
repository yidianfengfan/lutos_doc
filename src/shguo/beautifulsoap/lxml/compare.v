cProfile.runctx("self.parse_with_beautifulsoup(html_data)", globals(), locals())
def parse_with_beautifulsoup(html_data):
  soup = BeautifulSoup.BeautifulSoup(html_data)
  links_res = soup.findAll("a", attrs={"class":"detailsViewLink"})
  links = [car_link["href"] for car_link in car_links_res]

  
root = lxml.html.fromstring(html_data)
links_lxml_res = root.cssselect("a.detailsViewLink")
links_lxml = [link.get("href") for link in links_lxml_res]
links_lxml = list(set(links_lxml))
