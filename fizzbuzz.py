print('hello')

for i in range(1,16+1): #3의 배수
    if i % 15 == 0:
        print('fizzbuzz') #공배수 처리
    elif i%3==0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

print('fizzbuzz done!')
