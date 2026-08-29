n = 5

n = n + 2
print(n)

n += 5
print(n)

n *= 2
print(n)  # 24

# python executes the right hand side (RHS) first, so n + 1 => 24 + 1 = 25,
# and then runs the addition assignment operator a += RHS => 24 + 25 = 49
n += n + 1

print(n)  # 49
