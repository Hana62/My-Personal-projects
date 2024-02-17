#multiplication table without numpy
n=20
for i in range (1,n+1):
    for j in range(1,n+1):
        print(f"{i*j}",end="\t")
    print("\033[91m")




