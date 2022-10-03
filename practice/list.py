# 리스트 생성
a = [1, 5, 2]
b = [3, "a", 6, 1]
c = [1, 2, 4, [3, 5]]

# 리스트 길이 확인
a = [1, 5, 2]
print(len(a))

b = [1, 3, [2, 0], 1]
print(len(b))


# 리스트 인덱싱
a = [1, 3, 2, 4]
print(a[3])
print(a[:2])   # 2번 인덱스 앞까지만 포함
print(a[1:])   # 1번 인덱스부터 포함
print(a[1:3])
print(a[-1])


# 리스트 중첩
a = [1, 2, [2, 3], 0]
print(a[2])
print(a[2][0])


# 덧붙이기
a = [1, 2, 3]
a.append(5)
print(a)

a.append([1, 2])
print(a)

a += [2, 7]
print(a)     # [1, 2, 3, 5, [1, 2], 2, 7]


# 리스트 정렬
a = [2, 5, 3]
a.sort()
print(a)

a.sort(reverse=True)
print(a)


# 리스트 포함여부 확인
a = [2, 1, 4, "2", 6]
print(1 in a)       #True
print("1" in a)     #False
print(0 not in a)   #True

