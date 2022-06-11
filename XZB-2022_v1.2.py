# 重點更新
# - 引入下載器


from http.client import RESET_CONTENT
import urllib.request as req
import requests
import termcolor
import os, time, wget, re
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
                                             
    - For Educational Purposes Only -
''')
time.sleep(0.2)
print(termcolor.colored(
    bcolors.R +
    '''
    --------------------------------
    Please read the EULA below

    -Version 1.2-  -20220320-
       Copyright©2022 SCX
    
    此軟體僅供學術使用
    若用於商業或其他用途請自行承擔責任
    --------------------------------
    '''
    + bcolors.RESET
, "red"))
time.sleep(0.2)

#print(os.path.isfile('data.txt'))
if (os.path.isfile('data.txt') != True):    #若檔案不存在則手動登入
    while(login() != True):
        print('[登入]')
        account = input('請輸入賬號: ')
        password = input('請輸入密碼: ')
        login()
    StuPass = input('請輸入身份證後4碼: ')
    StuSN = input('請輸入上課證學號: ')
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
        account = input('請輸入賬號: ')
        password = input('請輸入密碼: ')
        login()
    print('賬號: '+StuSN)
    print('密碼: '+StuPass)



while True:
    eula = input(termcolor.colored(bcolors.Y + '\n若繼續代表您已同意EULA\n是否繼續(Y/N): ' + bcolors.RESET, "yellow"))
    if eula=='N':
        break
    if eula=='n':
        break



    url_L1 = ('https://makeup.jlweb.com.tw/ClassList1.aspx?Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(url_L1) as response:
        data_L1 = response.read().decode('utf-8')
    urlStu = ('https://makeup.jlweb.com.tw/StuLogin.aspx?Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(urlStu) as response:
        dataStu = response.read().decode('utf-8')
        dataStu = dataStu.split(',')
    print('\n\n\n--------------------------------')
    print('查詢同學 【'+ dataStu[1] + '】 的課程\n')

    class_N = ['']
    classList = data_L1.split('<br/>')
    for i in range(0,(len(classList) - 1)):
        className = classList[i].split(',')
        #print(className)
        classNum = className[0]
        classTitle = className[1]
        classN = classNum.split(';')
        #print(classN[1] + ' | ' + classTitle)
        print(str(i+1) + ' | ' + classTitle)
        class_N.append(classN[1])
    print('--------------------------------\n\n')

    

    #ClassID = str(input('請輸入課程代碼: '))
    #print(class_N)
    sxkc = str(input('請選擇課程: '))
    ClassID = class_N[int(sxkc)]
    urls1 = ('https://makeup.jlweb.com.tw/ClassList2.aspx?ClassID=' + ClassID + '&Code=' + Code + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(urls1) as response:
        datas1 = response.read().decode('utf-8')
    #print(datas1)
    classList = datas1.split('<br/>')
    print('課程列表: \n')
    for i in range(0,(len(classList) - 1)):
        className = classList[i].split(',')
        if(className[3] == '6'):
            print(' ' + str(i+1).zfill(2) + ' | ' + bcolors.R + '[Offline] ' + bcolors.RESET + className[0])
        else:
            print(' ' + str(i+1).zfill(2) + ' | ' + bcolors.G + '[Online]  ' + bcolors.RESET + className[0])

    classC = input('\n請選擇課堂: ')
    classNum = classList[(int(classC) - 1)].split(',')
    MovieID = classNum[2]

    urls2 = ('https://makeup.jlweb.com.tw/MovieList.aspx?ClassID=' + ClassID + '&Code=' + Code + '&MovieID=' + MovieID + '&StuPass=' + StuPass + '&StuSN=' + StuSN)
    with req.urlopen(urls2) as response:
        datas2 = response.read().decode('utf-8')
    #print(datas2)
    movieList = datas2.split('<br/>')
    videoNum = len(movieList) - 1
    print('[本堂課 共' + str(videoNum) + '節]\n')

    path = os.path.join('Class')
    if(os.path.isdir(path) != True):
        os.mkdir(path)
    
    
    xzjc = int(input('請選擇節次(0=ALL): '))
    className = classList[int(classC) - 1].split(',')
    cN0 = re.sub('\/|\\|', ' ', className[0])
    #print(cN0)
    if(xzjc == 0):
        for i in range(0,videoNum):
            movieList_first = movieList[i].split(',')
            videoCode = movieList_first[1]
            urls3 = ('http://xzb2022.duckdns.org/LocalUser/L096/' + str(videoCode) + '.mp4')
            r = requests.head(urls3, allow_redirects=True)
            print('')
            #print(r.url)
            filepath = './Class/' + cN0 + '_' + str(i+1) + '.mp4'
            if os.path.isfile(filepath):
                print('[檔案已存在 結束下載]')
            else:
                print('正在下載 第' + str(i+1) + '節')
                save_as = os.path.join(path, cN0 + '_' + str(i+1) + '.mp4')
                start_time = time.time()
                wget.download(urls3, save_as)
                print("\n[下載完成] [" + str(round((time.time() - start_time), 2)) + "s]")
    else:
        movieList_first = movieList[xzjc-1].split(',')
        videoCode = movieList_first[1]
        urls3 = ('http://xzb2022.duckdns.org/LocalUser/L096/' + str(videoCode) + '.mp4')
        r = requests.head(urls3, allow_redirects=True)
        print('')
        #print(r.url)
        filepath = './Class/' + cN0 + '_' + str(xzjc) + '.mp4'
        if os.path.isfile(filepath):
            print('[檔案已存在 結束下載]')
        else:
            print('正在下載 第' + str(xzjc) + '節')
            save_as = os.path.join(path, cN0 + '_' + str(xzjc) + '.mp4')
            start_time = time.time()
            wget.download(urls3, save_as)
            print("\n[下載完成] [" + str(round((time.time() - start_time), 2)) + "s]")




