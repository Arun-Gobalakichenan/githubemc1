'''
def gcd(m,n):
    fm=[]
    for i in range (1,m+1):
        if(m%i)==0:
            fm.append(i)
    fn=[]                       #normal or long way of finding gcd
    for j in range(1,n+1):
        if(n%j)==0:
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(print(cf[-1]))
gcd(20,40)

def gcd (m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0: #finding gcd using list
            cf.append(i)
    return(print(cf[-1]))        
gcd(20,40)

def gcd (m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0: #finding gcd without using list by only changing variable value with the latest
            mrcf=i;     # mrcf=most recent common factor(just_a_variable_name)
    return(print(mrcf))        
gcd(20,40)

def gcd(m,n):
    i=min(m,n)
    while (i>0):
        if (m%i)==0 and (n%i)==0:       #another method of finding gcd
            return(print(i))
        else:
            i=i-1
gcd(20,40)
'''

#euclid algorithm for finding gcd
def gcd(m,n):
    if (m<n):
        (m,n)=(n,m)
    if (m%n)==0:
        return(print(n))
    else:
        return(print(gcd(n,m%n))) # m%n is used to get remainder and remainder will be always less than n
gcd(20,40)

#revised euclid algorithm for finding gcd
def gcd(m,n):
    if (m<n):
        (m,n)=(n,m)
    while (m%n) != 0:
        return(print(gcd(n,m%n)))
    return(print(n))
gcd(20,40)