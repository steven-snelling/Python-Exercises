patterns = {
    "empid": "^[A-Z][0-9]{3}$",
    "gender": "^[M|F]$",
    "age": "^[0-9]{2}$",
    "sales": "^[0-9]{3}$",
    "bmi": "^Normal|Overweight|Obesity|Underweight$",
    "salary": "^[0-9]{2,3}$",
    "birthday": "^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$"
}


raw = [""]*10

raw[0] ="Laurie"
raw[2] = "Steve"
for name in raw:
    print(name)
#
# i = 0
# for key in patterns.keys():
#
#     print(key)
#     pat = patterns[key]
#     val = raw[i]
#     if pat matches val:
#         then we are good
#     else:
#         show error on specific key that failed
#     i++