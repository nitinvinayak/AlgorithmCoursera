# Uses python3
import sys

def lcm_naive(a, b):
    current_gcd = 1
    max=b
    min=a
    if (a>b):
    	max=a
    	min=b
    if (min==0):
        return 0
    while(max%min!=0):
    	current_gcd=min
    	min=max%min
    	max=current_gcd
    else:
        current_gcd=min
	
    
    return int(a*b/current_gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

