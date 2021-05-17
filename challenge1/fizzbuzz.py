#! usr/bin/env python3

def fiz_buzz():
    for i in range(1,101):
        if (i%3==0 and i%5==0):
            print("FizzBuzz")
            continue
        if (i%3==0):
            print ("Fizz")
            continue
        if (i%5==0):
            print ("Buzz")
            continue
        print (i)
def main():
    fiz_buzz()
main()

