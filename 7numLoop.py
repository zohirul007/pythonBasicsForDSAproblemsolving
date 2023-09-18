#loop odd number rules 2
# 1+3++5+...+100=?
sum = 0
for i in range(1, 101):
  if i%2 != 0: #(!= not equal)
    sum = sum + i
    print(sum)