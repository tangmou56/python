def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def anni(n):
	print(fact(365)/fact(365-n)*1/365**n)
	
	
def hach(n,m):
	print(fact(m)/fact(m-n)*1/m**n)