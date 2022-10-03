#함수 만들기
def hello():
    print('안녕!')
    print('반가워요!')
    
hello()


#조건문을 포함하는 함수
def bus_rate(age):
    if age > 65:
        print('무료입니다!')
    elif age >= 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')
        
bus_rate(20)


#결과 값을 return하는 함수
def bus_fee(age):
    if age > 65:
        return 0
    elif age >= 20:
        return 1200
    else:
        return 600
    
money = bus_fee(19)
print(money)
