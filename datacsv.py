
import requests, csv
from bs4 import BeautifulSoup as bs


# # with open("Query.csv", newline='') as csvfile:
# #     reader = csv.DictReader(csvfile)
# #     print(reader)
# #     for i in reader:
# #
# #         print("i")
#
# import pandas
# # df = pandas.read_csv("Query.csv")
# # print(df)
# da=StaticData.STOPWORD_DIR + "/QueryResults-2.csv"
# print(StaticData.STOPWORD_DIR + "/QueryResults-2.csv")
file = open("Query.csv")

print(type(file))
csvreader = csv.reader(file)

rows = []
titlelist=[]
answerlist=[]
data=[]
# for row in csvreader:
#         rows.append(row)
#         titlelist.append(row[3])
#         answerlist.append(row[4])
#         soup = bs(row[4], "html.parser")
#         pre1 = soup.find_all('pre')
#         code1 = soup.find_all('code')
#         data=[row[3],row[4],code1,pre1]
#         # print(data)
#         # print(row[3])
#         # print(row[4])
# # print(row)
# # print(type(answerlist[3]))
# soup=bs(answerlist[3], "html.parser")
# # print(type(soup))
# pre1=soup.find_all('pre')
# code1=soup.find_all('code')
# # print(pre1)
# # print(code1)
header = ['title','answer', 'code', 'pre']


with open('4192.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    print(csvreader)
    i=0
    for row in csvreader:
        # print(row)
        if i !=0:
            soup = bs(row[4], "html.parser")
            pre1 = soup.find_all('pre')
            code1 = soup.find_all('code')
            data1 = [row[3], row[4], code1, pre1]
            print(data1)
            writer.writerow(data1)
        i+=1


    # write the data
    # writer.writerow(data)