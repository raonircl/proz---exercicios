# estrutura de repetição for 
for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)

#while
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1

# com lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  

for i in lista:
    if i != 13:
        print(i)
