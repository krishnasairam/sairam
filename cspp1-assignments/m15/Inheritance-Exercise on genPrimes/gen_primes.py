#define the gen_primes function here
def genPrimes(limit):
    D = {}
    q = 2
    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
def main():
    p = genPrimes(int(input()))
    prms = [i for i in p]
    print(tuple(prms)) 
if __name__== "__main__":
    main()
