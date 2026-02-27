def top_k_frequent(nums, k):
    count = {}

    # 1) frequency count
    for x in nums:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1

    # 2) pick max frequency k times (simple)
    result = []
    for _ in range(k):
        max_freq = max(count.values())

        for key, value in count.items():
            if value == max_freq:
                result.append(key)
                del count[key]
                break

    return result


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # expected [1, 2]