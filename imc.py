

peso = float(input('entre com peso: '))
altura = float(input('entre com altura: '))


imc = peso / (altura/100)**2


if imc < 18.5:
    print(f'IMC = {imc}, Magreza')
elif imc < 25:
    print(f'IMC = {imc}, Normal')
elif imc < 30:
    print(f'IMC = {imc}, Sobrepeso')
elif imc < 40:
    print(f'IMC = {imc}, Obesidade')
elif imc > 40:
    print(f'IMC = {imc}, Obesidade Grave')


input('pressione enter para sair')
