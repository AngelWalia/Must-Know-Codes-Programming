#Program to find the reverse of a number

'''Program takes a number from the user and returns the reverse. For Example:

1234 --> 4321
901  --> 109

'''

def RevNum(n):
    rev=0
    while n>0:
        rev=(rev*10)+(n%10)
        n=n//10

    return rev


if __name__=='__main__':
    print(RevNum(1234))
    print(RevNum(901))
    
