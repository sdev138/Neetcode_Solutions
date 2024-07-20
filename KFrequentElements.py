# 'List' is only available in the typing module
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequentElements = {}
        result = []
        for number in nums:
            if number not in frequentElements:
                frequentElements[number] = 1
            else:
                frequentElements[number] += 1

        # this line sorts the values in the dictionary in
        # reverse order, based on their values
        sorted_dict = dict(sorted(frequentElements.items(),
                           key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        counter = 0
        for i in sorted_dict:
            result.append(i)
            counter += 1

            if counter == k:
                break
        return result


def main():
    solution = Solution()
    nums = [2, 2, 2, 1, 3, 3]
    k = 2
    solution.topKFrequent(nums, k)


main()
