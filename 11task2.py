def smallestDivisor(n): 
    if (n % 2 == 0): 
        return 2; 
    x = 3;  
    while(x * x <= n): 
        if (n % x == 0): 
            return x; 
        x += 2; 
  
    return n; 
  
n = int(input())
print(smallestDivisor(n)