num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# Q1. 짝수 출력하기
for num in num_list:
    if num % 2 == 0:
        print(num)

# Q2. 짝수의 개수 출력하기
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1

print(count)


# Q3. 모든 숫자 더하기
sum = 0
for num in num_list:
    sum += num
    
print(sum)


# Q4. 가장 큰 숫자 구하기
max_num = 0
for num in num_list:
    if num >= max_num:
        max_num = num
        
print(max_num)
print(max(num_list))   # max()를 사용하면 간단하다


# Q5. 주민번호를 입력받아 성별을 출력하는 함수 만들기
def check_gender(pin):
    gender = int(pin.split('-')[1][0])
    if gender == 1 or gender == 3:
        print('남성')
    elif gender ==2 or gender == 4:
        print('여성')
    else:
        print ('잘못 입력하셨습니다.')

my_pin = '2000101-4012345'
check_gender(my_pin)


# Q6. A가 들은 수업 중, B가 듣지 않은 수업 찾기
student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)
print(a_set - b_set)