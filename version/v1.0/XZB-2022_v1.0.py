from http.client import RESET_CONTENT
import urllib.request as req
import requests
import termcolor
import os,wget,time
import pyrebase



firebaseConfig = {
    'apiKey': "AIzaSyByaTEKgDvQ1bIl2op11mFgKEsmmJCVe3A",
    'authDomain': "xzb-2022.firebaseapp.com",
    'projectId': "xzb-2022",
    'storageBucket': "xzb-2022.appspot.com",
    'messagingSenderId': "709445052764",
    'appId': "1:709445052764:web:b0d093fc52722f49617999",
    'measurementId': "G-D3JRHES3TP",
    'databaseURL': ""
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login():
    try:
        login = auth.sign_in_with_email_and_password(account, password)
        #print('[ 登入成功 ]\n')
        status = True
        return status
    except:
        #print('[ 登入失敗 ]\n')
        status = False
        return status



class bcolors:
    R = '\033[91m'      #RED
    G = '\033[92m'      #GREEN
    Y = '\033[93m'      #YELLOW
    RESET = '\033[0m'   #RESET COLOR

Code = '0096'
StuPass = ''
StuSN = ''
os.system('color')
print('''
 __   __ __________      ___   ___ ___  ___  
 \ \ / /|___  /  _ \    |__ \ / _ \__ \|__ \ 
  \ V /    / /| |_) |_____ ) | | | | ) |  ) |
   > <    / / |  _ <______/ /| | | |/ /  / / 
  / . \  / /__| |_) |    / /_| |_| / /_ / /_ 
 /_/ \_\/_____|____/    |____|\___/____|____| ©
                                             
''')
time.sleep(0.5)
print(termcolor.colored(
    bcolors.R +
    '''
    --------------------------------
    Please read the EULA below

    -Version 1.0-  -20220228-
       Copyright©2022 SCX
    
    此軟體僅供學術使用
    若用於商業或其他用途請自行承擔責任
    --------------------------------
    '''
    + bcolors.RESET
, "red"))
time.sleep(0.5)

#print(os.path.isfile('data.txt'))
if (os.path.isfile('data.txt') != True):    #若檔案不存在則手動登入
    while(login() != True):
        print('[登入]')
        account = input('請輸入賬號：')
        password = input('請輸入密碼：')
        login()
    StuPass = input('請輸入身份證後4碼：')
    StuSN = input('請輸入上課證學號：')
else:                                       #偵測到檔案自動登入
    txt = open(r'data.txt','r')
    data = txt.read().split(',')
    txt.close()
    print('已檢測到data.txt')
    StuPass = data[0]
    StuSN = data[1]
    account = data[2]
    password = data[3]
    login()
    while(login() != True):
        print('[自動登入失敗]')
        account = input('請輸入賬號：')
        password = input('請輸入密碼：')
        login()
    print('賬號：'+StuSN)
    print('密碼：'+StuPass)



while True:
    eula = input(termcolor.colored(bcolors.Y + '\n若繼續代表您已同意EULA\n是否繼續(Y/N)：' + bcolors.RESET, "yellow"))
    if eula=='N':
        break
    if eula=='n':
        break

    ClassID = str(input('請輸入課程代碼：'))
    urls1 = ('https://makeup.jlweb.com.tw/ClassList2.aspx?ClassID=' + ClassID + '&Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(urls1) as response:
        datas1 = response.read().decode('utf-8')
    #print(datas1)
    classList = datas1.split('<br/>')
    print('課程列表：\n')
    for i in range(0,(len(classList) - 1)):
        className = classList[i].split(',')
        print(' '+str(i+1) + ' | ' + className[0])

    classC = input('\n請選擇課堂：')
    classNum = classList[(int(classC) - 1)].split(',')
    MovieID = classNum[2]

    urls2 = ('https://makeup.jlweb.com.tw/MovieList.aspx?ClassID=' + ClassID + '&Code=' + Code + '&MovieID=' + MovieID + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(urls2) as response:
        datas2 = response.read().decode('utf-8')
    #print(datas2)
    movieList = datas2.split('<br/>')
    videoNum = len(movieList) - 1
    print('\n  - 開始下載 共' + str(videoNum) + '節 -')

    path = os.path.join('Class')
    if(os.path.isdir(path) != True):
        os.mkdir(path)

    className = classList[int(classC) - 1].split(',')

    for i in range(0,videoNum):
        movieList_first = movieList[i].split(',')
        videoCode = movieList_first[1]
        urls3 = ('http://xzb2022.duckdns.org/LocalUser/L096/' + str(videoCode) + '.mp4')
        r = requests.head(urls3, allow_redirects=True)
        print('')
        #print(r.url)
        print('正在下載 第' + str(i+1) + '節')
        save_as = os.path.join(path, className[0] + '_' + str(i+1) + '.mp4')
        wget.download(urls3, save_as)


