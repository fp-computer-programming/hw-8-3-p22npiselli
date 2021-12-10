# Author: Nolan (AMDG) 1/9/2021

def sum_no_odds(num):
    total = 0
    x = 0
    while x < len(num):
        if num[x] % 2 == 0:
            total += num[x]
            x += 1
        elif num[x] % 2 != 0:
            return total
    return total


print(sum_no_odds([2, 4, 6, 8, 9]) == 20)
print(sum_no_odds([13, 12, 10]) == 0)
print(sum_no_odds([14, 16, 32]) == 62)