# 딕셔너리 생성, 출력
person = {'name': 'rara', 'age': 20}
print(person['name'])


# 딕셔너리 데이터 추가
person = {'name': 'rara', 'age': 20}

person['name'] = 'Jenny'
print(person)

person['height'] = 160
print(person)

person = {"name":"Alice", "age": 16, "scores": {"math": 81, "science": 92, "Korean": 84}}
print(person["scores"])
print(person["scores"]["science"])  #92


# 딕셔너리 키 포함 여부 확인
person = {'name': 'rara', 'age': 20}

print('name' in person)       #True
print('emain' in person)      #False
print('phone' not in person)  #True


# 리스트와 딕셔너리 조합
people = [{'name': 'rara', 'age': 20}, {'name': 'Jenny', 'age': 40}]
print(people[0]['name'])
print(people[1]['name'])

person = {'name': 'john', 'age': 7}
people.append(person)

print(people)    #person이 추가된 결과 출력
print(people[2]['name'])
