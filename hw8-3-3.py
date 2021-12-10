# Author: Nolan (AMDG) 1/9/2021

def count_odds(num):
    odd_num = 0
    x = 0
    while x < len(num):
        if num[x] % 2 != 0:
            odd_num += 1
            x += 1
        else:
            x += 1
    return odd_num


print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)