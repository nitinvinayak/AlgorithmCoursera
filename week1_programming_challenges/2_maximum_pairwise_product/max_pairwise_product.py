# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1=0
    max2=0
    for first in range(n):
        if(numbers[first]>max1):
            max1=numbers[first]
            index=first
        
    for second in range(n):
        if(numbers[second]>max2 and second!=index):
            max2=numbers[second]
                
    max_product=max1*max2

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
