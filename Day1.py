#1. positive negative
#n=int(input())
#if n>0:
 #   print("positive")
#elif n<0:
 #   print("negative")
#else:
 #   print("zero")

#2.Even or odd
#n=int(input())
#if n%2==0:
 #   print("e")
#else:
 #   print("o")

# #3.Sum of n natural no
# n=int(input())
# sum=0
# for i in range(1,n):
#     sum+=i
# print(sum)

# #4. range
# l=int(input())
# h=int(input())
#sum=0
# for i in range(l,h):
#     sum+=i
# print(sum)

#5.greatest of two numbers
# n=int(input())
# n2=int(input())
# if n>n2:
#     print(n)
# elif n2>n:
#     print(n2)
# else:
#     print("same")

#6.greatest of three numbers
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2 & n1>n3:
#     print(n1)
# elif n2>n1 & n2>n3:
#     print(n2)
# else:
#     print(n3)

#7.Leapyear or not
# n=int(input())
# if n%400:
#     if n%4 & n%100!=0:
#         print("y")
# else:
#     print("n")

#8. prime number
# n=int(input())
# c=0
# for i in range(2,n):
#     if n%i==0:
#         c+=1
# if c>0:
#     print("not prime")
# else:
#     print("prime")


#9. prime number in given range
# start = int(input())
# end = int(input())

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

#10. sum of digits of a number
n=int(input())
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10
print(sum)
























