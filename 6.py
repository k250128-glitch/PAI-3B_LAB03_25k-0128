def top_k_frequent(nums, k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

    return [item[0] for item in sorted_items[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))
