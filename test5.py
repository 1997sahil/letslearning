# #List
# marks= [10,20,30,40,29]
# print (marks)
# print (marks [0])
# print (marks [-1])
# marks.insert (0,88)
# print(marks)
# #Slicing
# nums = [10, 20, 30, 40, 50]
# print(nums[1:3])    # [20, 30]  (index 1 up to, not including, 3)
# print(nums[:2])     # [10, 20]  (from start)
# print(nums[2:])     # [30, 40, 50]  (to end)
# print(nums[::-1])   # [50, 40, 30, 20, 10]  (reversed)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # with index:
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# num =[10,20,30,30,40,30,88,78,3]
# print("Sum of total number: ", sum(num))
# print("Min Number: ", min(num))
# print("Max Number:", max(num))


# nums = [3, 8, 15, 22, 7, 19, 4]
# new_list = []
# for num in nums:
#     if num > 10:
#         new_list.append(num)
#         print(new_list)

# nums = [3, 8, 15, 22, 7, 19, 4]
# reversed_nums = []
# for i in range(len(nums) -1,-1,-1):
#     reversed_nums.append(nums[i])
#     print(reversed_nums)

# nums = [1, 2, 2, 3, 4, 4, 5]
# new_num = []
# for i in nums:
#     if i not in new_num:
#         new_num.append(i)
#         print(new_num)

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 1]
print(evens)    # [0, 2, 4, ..., 18]