# 주석
# js: console.log('test;)

print('test')

# let const 없음 / 파이썬은 변수 타입이 없음. >> 원래 안뎀
number = 1
float_number = 1.1  # js 에서는 일반적으로 floatNumber (개발자 언어 관련임. 케바케)
string = '문자열'
boolean = True  # js 에서는 true

# list, dict 거의 똑같음
number_list = [1, 2, 3, 4]
print(number_list[0])  # 1

string_dict = {'name': 'kim', 'age': 30}
print(string_dict['name'])  # kim

# 들여쓰기가 아주 중요함
if number > 10:
    print('10보다 큼')
else:
    print('10보다 작음')

print('상관 x')

for num in number_list:
    print(num)


# 함수
def func(num):
    print(num)


def sum(num1, num2):
    result = num1 + num2
    return result


print(sum(10, 20))

# 과일 갯수 세기.
fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
count = 0
for fruit in fruits:
    if fruit == '사과':
        count = count + 1
print(count)
