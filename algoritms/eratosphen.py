

def eratosfen(n):
    """Алгорим решето эратосфена, для нахождения простых чисел"""
    a = [True]*n
    a[0]=a[1]=False
    for k in range(2,n):
        if a[k]:
            for m in range(2*k,n,k):
                a[m] = False
    m = []
    for k in range(n):
        if a[k]:
            m.append(k)
    return m

if __name__ == '__main__':
    m = eratosfen(1000000000)
    print(m)

