# Without Context Manager

f = open('hello.txt', 'w')

try:
    f.write('hello')
finally:
    f.close()


# With Context Manager

with open('hi.txt', 'w') as f:
    f.write('hi')
