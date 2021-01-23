
nums_dict = {}
for a in range(1,5):
    for b in range(1,5):
        result = a**3 + b**3
        print("result:(a,b) : {},({},{})".format(result,a,b))
        if nums_dict.get(result, -1) == -1:
            nums_dict[result] = [(a,b)]
        else:
            nums_dict[result] = nums_dict[result] + [(a,b)]
for k in nums_dict.items():
    if len(k[1])>=6:
        print(k)
    for pairs1 in k[1]:
        for pairs2 in k[1]:
            print("a,b,c,d:{},{},{},{}".format(pairs1[0],pairs1[1],pairs2[0],pairs2[1]))
