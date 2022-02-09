
temp = int(input('entre a temperatura: '))



if temp < 48:
    print(f'carne crua')
elif temp < 54:
    print(f'carne mal')
elif temp<60:
    print(f'carne otima')
elif temp<65:
    print(f'carne media')
elif temp<71:
    print(f'carne bem passada')
elif temp>71:
    print('carne queimada')
