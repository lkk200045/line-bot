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
def luis():
    text = []
    while True:
        query = input("請輸入語句:")
        params['q'] = query
        if query == "":
            break
        else :
            text.append(query) 
        with open('test.txt','w',encoding='utf-8') as file:
            for i in text:
                file.write(i+ '\n')                        
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
        result = r.json()
        a = result['topScoringIntent']['intent']
        if a == '告白':
            print('謝謝我不愛妳')
        read('test.txt')
luis()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################