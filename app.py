import requests
from bs4 import BeautifulSoup
import play_scraper
import xlwt
from tempfile import TemporaryFile
from datetime import datetime

#page = requests.get('https://play.google.com/store/apps/category/ART_AND_DESIGN')
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('a'))

#mydivs = soup.findAll("div", {"class": "ZmHEEd"})

#print(mydivs)

#mysubdivs = soup.findAll("div", {"class": "ImZGtf mpg5gc"})
#mysubdivs = mysubdivs.findAll("div", {"class": "ImZGtf mpg5gc"})
#print(mysubdivs[0])

test = play_scraper.search('Art',page=1,detailed =True)
#print(test)
final_array = []

for id,x in enumerate(test):
    #print(x)
    detail_data = []
    z = []
    for y in x:
        #print(y+':', x[y])
        if y is 'app_id':
            #print(x[y])
            detail_data = play_scraper.details(x[y])
            #test.append(detail_data['category'])
            #print(detail_data)
    z = {**x, **detail_data}
    #print(z)
    final_array.append(z)

#print(final_array)
exit()
book = xlwt.Workbook()
sheet1 = book.add_sheet('FAMILY_PRETEND')
sheet1.write(0,0,'App')
sheet1.write(0,1,'Category')
sheet1.write(0,2,'Rating')
sheet1.write(0,3,'Reviews')
sheet1.write(0,4,'Size')
sheet1.write(0,5,'Installs')
sheet1.write(0,6,'Type free = true')
sheet1.write(0,7,'Price')
sheet1.write(0,8,'Content Rating')
sheet1.write(0,9,'Genres')
sheet1.write(0,10,'Last Updated')
sheet1.write(0,11,'Current Ver')
sheet1.write(0,12,'Android Ver')

i=1;
for sub in final_array:
    #print(sub)
    sheet1.write(i,0,sub['title'])
    sheet1.write(i,1,sub['category'])
    sheet1.write(i,2,sub['score'])
    sheet1.write(i,3,sub['reviews'])
    sheet1.write(i,4,sub['size'])
    sheet1.write(i,5,sub['installs'])
    if sub['free'] == True:
        sheet1.write(i,6,'Free')  # type
    else:
        sheet1.write(i,6,'Paid')  # type
    sheet1.write(i,7,sub['price'])
    sheet1.write(i,8,sub['content_rating'])
    sheet1.write(i,9,' ')
    sheet1.write(i,10,sub['updated'])
    sheet1.write(i,11,sub['current_version'])
    sheet1.write(i,12,sub['required_android_version'])
    i = i+1

now = datetime.now()
timestamp = datetime.timestamp(now)
name = "random_"+str(timestamp)+".xls"
book.save(name)
book.save(TemporaryFile())


#print(play_scraper.details('com.android.chrome'))

#print(play_scraper.developer('Disney', results=5))

#print(play_scraper.suggestions('cat'))

#print(play_scraper.similar('com.supercell.clashofclans', results=5))

#print(play_scraper.collection(collection='TRENDING',category='ART_AND_DESIGN',results=5,page=1))
#print(play_scraper.details('com.android.chrome'))

#print(play_scraper.categories())
