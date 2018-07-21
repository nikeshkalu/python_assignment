def sumNumber(*args):
    sum=0
    for each in args:
        sum+=each

    return sum


print("Sum is ",sumNumber(1,2,3,4,5,4))
print("Sum is",sumNumber(1,2,3,4,5,4,10,5,6,7,8,9,))
