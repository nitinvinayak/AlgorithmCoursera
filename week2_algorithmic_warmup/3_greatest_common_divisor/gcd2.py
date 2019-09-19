# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    max=b
    min=a
    if (a>b):
    	max=a
    	min=b
    while(max%min==0):
    	current_gcd=min
    	max,min=min,max/min
    	
	

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
