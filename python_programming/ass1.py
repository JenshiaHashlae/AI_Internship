# a=10
# b=3
# sum=a+b
# print("sum:",sum)
# difference=a-b
# print("differnce:",difference)
# product=a*b
# print("product:",product)
# div=a/b
# print("div:",div)
# floor_div=a//b
# print("floor_div:",floor_div)
# modulo=a%b
#print("modulo:",modulo)


# weight_kg=55
# height_m=1.75
# BMI=weight_kg/(height_m*height_m)
# print(BMI)


# a="Python"
# print(a[0])
# print(a[5])


# b="Python programming is fun "
# print(b[19:25])


# num_str="123"
# print(int(num_str))


# year=int(input("Enter the year:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")



# num = 11
# if num > 1:
#     for i in range(2,int(num/2)+1):
#         if num % i == 0:
#            print(num," is not a prime number")
#            break
#     else:
#       print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")

# string="malayalam"
# j=-1
# flag=0
# for i in string:
#     if i!=string[j]:
#         flag=1
#         break
#     j=j-1
# if flag==1:
#     print("false")
# else:
#     print("yes")

# for i in range(1,101):
#      print(i)


# num=[n for n in range(1,30) if n%5==0]
# print(num)



# sum=sum(range(1,101))
# print(sum)

# rows=5
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()


num=int(input("Enter the num:"))
sum=0
i=0
while i<=num:
    
    if i % 2==0:
        print(i)
        sum+=i
    i+=1
print("sum of even numbers is :",sum)


