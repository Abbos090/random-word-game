# def liner_search(nums, num):
#     cnt = 0
#     for i in range(len(nums)):
#         cnt += 1
#         if nums[i] == num:
#             return i, cnt
        
# def binary_search(nums, num):
#     low = 0
#     cnt = 0
#     high = len(nums) - 1
#     while low <= high:
#         cnt += 1
#         mid = (low + high) // 2
#         guess = nums[mid]
#         if guess < num:
#             low = mid + 1
#         elif guess > num:
#             high = mid - 1
#         else:
#             return mid,cnt
        
# matn = ['abbos','abduraxim', 'sarvarbegim','aziz', 'olim', 'qodirali']
# matn.sort()
# print(matn)
# print(binary_search(matn, 'olim'))
# print(liner_search(matn, 'olim'))

