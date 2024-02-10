
def prime_finder(n):
    prime_nos = []
    if n == 1:
        return prime_nos
    prime_nos = [2]
    if n == 2:
        return prime_nos
    
    for x in range(3,n+1):
        for y in prime_nos:
            if x/y != 1 and x%y == 0:
                break
        else:
            prime_nos.append(x)
    return prime_nos

#print(prime_finder(11))

#print(prime_finder(431))