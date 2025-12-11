#28. Highest common factor and gcd
# a=int(input())
# b=int(input())
# l=[]
# k=[]
# z=[]
# for i in range(1,a+1):
#     if a%i==0:
#         l.append(i)
# for j in range(1,b+1):
#     if b%j==0:
#         k.append(j)
# for x in l:
#     if x in k:
#         z.append(x)
# print(z[-1])

#29. Lcm
# a=int(input())
# b=int(input())
# l=[]
# k=[]
# z=[]
# for i in range(1,a+1):
#     if a%i==0:
#         l.append(i)
# for j in range(1,b+1):
#     if b%j==0:
#         k.append(j)
# for x in l:
#     if x in k:
#         z.append(x)
# hcf=z[-1]
# if hcf==1:
#     print(a*b)
# else:
#     print(int(a*b)/hcf)

#30. binary to decimal
# b=input()
# d=0
# p=0
# for i in b[::-1]:
#     d+= int(i)*(2**p)
#     p+=1
# print(d)

#31. Octal to decimal
# b=input()
# d=0
# p=0
# for i in b[::-1]:
#     d+= int(i)*(8**p)
#     p+=1
# print(d)

#32. hexadecimal to decimal
# hex_num = input().upper()
# hex_dict = {'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}
# decimal = 0
# power = 0
# for digit in hex_num[::-1]:
#     if digit.isdigit():          
#         value = int(digit)
#     else:                        
#         value = hex_dict[digit]

#     decimal += value * (16 ** power)
#     power += 1
# print(decimal)

#33. decimal to binary
# n=int(input())
# b=""
# while n>0:
#     b=str(n%2)+b
#     n//=2
# print(b)

#34. decimal to oct
# n=int(input())
# b=""
# while n>0:
#     b=str(n%8)+b
#     n//=8
# print(b)

#35. decimal to hex
# n=int(input())
# hex={10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# d=""
# while n>0:
#     r=n%16
#     if r<10:
#         d=str(r)+d
#     else:
#         d=hex[r]+d
#     n//=16
# print(d)

#36. binary to octal
# s = input()
# b = ""
# while len(s) % 3 != 0:
#     s = "0" + s
# for i in range(0, len(s), 3):
#     a = s[i:i+3] 
#     n = int(a)
#     d= 0
#     p=0
#     while n > 0:
#         r = n % 10
#         d+=r*(2**p)
#         p+=1
#         n//=10
#     b+=str(d)
# print(b)

#37. octal to binary
# s = input()
# b = ""
# for d in s:
#     n = int(d)
#     t=""
#     while n>0:
#         t=str(n%2) +t
#         n//=2
#     while len(t)<3: 
#         t="0"+t
#     b +=t
# b = b.lstrip("0")
# print(b)

#38. quadrants
# x,y=list(map(int,input().split()))
# if x>0 and y>0:
#     print("First Quadrant")
# elif x<0 and y>0 :
#     print("Second Quadrant")
# elif x<0 and y<0:
#     print("Third Quadrant")
# elif x>0 and y>0:
#     print("Fourth Quadrant")
# elif x==0 and y==0:
#     print("Origin")
# elif x!=0 and y==0 :
#     print("x-axis")
# elif x==0 and y!=0:
#     print("y-axis")
# else:
#     print("nil")

#39. permutations
# def fact(n):
#     r=1
#     for i in range(1,n+1):
#         r*=i
#     return r
# n=int(input())
# r=int(input())
# if r>n:
#     print("nil")
# else:
#     a=fact(n)//fact(n-r)
#     print(a)

#40. replace 0 with 1
# s=input()
# s1=''
# for i in range(len(s)):
#     if s[i]=="0":
#         s1+="1"
#     else:
#         s1+=s[i]
# print(s1)

#41. swapping two arrays
# a = []
# b = []
# for i in range(4):
#     a.append(int(input()))
# for i in range(4):
#     b.append(int(input()))
# for i in range(4):
#     a[i], b[i] = b[i], a[i]
# print("A =", a)
# print("B =", b)

# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# t=a
# a=b
# b=t
# print(a)
# print(b)

#42. sorting in string
# s=list(input())
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if ord(s[i])>ord(s[j]):
#             s[i],s[j]=s[j],s[i]
# print(*s,sep='')

#43. unique characters
# s=input()
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
# print(len(d))

#44. import numpy as np
# import ast
# # Ultra-fast for large data
# m1 = np.array(ast.literal_eval(input()))
# m2 = np.array(ast.literal_eval(input()))
# print(np.dot(m1,m2).tolist())

#45. rotation of one place
# s=input()
# a=s[-1]+s[:2]
# print(a)

#46. area of incircle
# a,b,c=list(map(int,input().split()))
# r=float(a+b-c)/2
# area=(22/7)*(r**2)
# print(round(area,3))

#47. panagram
# s=input().lower()
# a=set("abcdefghijklmnopqrstuvwxyz")
# p=set(s)
# miss=sorted(a-p)
# print(*miss,sep='')

#48.f to cel
# f = float(input())
# c = (f - 32) * 5/9
# print(c)

#49. sum of all prime
n=int(input())
t=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j== 0:
            break
    else:  
        t+=i
print(t)



