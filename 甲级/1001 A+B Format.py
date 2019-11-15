in_ = input()
a, b = in_.split(" ")
a, b = int(a), int(b)
res = str(a+b)[::-1]
res1 = ""
for (i,x) in enumerate(res):
    res1+=x
    if len(res)<=3 or len(res)==4 and res[-1]=="-":
        pass
    else:
        if i!=0 and (i+1)%3==0 and res[i+1]!="-":
            res1+=","
print(res1[::-1])