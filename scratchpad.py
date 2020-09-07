
fib= 10

a = 0
b = 1
c = 0
count = 0
while count < fib:
    if c <= 1:
    print(c)
    count = count + 1
    c = c + 1
  else:
    c = b + a
    a = b
    b = c
    print(c)