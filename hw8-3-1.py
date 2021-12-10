# Author: Nolan (AMDG) 1/9/2021

def sum_odds(num):
    odd_num = 0
    x = 0
    while x < len(num):
        if num[x] % 2 != 0:
            odd_num += num[x]
            x += 1
        else:
            x += 1
    return odd_num


print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)