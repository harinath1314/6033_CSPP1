#define the gen_primes function here
def genPrimes():
    a=1
    b=0
    while True:
        next = a+b
        yield next
        b = a
        a = next

# def main():
#   data=input()
#   l=data.split()
#   a=int(l[0])
#   b=int(l[1])
#   primeGenerator = genPrimes()
#   for i in range(a):
#       p=primeGenerator.__next__()
#       if(i%b==0):
#           print(p)
gen_i = genPrimes()
print(gen_i.__next__())
    
# if __name__== "__main__":
#   main()
