def main():
    in_1 = list(map(float, input().split(" ")))
    in_2 = list(map(float, input().split(" ")))
    K1, K2 = int(in_1.pop(0)), int(in_2.pop(0))

    if K1 == 0 and K2 == 0:
        return "0"
    elif K1 == 0:
        res = [0 for i in range(int(in_2[0])+1)]
    elif K2 == 0:
        res = [0 for i in range(int(in_1[0])+1)]
    else:
        res = [0 for i in range(int(max(in_1[0], in_2[0]))+1)]
    # print(in_1, in_2)
    # print(res)
    for i in range(0, max(len(in_1), len(in_2)), 2):
        if i<len(in_1):
            res[int(in_1[i])]+=in_1[i+1]
        if i<len(in_2):
            res[int(in_2[i])]+=in_2[i+1]
    # for i in range(0, len(in_2), 2):
    #     res[int(in_2[i])]+=in_2[i+1]
    res1 = ""
    cnt = 0
    for (i, x) in enumerate(res):
        if x!=0:
            res1 = " "+str(x)+res1
            res1 = " "+str(i)+res1
            cnt+=1
    res1 = str(cnt)+res1 
    return res1

if __name__ == '__main__':
    print(main())