def bignumber(n):

    a=n[0]
    for i in n:
        if i>a:
            a=i
    print(f"big number is {a}")


def sort(n):
    print("sorting...")
    for i in range(1,len(n),1):
        for j in range(0,len(n)-i,1):
            if n[j]>n[j+1]:
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    for i in n:
        print(i)


def smallnumber(n):
    a=n[0]
    for i in n:
        if i<a:
            a=i
    print(f"small number is {a}")

def reverse(n):
    print("reverse...")
    for i in range(len(n)-1,-1,-1):
        print(n[i])


def sum(n):
    a=0
    for i in n:
        a=a+i
    print(f"sum is {a}")


nums=[55,77,89,30,34]

bignumber(nums)
sort(nums)
smallnumber(nums)
reverse(nums)
sum(nums)
