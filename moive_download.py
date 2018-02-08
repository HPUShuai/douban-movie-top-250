import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(i * 25)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    target = soup.find_all('div',class_="info")
    target1 = soup.find_all('div',class_="star")
    # for each in target1:
    #     content = each.text.replace(" ","").replace("\n","")
    #     print(content[0:3],content[4:])
    for each in target:
        title = each.a.span.text
        name = each.p.text
        name1 = name.replace(" ","").replace("\n"," ").replace("...","....").replace("/","")
        director = name1.split()[0]   #导演
        star = name1.split()[1]
        time = name1.split()[2]
        country = name1.split()[3]
        # types = name1.split()[4]
        # print(director,star,time,country)
        # print(name1)
        print(title)
