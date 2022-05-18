from bs4 import BeautifulSoup
from requests import get

url = 'https://www.gov.pl/web/rdos-kielce/mapa-strony?show-bip=true'

page = get(url)
bs = BeautifulSoup(page.content,'html.parser')
ul = bs.find_all('ul',{'id':'page-list_20458818','class':{'page-link-list','bip-children'}})

i=0
obwieszczenia = []
linki = []
for items in ul:
	spans = items.find_all('span',class_='')
	anchors = items.find_all('a', href=True)
	for span in spans:
		obwieszczenia.append(span.get_text())
	for a in anchors:
		url = "https://www.gov.pl" + str(a['href'])
		linki.append(url)

ilosc = len(obwieszczenia)
print(f"Ilość obwieszczeń w 2022 roku: {ilosc}")

print('>>>>>>>>>>>>>> WYKAZ OBWIESZCZEŃ <<<<<<<<<<<<<<<< ')
for o in obwieszczenia:
	print(o)
print('>>>>>>>>>>>>>> WYKAZ LINKÓW <<<<<<<<<<<<<<<< ')
for l in linki:
	print(l)




