people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# 리스트의 모든 원소 조작(1)
def check_adult(person):
    if person['age'] >= 20:
        return '성인'
    else:
        return '청소년'
    # return ('성인' if person['age'] >= 20 else '청소년')     # 한줄로 표현

result = map(check_adult, people)
print(list(result))

# 리스트의 모든 원소 조작(2)_lambda
result = map(lambda person: ('성인' if person['age'] >= 20 else '청소년'), people)
print(list(result))