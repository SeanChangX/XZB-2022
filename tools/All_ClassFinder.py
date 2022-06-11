from http.client import RESET_CONTENT
import urllib.request as req

Code = '0096'
StuPass = input('請輸入身份證後四碼: ')
StuSN = input('請輸入學號: ')
Num = int(input('欲查看之範圍末號: '))
print('\n\n\n--------------------------------')

for ClassID in range(0,Num+1):
    url = ('https://makeup.jlweb.com.tw/ClassList2.aspx?ClassID=' + str(ClassID) + '&Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(url) as response:
        data = response.read().decode('utf-8')
    if(data != ''):
        dataS1 = data.split('<br/>')
        dataS2 = dataS1[0].split(',')
        #print(url)
        #print(data)
        print((str(ClassID)) + ' | ' + dataS2[0])
print('--------------------------------\n')