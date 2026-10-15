username_block = "wG35yJwFr5FsRFrcAMkauQ=="
grade10_block = "Lg0Zm/uONlV4U3W2BnUgBg=="

result = f"{username_block} {grade10_block}"
print(result)

with open("result.txt", "w") as f:
    f.write(result + "\n")
