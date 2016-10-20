import sys

str =  input('Enter something: ')

n = 0

s = []

s = str.split(' ')

j = 0

while len(s) != 1:

    if s[j] in ['+','-','*','/']:

        if s[j] == '+':

            n = int(s[j-2]) + int(s[j-1])

        elif s[j] == '-':

            n = int(s[j-2]) - int(s[j-1])

        elif s[j] == '*':

            n = int(s[j-2]) * int(s[j-1])

        elif s[j] == '/':

            if s[j-1] != 0:

                n = int(s[j-2]) / int(s[j-1])

            else:

                print('ERROR')

                sys.exit(-1)

        s.pop(j-1)

        j = j - 1

        s.pop(j-1)

        j = j - 1

        s[j] = n

        n = 0

    j = j + 1

print(s[0])
