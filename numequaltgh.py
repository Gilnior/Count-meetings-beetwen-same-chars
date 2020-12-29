print("=-" * 33)
print("Verify how many times the same chars meet.")
print("=-" * 33)

num = input('Send: ')

ax = 0
n = 1
meetings = 0

while not ax == len(num) - 1:
	if num[ax] == num[n]:
		meetings += 1
	ax += 1
	if not (len(num) - 1) == n:
		n += 1

print(f"There are {meetings} meeting (s).")
