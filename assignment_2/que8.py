my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c=[]
for each in my_numbers:
    if(each%2==1):
        for eachs in my_numbers:
            if(each**2==eachs):
                c.append(each ** 2)


print(c)