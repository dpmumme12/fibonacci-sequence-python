from time import sleep

def fib_seq(terms):
    n1, n2 = 0, 1
    #print("Fibonacci sequence:")
    for x in range(terms):
       # print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        #sleep(1)

    return n1

# recursive solution for the fib sequence
def fib_rec(n):
   
    if n == 0 or n == 1:
        return n
    
    else:
        return fib_rec(n-1) + fib_rec(n-2)


n = 10
cache = [None] * (n + 1)

# dynamic solution for the fib sequence using memoization
def fib_dyn(n):
    
    if cache[n] != None:
        return cache[n]
   
    if n == 0 or n == 1:
        return n
    
    else:
        
        m = fib_rec(n-1) + fib_rec(n-2)
        cache[n] = m
            
    return m

terms = int(input("How many sequences? "))

print(f"Fibonacci: {fib_seq(terms)}")