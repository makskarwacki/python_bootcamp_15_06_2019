import re

text = """17-120 17-121 17-122 131-123 12-123 ..@..pl"""

pattern_zip_code = re.compile("(^| )(\d{2}-\d{3})")
pattern_email = re.compile("[a-z0-9.\-]*@[a-z0-9.\-]*\.\w{2,4}")
pattern_date = re.compile("\d{2} \w{3} \d{4}"
                          )
with open("input.txt") as f:
    text = f.read()
    print(pattern_zip_code.findall(text))
    print(pattern_email.findall(text))
    print(pattern_date.findall(text))

# print(pattern.findall(text))
# x = pattern.search(text, 6)
# print(x.span())
#
# start = 0
# while True:
#
#     x = pattern.search(text, start)
#     if x:
#         start = x.span()[1]
#         print(x.group())
#     else:
#         break
#
#
#
