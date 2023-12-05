#!/usr/bin/python3
for i in range(89):
    if ((i%10) is not (i-i%10)) and i%10 > (i-i%10):
        print('{:02d}, '.format(i), end='')
print('89')
