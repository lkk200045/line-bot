########### Python 3.6 #############
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
}

params ={
    # Query parameter
    'q': '我愛你',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}
#輸入查詢句&語意分析
def user_input():
    text = []     
    while True:
        query = input("請輸入語句:")
        params['q'] = query
        if query == "":
            break
        else :
            r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
            result = r.json()
            a = result['topScoringIntent']['intent']
            print("意圖:"+ a)     
#寫入記事本
def write(text):
    with open('test.txt','w',encoding='utf-8') as file:
            for i in text:
                file.write(i[0] + ',' + i[1]  + '\n') 
#讀存取檔
def read(file):
    a = []
    with open(file,'r',encoding='utf-8') as f:
        for i in f:
            query,intent = i.strip().split(',')
            a.append([query,intent])
        print(a)
    #print(a)
#主程式
user_input()
read('test.txt')