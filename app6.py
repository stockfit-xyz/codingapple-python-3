# 파이썬 멀티쓰레딩 1 : 수집할 페이지가 백만 개 있으면 어떻게 하죠?
# 멀티스레딩이란? 
# 멀티스레딩은 하나의 프로그램에서 여러 개의 스레드를 동시에 실행하는 것을 의미합니다.
# 스레드는 프로그램의 실행 흐름을 의미하며, 멀티스레딩은 이러한 스레드들을 동시에 실행하여 병렬 처리를 가능하게 합니다.
# 멀티스레딩은 여러 개의 스레드를 동시에 실행하여 병렬 처리를 가능하게 합니다.

# 이번 강의에서 수집해볼 URL 들 입니다.
# 물론 반복문 쓰면 더 짧을 텐데 무서워하는 분들이 있으므로 하드코딩버전으로 준비했습니다. 복붙하고 시작합시다. 

url = [
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000'
]

# 반복문으로 쓰면 다음과 같습니다.
# url = []
# base_url = 'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time='

# # 10개의 URL 생성
# for i in range(10):
#     # 마지막 시간을 7일씩 감소시키면서 URL 생성
#     last_time = 1609524000000 - (i * 7 * 24 * 60 * 60 * 1000)  # 7일 * 24시간 * 60분 * 60초 * 1000밀리초
#     url.append(base_url + str(last_time))

# 그리고 이 URL들에 GET 요청을 하면 JSON 데이터가 오는데 이걸 간단하게 하나만 출력하는 크롤러를 만들어봅시다. 
# 실은 저번시간에 JSON 어쩌구 다룰 때 만들어뒀던 크롤러 코드 그대로 쓰시면 됩니다. 근데 함수로 싸매서 쓸겁니다. 

import requests
import json
import time

# def 함수(구멍):
#     data = requests.get('가져올 url')
#     딕셔너리 = json.loads(data.content)
#     print(딕셔너리['data'][0]['Close'])
# 또는     return 딕셔너리['data'][0]['Close']

def 함수(파라미터):
    data = requests.get(파라미터)
    딕셔너리 = json.loads(data.content)
    return 딕셔너리['data'][0]['Close'] # 그 중에서 첫번째 가격만 가져오겠습니다. 

함수(url[0])  # 이렇게 하면 첫번째 URL의 첫번째 가격이 나옵니다. 
함수(url[1])  # 이렇게 하면 두번째 URL의 첫번째 가격이 나옵니다.  쭉쭉

# 이런 걸 가지고 multi-threading : CPU 병렬처리 / muti-processing : 여러 개 파이썬 프로세스 동시 실행(실행창 띄우기)
# local 파이썬 프로세스 하나 띄우고 여러개 쓰레드 동시 실행하는 거 가능합니다.
# 예를 들어 100만개의 URL을 수집하려면 100만개의 파이썬 프로세스를 띄워서 동시에 수집하면 됩니다.
# 근데 그러면 메모리 부족해질 것 같아요? 그래서 멀티프로세싱을 쓰는 겁니다. 
# 멀티프로세싱은 파이썬 프로세스를 여러개 띄워서 동시에 작업을 시키는 겁니다. 
# lock을 걸어서  기다리기 때문에 병목현상이 방지된다.

# 멀티프로세싱의 장점
# 병렬 처리: 여러 프로세스가 동시에 작업을 수행
# CPU 자원 활용: 여러 CPU 코어를 동시에 사용
# 병목현상 감소: 작업을 여러 프로세스로 분산시켜 처리 시간 단축
# 예시로 설명
# 단일 프로세스: 100만개 URL 처리 시 27시간 소요
# 멀티프로세싱: 4개의 프로세스로 나누면 약 7시간으로 단축
# 병목현상이 발생하는 경우
# Lock 사용 시: 여러 프로세스가 같은 자원을 공유할 때 Lock을 사용하면 병목현상 발생
# I/O 작업: 디스크 읽기/쓰기, 네트워크 요청 등이 많을 때


# 이제 앞으로 함수('URL어쩌구') 이렇게 사용하면 이 자리에 데이터가 뾰로롱 남습니다. 
# 아주 멋진 크롤러입니다. 

# 근데 수집할 URL이 좀 많네요 
# 위에서 작성한 10몇개의 URL을 전부 수집하려면 코드 어떻게 짜야하죠?
# 함수에다가 0번째 URL, 1번째 URL ... 전부 한번씩 집어넣으면 끝이죠? 

# 함수( url[0] )
# 함수( url[1] )
# 함수( url[2] )
# ... 이렇게 계속 하시면 됩니다. 반복문 필요하면 쓰면 되고요.

# 근데 문제는 처리 시간입니다. 
# URL 하나 수집하는데 0.1초걸린다고 가정하면 100만개 수집하려면 몇초인가요? 
# 10만초 걸립니다. 27시간이네요 ㄷㄷ

# 해결책은 멀티프로세싱/멀티쓰레딩을 이용하시면 됩니다. 
# 파이썬 실행창 프로세스를 여러개 띄우는 멀티프로세싱을 쓰시던가 
# 여러분 PC에 내장된 CPU 쓰레드 여러개로 작업을 나눠서 시키든가 하시면 됩니다. 


#--------------------------------

# 멀티쓰레딩/프로세싱 쉽게 하는 법 
# 원래 class 문법 기반으로 Producer/Consumer 어쩌구를 만들어 쓰는 게 기본인데 
# 그것보다 훨씬 쉽게 "컴퓨터야 그냥 니가 알아서 멀티쓰레딩 해와라"는 식의 방법이 하나가 있습니다. 
# multiprocessing.Pool.map 이라는 함수입니다. 써봅시다. 

from multiprocessing.dummy import Pool as ThreadPool

