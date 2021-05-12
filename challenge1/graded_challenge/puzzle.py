#! usr/bin/env python3

"""find 2 numbers sum to 2020 and return their multiplication """
def to_sum(nums,n):
    for num in nums:
        if str(2020-int(num)-int(n)) in nums:
            return int(num) * (2020-int(num)-int(n))

"""find 3 numbers sum to 2020 and return their multiplication"""
def three_sum(nums):
    for num1 in nums:
        temp = nums
        temp.remove(num1)
        if to_sum(temp,num1):
            return to_sum(temp,num1)*int(num1)


if __name__ == "__main__":
    
    with open("puzzle1.txt","r") as numfile:
        nums = numfile.read().splitlines()

        result = to_sum(nums,"0")
        print("The 1st puzzle answer is", result)

        result = three_sum(nums)
        print("The 2nd puzzle answer is", result)
