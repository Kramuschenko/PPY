str = input("Wprowadz liczby, rozdzielone prazycinkami: \n")
numbers_str = str.split(",")
numbers = []
for n in numbers_str:
    numbers.append(float(n))

min = numbers[0]
max = numbers[0]
for num in numbers:
    if min > num:
        min = num
    if max < num:
        max = num

print('Min value: ', min)
print('Max value: ', max)
