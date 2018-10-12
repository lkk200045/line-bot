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
#讀存取檔
def read(text):
    a = []
    with open(text,'r',encoding='utf-8') as f:
        for i in f:
            a.append(i.strip())
    print(a)
    return a
#寫入記事本



def work(message):
    if '找工作' in message:
        s = '請輸入時間'
        return s
    elif message == '時':
        s = '請選擇地點'
        return s
    elif message == '中山大學':
        s = '請選擇工資'
        return s
    elif message =='你好':
        s = '你好'
        return s

def luis():
    text = []
    while True:
        query = input("請輸入語句:")
        params['q'] = query
        if query == "":
            break
        else :
            text.append(query)                         
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
        result = r.json()
        a = result['topScoringIntent']['intent']
        print(a)
        if '找工作' or '時' or '中山大學' in query:
            s = work(query)
        else:
            if a == '告白':
                s = '告白'
        print(s)
luis() 