# Byron Garcia
# 3/17/24
# Created loop that starts counter at 0, will run into it reaches 50
# if value of counter is divisible by 10, append value to list called tens


tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Numbers divided by 10", tens)