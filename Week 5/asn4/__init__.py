a = 0
b = 0
c = 0
j = 0
while j < 4:
    i = int(input())

    if i > 0:
        a = a + 1

    if i == 0:
        b = b + 1
    if i < 1:
        c = c + 1
    j = j + 1

if a > b and a > c or a < b :
    print('positive')
if b > a or b > c:
    print('tie')
if c > a and c > b and c < b and c < a:
    print('negative')