# total of list values

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(total)

# coordinates

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# x's and list - F

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# example of list activity

names = ['krzyś', 'miś', 'zdziś']
print(names[1]) # druga na liście
print(names[-1]) # ostatnia
print(names[1:]) # wszystkie elementy od 1 do końca

names[0] = 'Krzysiek' # aktualizuje listę pod wskazanym indexem
print(names)


# największa wartość

numbers = [2, 3, 4, 5, 6, 7, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)