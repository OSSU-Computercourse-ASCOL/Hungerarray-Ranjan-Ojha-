s = 'azcbobobegghakl'

curMax = 0
Max = 0
p = 0
for pos in range(len(s) - 1):
        if s[pos] <= s[pos + 1]:
            curMax += 1
        else:
            curMax = 0
        if Max < curMax:
            Max = curMax
            p = pos
if p:
    p += 1
print (s[p-Max:p + 1]) 