# import bisect
#
# n = int(input())
# nums = list(map(int, input().split()))
# dp = []
# arr = []
#
# dp.append(1)
# arr.append(nums[0])
#
# for i in range(1,n):
#     if nums[i] <= arr[-1]:
#         rs = bisect.bisect_left(arr, nums[i]) # nums[i]가 arr의 몇번째 인덱스인지 이진탐색 후 반환
#         arr[rs] = nums[i]
#     elif nums[i] > arr[-1]:
#         arr.append(nums[i])
#         dp.append(dp[-1]+1)
#
#
# print(max(dp))
#
# # Arr에 20 추가
# # bisect.bisect_left([10,20], 10) 에서 기존 인덱스 값 10의 왼쪽인 0번째 인덱스가 반환, arr[0] = 10
# # bisect.bisect_left([10,20,40], 30) 에서 삽입 위치 인덱스 2가 반환, arr[2] = 30
# # arr에 50 추가
#
#
# # import bisect
# #
# # n = int(input())
# # array = list(map(int, input().split()))
# # dp = []
# # x = []
# #
# # dp.append(1)
# # x.append(array[0])
# #
# # for i in range(1, len(array)):
# #     if array[i] > x[-1]: # 현재 값이 x 배열의 마지막 값보다 클 경우
# #         x.append(array[i]) # x 배열에 현재 값을 추가해 주고
# #         dp.append(dp[-1] + 1) # 증가 부분 수열의 길이를 1 증가시킨다.
# #     else: # 그렇지 않을 경우
# #         idx = bisect.bisect_left(x, array[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
# #         x[idx] = array[i] # x 배열의 idx 위치에 현재 값을 넣어준다.
# #
# #
# # print(max(dp))
import bisect

n = int(input())
nums = list(map(int, input().split()))
dp = []
x = []

dp.append(1);
x.append(nums[0])

for i in range(1,n):
    if nums[i] > x[-1]:
        x.append(nums[i])
        dp.append(dp[-1]+1)
    else:
        idx = bisect.bisect_left(x, nums[i])
        x[idx] = nums[i]


print(len(x))