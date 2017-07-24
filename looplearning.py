languages = ['C','C++','Perl','Python']
for x in languages:
    print(x)

for i in range(5,9):
    print(i)

a = ['google', 'baidu', 'taobao', 'facebook']
for i in range(len(a)):
    print(i, a[i])

for letter in 'lichenhgao':
    if letter == 'h':
        continue
    print('the letter is:', letter)

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print("the var is:", var)
print("good bye!")


for n in range(2,200):
    for x in range(2,n):
        if n % x == 0:
            #Sprint(n, '\=', x, '*', n//x)
            break
    else:
        print(n,"是质数")