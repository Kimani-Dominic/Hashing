def find_frequent_elements(nums):
    # Dictionary to store the frequency of each element
    frequency_dict = {}
    
    # Iterate through the array and count the occurrences of each element
    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Find the maximum frequency
    max_frequency = max(frequency_dict.values())
    
    # Create a list of elements with the maximum frequency
    frequent_elements = [element for element, frequency in frequency_dict.items() if frequency == max_frequency]
    
    return frequent_elements

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
result = find_frequent_elements(nums)
print(result)
