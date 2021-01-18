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

terms = int(input("How many sequences? "))

print(f"Fibonacci: {fib_seq(terms)}")