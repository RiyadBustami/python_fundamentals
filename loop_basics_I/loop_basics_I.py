# 1
for i in range(0, 151, 1):
    print(i)

# 2
for i in range(5, 1001, 5):
    print(i)

# 3
for i in range(1, 101, 1):
    out = ""
    if i % 5 == 0:
        out += "Coding"
        if i % 10 == 0:
            out += " Dojo"
    else:
        out = i
    print(out)
# 4
sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)
# 5
for i in range(2018, 0, -4):
    print(i)
# 6
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1, 1):
    if i % mult == 0:
        print(i)
