def commutative_sum(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    ans[0] = nums[0]
    for i in range(1, n):
        ans[i] = nums[i] + ans[i - 1]
    return ans


if __name__ == '__main__':
    nums: list[int] = [1, 2, 3, 4, 5]

    print(commutative_sum(nums))
