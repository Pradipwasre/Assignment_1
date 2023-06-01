#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# In[1]:


def arraypairsum(nums):
    
    nums.sort()
    result = 0
    numlen = len(nums)
    for i in range(0,numlen-1,2):
        result += nums[i]
    return result


# In[6]:


nums = [1,4,3,2]
arraypairsum(nums)


# Question 2
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

# In[10]:


def candytype(candyType):
    length = int(len(candyType)/2)
    unique_candy = len(set(candyType))
    return min(length,unique_candy)


# In[11]:


candyType = [1,1,2,2,3,3]
candytype(candyType)


# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# In[1]:


def harmonious_array(nums):
    letter = {}
    ans = 0
    for i in nums:
        if i not in letter:
            letter[i] = 1
        else:
            letter[i] += 1
    for i in letter:
        if i +1 in letter.keys():
            ans = max(ans,letter[i] + letter[i+1])
    return ans


# In[2]:


nums = [1,3,2,2,5,2,3,7]
harmonious_array(nums)


# Question 4
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# In[3]:


def flowers_place(flowerbed,n):
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False


# In[4]:


flowerbed = [1,0,0,0,1]
n = 1
flowers_place(flowerbed,n)


# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# In[9]:


def maxproduct(nums):
    nums.sort()
    l1 = nums[-1] *nums[-2]*nums[-3]
    l2 = nums[0]* nums[1]*nums[-1]
    return max(l1,l2)


# In[10]:


nums = [1,2,3]
maxproduct(nums)


# Question 6
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.

# In[12]:


def search_ele(nums,target):
    left = 0
    right = len(nums)-1
    while (left <= right):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
            
        else:
            right = mid-1
    return -1


# In[13]:


nums = [-1,0,3,5,9,12]
target = 9
search_ele(nums,target)


# Question 7
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# In[16]:


def ismonotonic(nums):
    if nums[-1] < nums[0]:
        nums = nums[::-1]
        
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True


# In[17]:


nums = [1,2,2,3]
ismonotonic(nums)


# Question 8
# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

# In[19]:


def smallest_range(nums,k):
    if len(nums) <= 1 :
        return 0
    diff = max(nums)- min(nums)
    new_diff = diff-2*k
    if new_diff < 0:
        return 0
    else:
        return new_diff


# In[20]:


nums = [1]
k = 0
smallest_range(nums,k)


# In[ ]:




