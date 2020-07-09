s = 'azcbobobegghakl'

total = 0
for pos in range(len(s) - 2):
    if "bob" == s[pos:pos+3]:
        total += 1

print ("Number of times bob occurs is:", total)