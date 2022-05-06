## Actividad 1:
import pdb
pdb.set_trace()

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

r =[max(i) for i in lista]
print (r)



## Actividad 2:

lista_2 = [3, 4, 8, 5, 5, 22, 13]
def es_primo(num):
    for n in range(2,num):
        if num% n == 0:
            return False
    return True


resultado_2 = list(filter(es_primo,lista_2))
print (resultado_2)
