# n=5
# i=1
# while i < 11:
#     print (n, "X", i, "=", n*i)
#     i=i+1


# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("The sum is:", total)

# n = int(input("Enter a number: "))
# count = 0

# while n != 0:
#     n= n//10
#     count=count+1
# print("Number of digits:", count)


# password = "python123"
# guess = input("Enter password: ")

# while password != guess:
#     print("Wrong password")
#     guess = input("Enter password: ")

# print("Correct password!")


# total = 0
# num = int(input("enter the number:"))
# while num !=0:
#     total = total + num
#     num = int(input("enter the another number:"))
#     print("sum of total number: ",total)


# n = int(input("Enter a number: "))
# n=n+1
# result = 1
# i = 1

# for i in range (i, n):
#     result = result * i
#     i = i + 1

# print("Factorial:", result)
      
n = int(input("Enter a number: "))
reverse = 0
while :
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reverse:", reverse)

    
