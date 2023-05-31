#!/usr/bin/env python
# coding: utf-8

# <aside>
# 💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# </aside>

# In[3]:


def two_sum(nums, target):
    seen = {}
    
    for i,value in enumerate(nums):
        remaining = target - nums[i]
        
        if remaining in seen:
            return [i,seen[remaining]]
        
        else:
            seen[value] = i


# In[4]:


nums = [2,7,11,15]
target = 9
two_sum(nums,target)


# <aside>
# 💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# 
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 
# </aside>

# In[29]:


def remove_ele(nums,val):
    
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


# In[56]:


nums = [3,2,2,3]
val =  3
remove_ele(nums,val)


# <aside>
# 💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# </aside>

# In[52]:


def find_target(nums,target):
    
    i = 0
    
    while i < len(nums) and nums[i]<target:
        i +=1 
            
    return i 
    


# In[54]:


nums = [1,3,5,6]
target = 5
find_target(nums,target)


# In[40]:


#def find_target(nums, target):
    
#    for i in range(len(nums)-1):
#        if nums[i] == target:
#            return i
#        if nums[i]< target and target < nums[i+1]:
#            return nums[i] 


# Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# In[57]:


def increment_one(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] != 9:
            digits[i] +=1
            break
        else:
            digits[i] = 0
    
    if digits[i] == 0:
        digits.insert(0,1)
    return digits


# In[59]:


digits = [1,2,0]
increment_one(digits)


# Q5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# In[18]:


def merge_lists(nums1,m,nums2,n):
    i = m-1
    j = n-1
    for right in range(m+n-1,-1,-1):
        if j < 0:
            break
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[right] = nums1[i]
            i -= 1
        else:
            nums1[right] = nums2[j]
            j -= 1 
        
    return nums1


# In[19]:


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,7]
n = 3
merge_lists(nums1,m,nums2,n)


# Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# In[36]:


def duplicates(nums):
    
    hashset = set()
    
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)


# In[37]:


nums = [1,2,3,1]


# In[38]:


duplicates(nums)


# Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

# In[42]:


def movezeros(nums):
    
    slow = 0
    for fast in range(len(nums)):
        
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow],nums[fast] = nums[fast], nums[slow]
            
        if nums[slow] != 0:
            slow +=1 
    return nums


# In[45]:


nums = [0,1,0,3,12]
movezeros(nums)


# Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# In[ ]:


def findErrorNums(self, nums):
      l, dup, mis = len(nums), 0, 0
      for num in nums:
          if nums[abs(num) - 1] < 0 :
              dup = abs(num)
          else: nums[abs(num) - 1] *= -1
      
      for index in range(l):
          if nums[index] > 0:
              mis = index + 1
              break
              
      return [dup, mis]


# In[63]:


def finderror(nums):
    l, dup, mis = len(nums), 0,0
    
    for num in nums:
        if nums[abs(num)-1]< 0:
            dup = abs(num)
        else:
            nums[abs(num)-1] *= -1
        
        
    for index in range(l):
        if nums[index] > 0:
            mis = index +1
            break
            
    return [dup,mis]


# In[64]:


nums = [1,2,2,4]
finderror(nums)

