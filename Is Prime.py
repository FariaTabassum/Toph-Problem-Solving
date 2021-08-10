"""
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
 and ends at a specified number.
 he range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding
 a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
"""
N = int(input())

# If given number is greater than 1
if N > 1:

    # Iterate from 2 to n / 2
    for i in range(2, int(N / 2) + 1):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (N% i) == 0:
            print("No")
            break
    else:
        print("Yes")

else:
    print("No")