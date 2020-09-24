sum = 0
for ele in range(1, 1000):
    for i in range(1, ele + 1):
        if ele % i == 0 and i != 1 and i != ele:
            break
    else:
        print(ele)
        # sum += ele
print(sum)

