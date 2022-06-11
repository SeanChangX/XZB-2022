from http.client import RESET_CONTENT
import urllib.request as req

Code = '0096'
StuPass = input('請輸入身份證後四碼: ')
StuSN = input('請輸入學號: ')

url = ('https://makeup.jlweb.com.tw/ClassList1.aspx?Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
with req.urlopen(url) as response:
    data = response.read().decode('utf-8')
print(data)
print('\n\n\n--------------------------------')

urlStu = ('https://makeup.jlweb.com.tw/StuLogin.aspx?Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
with req.urlopen(urlStu) as response:
    dataStu = response.read().decode('utf-8')
    dataStu = dataStu.split(',')
print('查詢同學 【'+ dataStu[1] + '】 的課程\n')


classList = data.split('<br/>')
for i in range(0,(len(classList) - 1)):
    className = classList[i].split(',')
    #print(className)
    classNum = className[0]
    classTitle = className[1]
    classN = classNum.split(';')
    print(classN[1] + ' | ' + classTitle)

print('--------------------------------\n\n\n')