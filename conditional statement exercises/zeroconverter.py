# You are given a number n. The number n can be negative or positive.
# If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
# If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
# Note:- You don't have to return anything, you just have to print the array.

def neg_pos():
    num = int(input("enter a value"))
    if num<0:
        while num<=0:
            print(num)
            num =num +1
    elif num>0:
        while num>=0:
            print(num)
            num= num-1
    else:
        print("num is zero")

neg_pos()
