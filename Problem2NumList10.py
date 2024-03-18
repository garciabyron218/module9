# Byron Garcia
# 3/17/24
# Program will loop a list appending the current value counter until
# the counter is greater than 10
# not sure if the assignment wanted the list to start with numbers 1-10 or none


L = []
counter = 0
while counter <= 10:
    L.append(counter)
    counter += 1

print(L)