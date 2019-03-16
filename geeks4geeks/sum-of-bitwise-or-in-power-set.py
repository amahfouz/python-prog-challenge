#!/bin/python
#
# Solution for
# https://www.geeksforgeeks.org/sum-of-bitwise-or-of-all-possible-subsets-of-given-set/

# Let 'n' be the number of members of the original set
#
# Total number of subsets is 2^n (including empty set)
#
# In any given subset, for the i[th] bit to be 
# zero all corresponding bits in set members must
# be zero. Let the number of members where that 
# bit is zero to be 'zi'. So the number of sets
# made up of these numbers is 2^zi. Negating the
# condition, the number of sets where this bit is
# 1 is equal 2^n - 2^zi.
# 
# So all has to be done is to compute the number of
# members that have the i[th] bit as zero for every
# i from 0 to 31.
#

# length of integers in the problem
NUM_SIZE = 32
def or_sum(arr):
    zero_count = [0 for _ in range(NUM_SIZE)]

    for index in range(NUM_SIZE):
        for num in arr:
            if not (num & (1 << index)):
                zero_count[index] += 1
            num >> 1

    # all zeros have now been computed

    result = 0
    two_pow_n = 1 << len(arr)
    for i in range(NUM_SIZE):
        num_subsets = two_pow_n - (1 << zero_count[i])
        val_of_bit = 1 << i
        contribution = num_subsets * val_of_bit
        result += contribution

    return result    

if __name__ == "__main__": 
    arr = [ 1, 2, 3 ]
    print or_sum(arr)