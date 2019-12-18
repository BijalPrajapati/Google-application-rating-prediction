import play_scraper
import xlwt
from tempfile import TemporaryFile

category = play_scraper.categories()
#print(category)
final_category = []

for temp_cat in category:
    final_category.append(category[temp_cat])

book_cat = xlwt.Workbook()
sheet1 = book_cat.add_sheet('Category')
sheet1.write(0,0,'Category Id')
sheet1.write(0,1,'Category')
sheet1.write(0,2,'Url')

i=1;
for cat in final_category:
    sheet1.write(i,0,cat['category_id'])
    sheet1.write(i,1,cat['name'])
    sheet1.write(i,2,cat['url'])
    i = i+1

name = "category.xls"
book_cat.save(name)
book_cat.save(TemporaryFile())