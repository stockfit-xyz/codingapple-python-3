import json
import requests

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')

딕셔너리 = json.loads(data.content)
print(딕셔너리['data'][1]['Close']) # 두번째 딕셔너리 안에 있는 Close 값만 출력

# 반복문으로 전체 200개 다 뽑아보기
for i in range(len(딕셔너리['data'])):
    print(딕셔너리['data'][i]['DT'])
    print(딕셔너리['data'][i]['Close'])

# JSON 파일에서 DT는 일명 epoch/UNIX 시간이라고 부릅니다. 
# 이것은 1970년 1월 1일 00:00:00 UTC+0 이후의 경과 시간을 나타냅니다. 
# 이것을 우리가 알아볼 수 있는 날짜로 바꾸려면 이렇게 합니다. 
# 여기서의 앞 10자리, 뒤 3자리는 밀리세컨드입니다. 이 단위로 표현하고 싶을 때 씀.
# 이것은 1/1000초를 나타냅니다. 

# 먼저 날짜를 뽑아오고
import datetime
print(딕셔너리['data'][0]['DT'])

# 이걸 우리가 알아볼 수 있는 날짜로 바꾸려면 이렇게 합니다. 
dt = 딕셔너리['data'][0]['DT'] / 1000  # 밀리초 → 초
print(datetime.datetime.fromtimestamp(dt))

#또는 import time 을 써서 이렇게 해도 됩니다. 
import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['data'][0]['DT'] / 1000)))
# 딕셔너리['data'][0]['DT']는 1747256400000/1000 이것과 같음
# 이렇게 하면 우리가 알아볼 수 있는 날짜로 바꿀 수 있습니다. 



