num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# Q1
for num in num_list:
    if num % 2 == 0:
        print(num)
        
print('===== 구분선 =====')

# Q2
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1

print(count)

print('===== 구분선 =====')

# Q3
total = 0
for num in num_list:
    total += num
print(total)

print('===== 구분선 =====')

# Q4
max_num = 0
for num in num_list:
    if num >= max_num:
        max_num = num
print(max_num)