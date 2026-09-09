def majority_element(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    n = len(nums)

    for num, count in freq.items():
        if count > n // 2:
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))
