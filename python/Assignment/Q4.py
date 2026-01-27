# Problem Statement: Can Place Flowers
# You are given a flowerbed represented by an integer array flowerbed, where:
# 1 indicates a plot that already has a flower planted
# 0 indicates an empty plot
# 
# You are also given an integer n, representing the number of new flowers you want to plant.
# Rule
# No two flowers can be planted in adjacent plots
# Your task is to determine whether it is possible to plant “n” new flowers in the flowerbed without violating the no-adjacent-flowers rule.
# 
# Input
# An integer array flowerbed consisting only of 0s and 1s
# An integer n representing the number of flowers to plant
# Output
# Return true if n new flowers can be planted safely
# Return false otherwise
# 
###################### Examples ######################
# Example 1
# Input:  flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2
# Input:  flowerbed = [1,0,0,0,1], n = 2
# Output: false
#######################################################
# Task
# Write a program or function to check whether it is possible to plant the given number of flowers while ensuring that no two flowers are placed next to each other.

def flowerBed(bed, n):
    for i in range(len(bed)):
        if bed[i] == 0:
            # Check if left plot is empty (or doesn't exist)
            empty_left = (i == 0) or (bed[i - 1] == 0)
            # Check if right plot is empty (or doesn't exist)
            empty_right = (i == len(bed) - 1) or (bed[i + 1] == 0)
            
            if empty_left and empty_right:
                bed[i] = 1
                n -= 1
    
    return n == 0

print(flowerBed([1,0,0,0,1], 1))
print(flowerBed([1,0,0,0,1], 2))
