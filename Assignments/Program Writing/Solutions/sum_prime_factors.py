import prime_finder

def sum_prime(n):
    prime_lst = prime_finder.prime_finder(n)
    factors = []
    for i in prime_lst[:len(prime_lst)//2]:
        if n%i == 0 and i in prime_lst:
            factors.append(i)
    print(factors)
    return sum(factors)


print(sum_prime(10005))

# Solution 2

def sum_of_prime_factors(n):
  # Write your code here
  prime_lst = [2]
  for x in range(3,n+1):
    for y in prime_lst:
        if x/y != 1 and x%y == 0:
            break
    else:
        prime_lst.append(x)
  factors = []
  for i in prime_lst[:len(prime_lst)//2]:
    if n%i == 0 and i in prime_lst:
      factors.append(i)
  return sum(factors)

print(sum_of_prime_factors(60))
        