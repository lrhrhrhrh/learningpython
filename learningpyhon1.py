
age = int(input("请输入你家狗狗的年龄："))
print("")

if age < 0:
    print("Are you kidding!")
elif age == 1:
    print("as a 14-year-old person")
elif age == 2:
    print("as a 22-year-old person")
elif age > 2:
    human = 22 + (age - 2)*5
    print("对应人类的年龄：", human)

### hint to exit
input("click \'enter\' to exit")

# this is a game about guessing number
number = 7
guess = -1
print("Gussing number game")
while guess != number:
    guess = int(input("Pleasr type your number:"))
    if guess == number:
        print("Conglatulations to you.")
    elif guess < number:
        print("less...")
    elif guess > number:
        print("more...")