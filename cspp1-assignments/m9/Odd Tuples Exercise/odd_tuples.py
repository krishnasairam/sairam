'''Exercise : Odd Tuples ''' 
def oddTuples(aTup):
    '''returns: tuple, every other element of aTup. '''
    new = ()
    a = 0
    for t in aTup:
        if a % 2 == 0:
            new = new + (t,)
        a += 1       
    return new
def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (str(data[j]),)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()