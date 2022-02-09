
teste = int(input('entre com o numero: '))
tent = 0

while teste>1:
    num = teste
    while num!=1:
        tent += 1
        if (num % 2) == 0:
            print("{0} par x/2".format(num))
            num = num/2
        else:
            print("{0} impar 3x+1".format(num))
            num = (num*3)+1
    else:
        final = teste-5
        teste = teste-1
        print('1.0')
        print(f'vamos tentar {teste}')




print(num)
print(f'{tent} tentativas')