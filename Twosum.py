
def twoSum(nums, target):

    complement_map = {}
    for index, num in enumerate(nums):

        if num in complement_map:
            result = [index , complement_map[num]]
            return result

        else: 
            complement = target - num
            complement_map[complement] = index
    
            
        