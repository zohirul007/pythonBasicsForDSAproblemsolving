#loop odd number rules 3
# 1+3++5+...+100=?
sum = 0
for i in range(1, 101, 2):
  sum = sum + i
print(sum)