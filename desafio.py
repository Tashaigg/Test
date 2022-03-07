lista = [3, 7, 10, 15]
lista2 = [12, 15, 20, 25]
lista3 = [5, 8, 10, 30]

for c in range(len(lista)):
 for d in range(len(lista2)):
  for e in range(len(lista3)):
      num = lista[c]*lista2[d]*lista3[e]
      print(f'c= {c}; d= {d}; e= {e}')
      print(lista[c])
      print(lista2[d])
      print(lista3[e])
      print(num)
