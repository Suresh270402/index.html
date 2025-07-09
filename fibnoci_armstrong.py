
#print the fibnocci series. 

a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c

# print the 31 st fibnocci value
a=0
b=1
limit=31
for i in range(limit-1):
    c=a+b
    a=b
    b=c
print(a)


# check the given number is armstrong or not. 
num=153
def fun(num):
    num2 = num
    num3 = num
    count = 0
    while num!=0:
          num=num//10
          count+=1
    total=0
    while num2!=0:
        last_digit=num2%10
        total=total+(last_digit**count)
        num2=num2//10
    if total==num3:
        print("armstrong")
    else:
        print("not a strong armstrong")
fun(num)

