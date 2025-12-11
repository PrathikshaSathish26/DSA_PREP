1. positive negative
n=int(input())
if n>0:
   print("positive")
elif n<0:
   print("negative")
else:
   print("zero")

2.Even or odd
n=int(input())
if n%2==0:
   print("e")
else:
   print("o")

#3.Sum of n natural no
n=int(input())
sum=0
for i in range(1,n):
    sum+=i
print(sum)

#4. range
l=int(input())
h=int(input())
sum=0
for i in range(l,h):
    sum+=i
print(sum)

5.greatest of two numbers
n=int(input())
n2=int(input())
if n>n2:
    print(n)
elif n2>n:
    print(n2)
else:
    print("same")

6.greatest of three numbers
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 & n1>n3:
    print(n1)
elif n2>n1 & n2>n3:
    print(n2)
else:
    print(n3)

7.Leapyear or not
n=int(input())
if n%400:
    if n%4 & n%100!=0:
        print("y")
else:
    print("n")

8. prime number
n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c>0:
    print("not prime")
else:
    print("prime")

9. prime number in given range
n = int(input())
m = int(input())
for i in range(n, m + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

10. sum of digits of a number
n=int(input())
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10
print(sum)

11. Reverse of a number
n=int(input())
rev=1
while n>0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)

12. palindrome
n=int(input())
t=n
rev=1
while n>0:
    d=n%10
    rev=(rev*10)+d
    n//=10
if rev==t:
    print("y")
else:
    print("n")

13. armstrong
n=int(input())
t=n
p=len(str(n))
s=0
while n>0:
    d=n%10
    s+=d**p
    n//=10
if s==t:
    print("y")
else:
    print("n")

14. armstron in a range
n = int(input())
m = int(input())
for i in range(n, m):
    t = i
    p = len(str(i))
    s = 0
    temp = i      
    while temp > 0:
        d = temp % 10
        s += d ** p
        temp //= 10
    if s == t:
        print(i,end=" ")

15. fibonnoci
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a, b = b, a + b

16. nth term of fibonnaci
n = int(input())
a = 0
b = 1
l=[]
for i in range(n):
    l.append(i)
    a, b = b, a + b
print(l[-1])

17. factorial of a number
n=int(input())
s=1
for i in range(1,n+1):
    s*=i
print(s)

18. power of a number
n=int(input())
p=int(input())
print(n**p)

19. factor of a number
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(*l)

20. prime factors of a number
n=int(input())
l=[]
k=[] 
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in l:
    if j==1:
        continue
    c=0
    for x in range(2, j):
        if j%x== 0:
            c+=1
    if c==0:
        k.append(j)
print(*k)

21. strong number
n=int(input())
s=0
t=n
while n>0:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    s+=fact
    n//=10
if s==t:
    print("yes")
else:
    print("no")

22. perfect number
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("y")
else:
    print("n")

23. perfect square
n=int(input())
c=0
for i in range(1,int(n/2)):
    if i**2==n:
        c+=1
if c>0:
    print("y")
else:
    print("n")

24. automorphic
n=int(input())
l=len(str(n))
sq=str(n**2)
a=sq[-l:]
if str(n)==a:
    print("y")
else:
    print("n")

25. harshad
n=int(input())
s=0
while n>0:
    d=n%10
    s+=d
    n//=10
if n%s==0:
    print("y")
else:
    print("n")

26. abundant number
n=int(input())
l=[]
s=0
for i in range(1,n):
    if n%i==0:
        l.append(i)
for j in l:
    s+=j
if n<s:
    print("y")
else:
    print("n")

27. friendly pair
a,b= list(map(int,input().split()))
s1=0
s2=0
for i in range(1,a):
    if a%i==0:
        s1+=i
for j in range(1,b):
    if b%j==0:
        s2+=j
x=int(a/s1)
y=int(b/s2)
if x==y:
    print("y")
else:
    print("n")
        























