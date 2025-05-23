num=[23,45,67,89,90]

for i in range(1,len(num),1):
    for j in range(0,len(num)-i,1):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp

for i in num:
    print(i)