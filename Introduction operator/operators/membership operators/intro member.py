# membership operators========== 9 0ct 2026==========
#====================================================================

name = "hello"

# in
print("h" in name) # true
print("z" in name) # false
print("H" in name) # false capital H means wrong case snsitive
print("llo" in name) # true
print("lllo" in name) # false  only have llo no continues lllo in name

# not in

print("e" not in name) # false bzc there is e
print("lo" not in name) # false there is lo