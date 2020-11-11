print("=-" * 33)
print("Verifico quantos números ou letras iguais adjacentes há.")
print("=-" * 33)

num = input('Manda: ')


ax = 0
n = 1
encontros = 0

while not ax == len(num) - 1:
	if num[ax] == num[n]:
		encontros += 1
	ax += 1
	if not (len(num) - 1) == n:
		n += 1

print(f"Foi/Foram detectada (s) {encontros} ocorrência (s).")
