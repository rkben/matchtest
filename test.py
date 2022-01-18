# Function gen
# for x in range(0, 1000):
#    print(f"def func{x}() -> None:\n    return")

# Dict gen
# print("from funcs import *")
# print("func_dict = {")
# for x in range(0, 1000):
#     print(f"{x}: func{x},")
# print("}")


# if else
# print("if x == 0:")
# print("    func0()")
# for x in range(1, 1000):
#     if x > 0:
#         print(f"elif x == {x}:")
#         print(f"    func{x}()")

print("match x:")
for x in range(1, 1000):
    print(f"    case {x}:")
    print(f"        func{x}()")

print("    case _:")
print("        return")
