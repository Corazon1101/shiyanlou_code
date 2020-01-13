#!/usr/bin/env python3
sticks = 21

print('There are 21 sticks. You can take 1-4 number of sticks at a time')
print('Whoever will take the last one will loose')

while True:
    print('Sticks left: ', sticks)
    usr_pick = int(input('Take sticks(1-4): '))
    if sticks == 1:
        print('you picked the last one, you loose')
        break
    if usr_pick > 5 or usr_pick <= 0:
        print('Wrong choice')
        continue
    print("Computer took: ", (5 - usr_pick), "\n")
    sticks -= 5
