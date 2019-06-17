var01 = "python is good language"

var01_split = var01.split()
print(var01_split, type(var01_split))

var01_replace = var01.replace('o', '0')
print(var01_replace)

if "o" in var01:
    print("o exist in var01")
else:
    print("o not exist in var01")
