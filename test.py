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
        query = input("請輸入語句:")
        params['q'] = query
        if query == "我要找工作":
            a ='我要找工作'
        else :
            r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
            result = r.json()
            a = result['topScoringIntent']['intent']
        return a     
#主程式
if __name__ == "__main__":
    a =user_input()
    if a =='告白':
        print('我愛你')
    elif a=='詢問':
        print('詢問')
    elif a=='我要找工作':
        print('我要找工作')