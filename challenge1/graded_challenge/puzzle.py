#! usr/bin/env python3

"""find 2 numbers sum to 2020 and return their multiplication """
def to_sum(nums):
    for num in nums:
        if str(2020-int(num)) in nums:
            return [int(num), (2020-int(num))]

"""find 3 numbers sum to 2020 and return their multiplication"""
def three_sum(nums):
    for num1 in nums:
        temp = nums
        temp.remove(num1)
        for num2 in temp:
            if str(2020-int(num1)-int(num2)) in temp:
                return [int(num1), int(num2), (2020-int(num1)-int(num2))]


if __name__ == "__main__":
    
    with open("puzzle1.txt","r") as numfile:
        nums = numfile.read().splitlines()

        result = to_sum(nums)
        print("\nThe 1st puzzle answer\n")
        print("The numbers are",result[0],result[1])
        print("Final answer is",result[0]*result[1])

        result = three_sum(nums)
        print("\nThe 2nd puzzle answer\n")
        print("The numbers are",result[0],result[1],result[2])
        print("Final answer is",result[0]*result[1]*result[2])
