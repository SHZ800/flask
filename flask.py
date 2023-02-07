e = []
x = int(input("Input Number:"))
if x >1:
    for i in range(2, x+1):
        if x % (i) ==0:
            e.append(i)
             if len (e)++