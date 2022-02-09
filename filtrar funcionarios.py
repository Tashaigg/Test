


#tem carro noite / tem carro dia / nao tem carro






funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista1 = tem_carro & turno_noite
lista2 = tem_carro & turno_dia
lista3 = funcionarios-tem_carro

print (lista1)
print (lista2)
print (lista3)
