c0 = int(input("Enter value of c0: "))
step = 0
while c0 != 1:
    step += 1
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3*c0+1
    print("step:", step, "c0:", c0)
    
