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