#문제 1번 : 글자 출력하기

print('makit "code" lab')
print("she's gone")

#문제 2번 : 숫자 저장하기

a=10
b=20
print('a의 값은', a)
print('b의 값은', b)
print('a와 b의 합은', a+b)

#문제 3번 : ‘makit’ 곱하기 3

a = 10
b = 'makit'
print(a * 3)
print(b * 3)

#문제 4번 : 하나 빼기, 하나 더하기 연산자

m = 1
print(m)
m = m + 1
print(m)
m += 1
print(m)
m = m - 1
print(m)
m -= 1
print(m)

#문제 5번 : 몫 연산자(//)와 나머지 연산자(%)

a = 30//8
b = 30%8
c = 30/8
print('30을 8로 나눈 몫은', a)
print('30을 8로 나눈 나머지는', b)
print('30을 8로 나눈 결과는', c)

#문제 6번 : 문자열과 문자열 붙이기

print(12 + 34) # 숫자끼리 더하기
print('12' + '34') # 문자열 붙이기, 연결하기
print(2 ** 3) # 2의 3제곱

#문제 7번 : 한 줄 띄기

a = '시은 우진'
a = '시은 우진 화이팅!!'
print(a)
print( )
print(a)

#문제 8번 : 입력받아 컴퓨터랑 대화하기

name = input('이름이 무엇인가요? ' ,)
age = int(input('몇 살인가요? ', ))
print(name, '님은 내년에는' , age+1 , '살이 됩니다.')

#문제 9번 : 두 수를 입력받아 합과 평균 구하기

a = int(input())
b = float(input())
print('a와 b의 합은', a+b)
print('a와 b의 평균값은', (a+b)/2)

#문제 10번 : 문자열에서 하나의 문자 뽑아내기

makit='Sieun Woojin!'
result = makit[0]

print(result)
result = makit[6]

print(result)
result = makit[12]
print(result)

#문제 11번 : 문자열에서 여러 문자 뽑아내기

makit = 'Sieun Woojin!'
result = makit[2:9]
print(result)
result = makit[0:5]
print(result)
result = makit[6:]
print(result)

#문제 12번 : 동쪽을 찾아라

makit = '동서남북동서남북동서남북'
print(makit[::4])

#문제 13번 : 문자열 뒤집기

makit = '동서남북'
print(makit[::-1])

#문제 14번 : 문자열 바꾸기

phone = '010-1234-5678'
new_phone = phone.replace('-' , '.')
print(new_phone)

#문제 15번 : 참과 거짓

a = 10
b = 20
print(a < b)
print(a > b)
print(7 > 8)
print(7 < 8)
print(1 <= 1)
print(1 >= 2)
print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 != 2)

#문제 16번 : and, or 그리고 not 연산자

a = 20
b = 30
print(a > 40 and b > 40)
print(a > 20 and b > 20)
print(a < 30 and b > 30)
print(a > 10 and b > 10)
print(20 > 40 or 30 > 40)
print(20 > 20 or 30 > 20)
print(20 < 30 or 30 > 30)
print(20 > 10 or 20 > 10)
print(a != b)
print(not(a != b))

#문제 17번 : 1234초는 몇 분, 몇 초일까

n = int(input('초를 입력하세요:', ))
print(n, '초(sec)는', n//60, '분(min)', n%60, '초(sec)입니다.')

#문제 18번 : 7512분은 며칠, 몇 시간, 몇 분일까

n = int(input('분을 입력하세요:', ))
day = n//(60*24)
hour = (n//(60*24))%60
minute = n%60
print(n, '분은', n//(60*24), '일', (n-(day*(60*24)))//60, '시간', n%60,'분입니다.')

#문제 19번 : 기차처럼 만드는 리스트 자료 저장

a = ['메이킷','우진','시은']
print(a)
print(a[0])
print(a[1])
print(a[2])

#문제 20번 : 리스트 순서를 정하는 인덱스 알아보기

a = ['메이킷','우진','제임스','시은']
print(a[0:2])
print(a[1:])
print(a[2:])
print(a[:])

#문제 21번 : 리스트 추가, 삭제하기

a = ['우진','시은']
a.append('메이킷') # 리스트에 마지막 자료 추가하기
print(a)
a.remove('메이킷') # 리스트의 마지막 자료 삭제하기
print(a)

#문제 22번 : 리스트 원하는 위치에 삽입하기

a = ['우진','시은','메이킷']
a.insert(1,'하워드')
print(a)

#문제 23번 : 리스트 합치기

a = ['우진', '시은']
b = ['메이킷', '소피아', '하워드']
a.extend(b)
print(a)
print(b)

#문제 24번 : 공백 리스트와 합치기

a = ['우진','시은']
b = ['메이킷','소피아','하워드']
c = []
c.extend(a)
print(c) # ['우진','시은'] 출력
c.extend(b)
print(c) # ['우진','시은','메이킷','소피아','하워드'] 출력

#문제 25번 : 리스트의 개수인 길이 구하기

a = [3, 7, 4, 5, 6, 8]
print('리스트 a의 개수 즉 길이는', len(a) )
print('리스트 a의 숫자들의 평균은', sum(a)/len(a) )

#문제 26번 : 리스트 잘라내기(슬라이싱)

a = [1,2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

b = a[:5]
print('b :',b)

c = a[5:]
print('c :',c)

d = a[4:6]
print('d :',d)

e = a[::2]
print('e :',e)

f = a[1::2]
print('f :',f)

#문제 27번 : 리스트 거꾸로 잘라내기

a = ['형우', '윤진', '시은', '우진']
b = a[::-1]# -1 인덱스 부터 -4 인덱스까지 슬라이싱
print(b)

#문제 28번 : 리스트 안에 리스트

a = [['메이킷', 95], ['우진', 100], ['시은', 98]]
print(a[0][0] ,'학생의 시험 점수는', a[0][1])
print(a[1][0] ,'학생의 시험 점수는',a[1][1] )
print(a[2][0] ,'학생의 시험 점수는',a[2][1])

#문제 29번 : 리스트 안에 있는 문자로 하나의 문자열 만들기(join)

a = ['시은', '우진', '지훈', '지연']
b = ' '.join(a)
print(b)

#문제 30번 : 문자열 분리해 리스트 만들기(split)


#문제 31번 : 여러 개의 값 입력받기
#문제 32번 : 
#문제 33번 : 
#문제 34번 : 
#문제 35번 : 
#문제 36번 : 
