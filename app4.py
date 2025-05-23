# 간단하게 Epoch 시간데이터 다루기 

# 프로그래밍할 때 시간을 어디 적는 일이 많습니다. 
# 시간을 기록할 때 우리 인간이 보는 년월일 이런걸 사용하면 더하고 빼기 살짝 불편해서 
# Epoch 아니면 Unix 라고 부르는 시간형식이 있습니다. 그걸 가끔 사용합니다.
# 1970년 1월1일 부터 지금까지 몇초나 흘렀는지를 알려주는 시간 형식입니다. 

import time
print(time.time())
# 이렇게 쓰시면 1610175600 이런 식으로 시간이 출력됩니다. 일명 Epoch Time 입니다. 

A = time.time()
print(A)

# 처리시간이 오래 걸리는 코드 ~~~
100000 + 100000222222222222222222222

B = time.time()
print(B-A)




import time
시간 = time.time()
시간 = time.ctime(1610175600)
print(시간) # Sat Jan  9 16:00:00 2021
# Epoch 타임이 보기 싫으시면 인간이 읽을 수 있는 시간형식으로 변환하실 수 있습니다.  -> C타임으로 사용

# localtime() 함수는 현재 시간을 년월일 시분초로 바꿔줍니다.  세부항목만 출력하기기
import time
시간 = time.localtime()
print(시간)
print( '년 : ' + str(시간.tm_year) ) # 년    str() 함수는 문자열로 변환해줍니다. 
print( '월 : ' + str(시간.tm_mon) ) # 월
print( '일 : ' + str(시간.tm_mday) ) # 일
print( '시 : ' + str(시간.tm_hour) ) # 시
print( '분 : ' + str(시간.tm_min) ) # 분
print( '초 : ' + str(시간.tm_sec) ) # 초

# 아니면 애초에 이렇게 localtime() 쓰시면 뽑아쓰기 좋게 년월일, 시분초를 담아줍니다. 
# 오늘의 날짜, 시간 일부만 따로 출력할 일이 있으면 저렇게 년 월 일 뽑아쓰십시오. 
# Epoch 타임을 localtime() 안에 집어넣으면 년월일 시 분 초로 바꿔줍니다. 

# 시간형식을 조금 더 자유롭게 표기하고 싶으면 strftime() 함수를 가져다 쓰시면 됩니다. 
# 이건 두개의 파라미터를 입력가능한데 첫째 파라미터엔 어떤 식으로 표현해줄지 포맷팅문법을,
# 둘째파라미터는 localtime() 형식의 시간 (일명 struct_time object라고함) 을 집어넣으시면 됩니다. 

import time
시간 = time.localtime()
time.strftime('%Y년 %m월 %d일', 시간) # %Y년 %m월 %d일 => 포맷팅문법, 시간 = 로컬타임
print(시간.tm_year)
print(시간.tm_mon)
print(시간.tm_mday)

print('--------------------------------')
print(time.strftime('%Y년 %m월 %d일', 시간))


# %Y 년
# %m 월
# %d 일
# %H 시
# %M 분
# %S 초 를 사용하시면 됩니다. 


