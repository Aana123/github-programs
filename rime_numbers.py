n=100

if (n <= 0):
    print (n," is not a prime no.")
else :
    # Write your for loop here!
    # Wriye a for loop to iterate from 23 to n-1 simply printing ech number first!
    for x in range(2,n):
        print(x)
        # Write a check if n is divisible by x then print not prime and break the loop
        if (n%x == 0):
            print(n,"is not a prime")
            break
        # Step counter is 2 !!!!!!/
    # write a else 
    else :
        print(n,"is a prime no.")
