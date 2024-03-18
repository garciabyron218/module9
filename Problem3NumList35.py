# Byron Garcia
# 3/17/24
# Program will loop asking for a number, adding it to a list, once the list adds up to 100, loop will close


number = []
sum_total = 0

while sum_total <= 100:
    num = int(input("Input a number"))
    number.append(num)
    sum_total += num

print("Sum total", sum_total)
print("List of number input", number)