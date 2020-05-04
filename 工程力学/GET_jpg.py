#-*- codeing = utf-8 -*-
#@Author: Angious
#@Time : 2020/5/4 10:21
#@File : GET_jpg.py
#@Software : PyCharm

import requests

url1 = 'http://app.readoor.cn/app/bv/getBookInfo?b_id=81377&level=1&sign=ODEzNzcs' \
      'NzE1MzQzMSwxNTg4NTU3OTE0LDlmZTk3ODBlMjY1ZDBkNGFhN2MzY2IzZWMxYTIxYzI4&appid=1535595605'

url2 = 'http://data2.readoor.cn/files/5904365ab9f997/pdf/5357245e49184e/3/'
resp = requests.get(url1).json()
resp = resp['page_list_h']
print(resp)

#print(len(resp))
path = 'D:\Code\PDFbooks\jpg\\'

def save_file(path, file_name, data):
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()
    file.close()


for i in range(0,len(resp)):
    s = str(resp[i])
    geturl = url2 + s
    file_name = str(i)+'.jpg'
    data = requests.get(geturl).content
    save_file(path, file_name, data)






