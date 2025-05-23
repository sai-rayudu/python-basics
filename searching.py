nums=(4,5,6,7,8)
a=9
find=False
for i in nums:
    if i==a:
        print("found")
        find=True
    
if not find:
    print("not found")
