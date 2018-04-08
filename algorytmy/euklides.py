def nwd_reku(a,b):
    if(b == 0):
        return a
    elif(a>=b):
        return(nwd(b,a%b))
    else:
        return(nwd(a,b%a))


def nwd(a,b):
    while(a>0 and b>0):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a,b


print(nwd(20,5))
