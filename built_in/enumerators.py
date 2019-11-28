# nums = [10, 20, 55, 100]

# largest = max(nums)
# smallest = min(nums)
# # print(largest)
# # print(smallest)

# # total = 0
# # for num in nums:
# #     total += num

# # total = sum(nums)
    
# # print(total)

# nums = [10, 20, 55, 100]

# def is_even(num):
#     return num % 2 == 0

# are_all_even = all(is_even(num) for num in nums)
# print(are_all_even)





# name = "ALEX"
# all_upper = all(letter.isupper() for letter in name)
# print(all_upper)

passwords = ["pwd1234", "ADMIN", "password", "12345", "!!!!!?", "$$$$$$$$$$"]

safe_passwords = sum(password.isupper() for password in passwords)
print(safe_passwords)