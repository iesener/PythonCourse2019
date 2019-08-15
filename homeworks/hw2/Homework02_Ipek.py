from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata
##
def divclass(i): ## This function will help me reach the specific divisions each petition is 
  if i == 1:     ## located in the main page.
    return "odd views-row-first"
  if i in [3,5,7,9,11,13,15,17,19]:
    return "odd"
  if i in [2,4,6,8,10,12,14,16,18]:
    return "even"
  if i == 20:
    return "even views-row-last"

with open('hw02_ipek.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("title", "date", "issues", "number_of_signatures"))
  w.writeheader()
  ##
  petitions = []
  for j in range(0, 5):  ## This feature helps me load the next page.
    web_page = urllib.request.urlopen("https://petitions.whitehouse.gov/petitions?page=%s" %j)
    all_html = BeautifulSoup(web_page.read())
    for i in range(1,21):   ## To refer to each of the 20 petitions in each page.
      sub = all_html.find_all('div',{'class': 'views-row views-row-%s views-row-%s' %(i,divclass(i))})
      if sub != []:      ## This feature helps me keep the number of total petitions unknown.
        for row in sub:
          petition ={}
          extension = row.a["href"]
          petition["title"] = row.a.text
          petition["number_of_signatures"] = row.find('span', {'class' : 'signatures-number'}).get_text()
          try:      ## For the petitions that do not have "issue" info.
            petition["issues"] = row.h6.get_text()
          except AttributeError:
            petition["issues"] = "NA"
          petition_page = urllib.request.urlopen('https://petitions.whitehouse.gov%s' % extension)
          petition_html = BeautifulSoup(petition_page.read())
          date_text = petition_html.find('h4', {"class": "petition-attribution"}).get_text()
          petition["date"] = date_text.split("on ",1)[1]
          w.writerow(petition)
      if sub == []:
        break