# pool = ThreadPool(4)
# pool.map(작업시킬함수, 작업시킬리스트)
# pool.close()
# pool.join()


# 잠깐 map 함수 사용법을 알아봅시다

리스트 = [2,3,4,5,6]
# 이런 리스트가 있습니다. 이 안의 모든 자료에 1씩 더한 새로운 리스트를 만들고 싶으면 코드를 어떻게 짤까요?
# 가장 쉽고 직관적인건
#     - 리스트[0]에 1더해주셈 그걸 새로운 리스트에 추가
#     - 리스트[1]에 1더해주셈 그걸 새로운 리스트에 추가
#     ..

# 이렇게 하드코딩하거나 반복문을 사용하는 겁니다. 
새로운리스트 = []
for i in 리스트:
    새로운리스트.append(i + 1)
print(새로운리스트)


# 이게 싫으면 기본 내장 함수인 map을 사용하십시오. 
def 더해주셈(x): # 뭔가 집어넣으면 1을 더해서 퉤 뱉어주는 함수 만들고   
    return x + 1
result = map(더해주셈, 리스트) # 그걸 리스트자료와 함께 map에 집어넣으면 됩니다. 
print(list(result)) # 그럼 그 함수를 리스트 안에 있던 모든 자료에 전부 적용해줍니다. 리스트로 변호ㅓㅏㄴ
 
# map(함수넣으셈, 리스트넣으셈)
# map 함수는 내가만든 함수와 리스트자료를 입력할 수 있습니다. (파라미터 두개입력가능)
# 그러면 리스트 안에 있던 모든 자료에 함수를 적용시켜줍니다. 
# 끝입니다.  

# 그래서 모든 리스트자료에 1을 더한다는 아까의 기능을 만들고 싶으면 
# step 1. 뭔가 집어넣으면 1을 더해서 퉤 뱉어주는 함수 만들고
# step 2. 그걸 리스트자료와 함께 map에 집어넣으면 됩니다. 
# 그럼 그 함수를 리스트 안에 있던 모든 자료에 전부 적용해줍니다. 

리스트 = [2,3,4,5,6]
def 더해주셈(x):
  return x + 1

result = map(더해주셈, 리스트)
print(result)

# 그래서 방금 말한 1번과 2번을 개발해본겁니다. 
# 그럼 아까와 똑같은 1더해주는 기능을 약간 더 쉽게 짤 수 있습니다. 
# 어색하고 거부감이 드는 이유는 아직 안외웠기 때문입니다.
# 이것 역시 암기의 영역이니 map을 어떻게 쓰는지 빨간 글씨와 step 1, 2번을 외워두도록 합시다.  

# 다시 멀티쓰레딩 코드로 돌아옵시다. 
pool = ThreadPool(4)
pool.map(함수, url)
pool.close()
pool.join()

# pool.map 함수도 똑같은데 멀티쓰레딩으로 처리해줍니다. 
# 멀티쓰레딩 라이브러리에 있는 map 함수 사용법도 아까랑 똑같은데
# 다만 이 map 함수는 멀티쓰레딩식으로 분산처리를 지가 알아서 해준다는 소리입니다. 
# 그니까 map 함수에 데이터 100만개 들어있는 리스트 자료를 넣으시면 
# 데이터 100만개를 프로세스/쓰레드가 각각 몇개씩 나눠가진 다음 분산처리 해준다는 겁니다.  
# 그럼 처리시간이 적게 걸리겠죠? 그래서 사용합니다. 

# 그래서 코드를 이렇게 짰습니다. 

from multiprocessing.dummy import Pool as ThreadPool

def 함수(구멍):
  data = requests.get(구멍)
  딕셔너리 = json.loads(data.content)
  return 딕셔너리['data'][0]['Close']

pool = ThreadPool(4)
result = pool.map(함수, url) # 함수 넣고, 작업시킬 리스트인 url 리스트 넣고
pool.close()
pool.join()

print('------------구분선--------------------')
print(result) # 출력 한 번 해보기
 

# 프로세스/쓰레드를 4개 쓴다고 써놔서 4분의1 시간이 걸린다고 예상할 수 있겠지만 
# 그것은 이론상일 뿐이고 
# 일단 이 예제는 그냥 실행할 때 보다 절반 이하의 시간으로 모든 URL 수집을 처리할 수 있습니다. 

# 실전에서는 
    # - 수집 필요한 모든 URL을 리스트[ ] 자료에 담아두신 다음 
    # - URL을 입력하면 수집 결과를 퉤 뱉어주는 크롤러함수를 만들어두고 
    # - 그거 두개를 동시에 멀티쓰레딩 map 함수에 집어넣으면 되겠네요. 

 


# 4줄 컷입니다. 
# 기본 내장라이브러리를 저렇게 import 해오시고 (멀티쓰레딩하는 법인데 멀티프로세싱을 하려면 .dummy를 제거합니다)
# ThreadPool() 에다가 몇개의 프로세스/쓰레드로 동시에 작업을 시킬지 숫자로 적으시고
# map 에다가는 저거 적으시면 됩니다. 끝! 

# 그 다음에 마무리되면 close() join() 을 차례로 해주면 됩니다. (작업 고만시키고 작업한거 join 그니까 전부 가져오라는 뜻입니다.)
# 그럼 map()에서 리스트안에 있던 자료들을 전부 함수에 차례로 집어넣어주는데 그 집어넣은 결과를 리스트로 만들어줍니다. 
# 근데 그냥 해주진 않고 멀티쓰레딩을 이용해서 분산처리를 지가 알아서 해준다는 겁니다. 
# 하지만 빨간게 뭔 뜻인지 모르겠으니 다음시간에 map 함수를 알아봅시다.