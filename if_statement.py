is_male = True
is_tall = True

# or, and, elif, and not
if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("You are a short male")
elif not is_male and (is_tall):
    print("You are not a male but are tall")
else:
    print("You neither male or tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(345 ,23523, 235))
