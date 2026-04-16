letter="""Dear {NAME} ,you are selected! {DATE} ."""

# a=letter.format("mrs.")
# print(a)

# b=letter.format("mrs.","we","suspended.")
# print(b)

                #   0      1       2
# c=letter.format("mrs.","we","suspended.")
# print(c)

name=input("enter the name:")
date=input("enter the date:")

d=letter.format(NAME=name,DATE=date)
print(d)