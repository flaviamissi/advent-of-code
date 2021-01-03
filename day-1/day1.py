from typing import List


def findpair(target: int, numbers: int) -> List[int]:
    i = 0
    a = numbers[i]
    numbers1 = numbers[i+1:]
    b = target - a
    if b in numbers1:
        return [numbers[i], numbers[numbers.index(b)]]

    return findpair(target, numbers1)


def findtriple(target: int, numbers: int) -> List[int]:
    for i, n in enumerate(numbers):
        if i+1 >= len(numbers):
            break
        item = numbers[i]
        nums = findpair(target - n, numbers[i+1:])
        if sum(nums) + item == target:
            nums.append(item)
            return nums
    return []


def readnums(file_name: str ='input.txt') -> List[int]:
    file = open(file_name, mode='r')
    nums = []
    for num in file.readlines():
        nums.append(int(num.rstrip('\n')))
    file.close()
    return nums


if __name__ == '__main__':
    nums = readnums()
    sum_ = findtriple(2020, nums)
    print('the 2 numbers which sum == 2020 are: ', sum_)
    print('their multiplication is:', sum_[0] * sum_[1] * sum_[2])
