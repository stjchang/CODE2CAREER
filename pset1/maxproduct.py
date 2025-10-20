# Problem 1: Given an array of integers, find the maximum product of two integers in the array.

def max_product(arr):
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    negMax1 = max(arr[0], arr[1])
    negMax2 = min(arr[0], arr[1])
    
    for num in arr[2:]:
        if num > 0: # positive number
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
                
        elif num < 0: # negative number
            if num < negMax1: 
                negMax2 = negMax2
                negMax1 = num
            elif num > negMax1:
                negMax2 = num
    
                
    return max(max1 * max2, negMax1 * negMax2)

if __name__ == "__main__":
    arr = [5, -10, -6, 9, 4]
    print(max_product(arr)) 
            
            
            
    
    