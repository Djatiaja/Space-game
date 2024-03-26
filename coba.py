# a = 10 
# b = 20

# def change():
#     global b 
#     a = 45
#     b = 56 

# change()

# print(a)
# print(b)



# def display(b, n):
#     while n>0:
#         print(b, end="")
#         n=n-1

# display("z", 3)


# def foo(k):
#     k[0]= 1
# q=[0]

# foo(q)

# print(q)



# def cube(x):
#     return x*x*x

# x= cube(3)
# print(x)

# def power(x, y=2):
#     r=1
#     for i in range(y):
#         r= r * x

#     return r

# print( power(3))
# print(power(3,3))



# i=0
# def change(i):
#     i=i+1
#     return i 

# change(1)

# print(i)


# def sum (*arg):
#     r=0
#     for i in arg:
#         r+=i
#     return r

# print(sum.__doc__)
# print(sum(1,2,3))
# print(sum(1,2,3,4,5 ))


# def f(): x=4

# x=2

# f()

# print(x)

# def funct(a, b=5, c=10):
#     print(a, b, c)

# funct(3,7)

# funct(25,c=24)

# funct(c=11, a=2)

# def f1(x):
#     global x 
#     x+=1
#     print(x)

# f1(15)
# print("hello")

# def foo():
#     def f1():
#         print("asu")
#     return Total +1

# Total= 0

# print(foo())
# f1()


# def a(b):
#     b=b+[5]


# c=[1,2,3,4]
# a(c)
# print(len(c))

# li=[]
# def convert(b):
#     if (b==0):
#         return 1
#     dig=b%2
#     li.append(dig)
#     convert(b//2)

# convert(6)
# li.reverse()

# for i in li:
#     print(i, end=" ")

# def test(i, j):
#     if (i==0):
#         return j
#     else:
#         return test(i-1, i+j)
# print(test(4,7))



# def fact(num):
#     if num==0 :
#         return 0
#     elif num ==1:
#         return 1
#     else:
#         return fact(num-1)+fact(num-2)
    
# for i in range(0,4):
#     print(fact(i))


# def fun(n):
#     if (n>100):
#         return n -5
#     return fun (fun(n+11))
# print(fun(45))