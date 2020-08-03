# 이름이 a,b,c,d 인 네사람의 나이 및 국어,영어,수학점수가 포함된 리스트를작성
a = {'age':30, 'kor':80, 'eng':70, 'math':90}
b = {'age':28, 'kor':90, 'eng':50, 'math':84}
c = {'age':26, 'kor':87, 'eng':68, 'math':70}
d = {'age':31, 'kor':78, 'eng':80, 'math':60}
# 1. c의 총점과 평균
cSum = c['kor']+c['eng']+c['math']
cAvg = cSum / 3
print(cSum)
print(cAvg)
# 2. 모두의 나이의 합계
age_sum = a['age']+b['age']+c['age']+d['age']
print(age_sum)
# 3. 모든 점수 중 가장 낮은 점수는 몇점인지 구하시오.
