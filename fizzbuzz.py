print('hello')

for i in range(1,16+1): #3의 배수
    if i%3==0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
