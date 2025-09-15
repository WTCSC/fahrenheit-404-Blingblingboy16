temp_unit = input("Please enter the unit you want to convert from (only do C or F, else i panic)")
temp = input("Whats the degree in " + temp_unit + " you want to convert?")

if temp_unit == "C":
    c_temp_int = int(temp)
    result = c_temp_int * 1.8 + 32
    print(result)
if temp_unit == "F":
    f_temp_int  = int(temp)
    result = f_temp_int - 32 / 1.8
    print(result)
else:
    (print("i scawed"))

