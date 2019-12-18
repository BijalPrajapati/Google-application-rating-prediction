import pandas as pd
import numpy as np

def convert_free(cell):
    if cell == 'Free':
        return 'True'
    else:
        return 'False'

def convert_size(cell):
    #print(cell)
    if cell == 'Varies with device':
        return '20M'
    else:
        return cell

def convert_android(cell):
    if cell == 'Varies with device':
        return '4.1'
    else:
        return cell

def convert_version(cell):
    if cell == 'Varies with device':
        return '1'
    else:
        return cell

def conver_mbtokb(cell):
    print(cell)
    kbval = float(cell)*1024.0
    print(kbval)
    return kbval

def type_cat(types):
    if types == 'Free':
        return '0'
    else:
        return '1'

df = pd.read_excel('final4.xls','Sheet1', converters = {
 #   'Size' : conver_mbtokb,
  #  'Paid_Free' : type_cat,
   # 'Android Ver' : convert_android,
    #'Current Ver' : convert_version
})


df
#print(df.head())
#print(df['App'])
#print(df['Paid_Free'])

#df.to_excel('final.xls', sheet_name='Sheet1')
#df1 = pd.read_excel('final.xls','Sheet1')
#df['Rating'].replace('', np.nan, inplace=True)
#print(df['Rating'])
#df.dropna(subset=['Rating'], inplace=True)

# review
#df['Reviews'].replace(0, np.nan, inplace=True)
#print(df['Reviews'])
#df.dropna(subset=['Reviews'], inplace=True)

#df = df.set_index("Reviews")
#df = df.drop(0, axis=0)
#df.drop_duplicates(subset =["App"], keep = 'last' , inplace = True)
#print(df['App'].is_unique)

#df['Price'] = df['Price'].str.replace(r'\$', '')

#df['Size'] = df['Size'].str.replace(r'M', '')
#df['Installs'] = df['Installs'].str.replace(r'+', '')


#Cleaning of content rating classification
RatingL = df['Content Rating'].unique()
RatingDict = {}
for i in range(len(RatingL)):
    RatingDict[RatingL[i]] = i
df['Content Rating'] = df['Content Rating'].map(RatingDict).astype(int)

#df.sort_values("Category", inplace = True)

df.to_excel('final4.xls', sheet_name='Sheet1')