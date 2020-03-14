#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import re
try:
    url='https://www.dcard.tw/f/all/p/233173121'
    html=requests.get(url)

    print(type(html))
    if html.status_code==requests.codes.ok:
        print("success",len(html.text))
        keyw=input("input the key word:")
        key=re.findall(keyw,html.text) #key is a list
        if key != None:
            print("there are %d same vocabulary" % len(key)) #看key的長度就知道有多少相符字詞
        else:
            print("there are no same vocabulary")
        
    else:
        print("fail")
    a='file.text'
    with open(a,'wb') as file_obj: 
        for store in html.iter_content(102400): #iter_content是把下載下來的檔案從response物件以102400位元組為單位存入磁碟
            size=file_obj.write(store) #每次都將寫入大小作紀錄
            print(size) #每次都印出
        print("成功") #迴圈結束後印出
except Exception as err:
    print("錯誤發生")

