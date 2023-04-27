import random
att=int(input("enter the number of attempt: "))
a=random.randint(1,100)
while att>0:
    n=int(input("enter the number: "))
    if n<a:
        c=a-n
        print("your guessed number is:",n)
        print("you are failed")
    elif n>a:
        c=n-a
        print("your guessed number is:",n)
        print("you are failed")
    elif n==a:
        print("you are passed")
        print("your guessed number is correct")
    else:
        print("your guessed number is not acceptable ")

    att-=1
print("correct number is",a)
