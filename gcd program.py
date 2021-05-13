
def hcf(a, b):
    if(b == 0):
        return(a)
    elif(a>b):
        return(a%b)
    

v=hcf(60,48)
print("The gcd of 60 and 48 is : ",v)

