class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers, start=1):
            for index1, value1 in enumerate(numbers,start=1):
                if value +value1 == target and index != index1:
                    return ([index, index1])
                    break

        

        