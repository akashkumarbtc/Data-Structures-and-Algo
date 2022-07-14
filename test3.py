"""
3(ab)4(cd)
"""

# s = "3(a2(c))"

# stack = []
# for i in s:
#     if i != ')':
#         stack.append(i)
#     else:
#         pattern = ""

#         while stack[-1].isalpha():
#             pattern = stack.pop() + pattern

#         stack.pop()

#         intval = ""
#         while stack and stack[-1].isdigit():
#             intval   = stack.pop() + intval

#         res = pattern * int(intval) 
#         for x in res:
#             stack.append(x)


# print(*(stack), sep="")

"""
 Input: n = "218765" 
 258761
Output: "251678" 
  
 Input: n = "1234" 
 Output: "1243" 
4321
 """

stack = []

s = "218765"

for i in s:
    stack.append(int(i))

print(stack)

res = []
is_unorder = False
while stack:
    val = stack.pop()

    if res and  val < res [0] and not is_unorder:
        is_unorder = True
        res.insert(0, val)
        for  i in range(len(res) -1, 0, -1):
            if res[i] > val:
                res[0], res[i] = res[i], res[0]
                break

        first = res[0]
        res = res[1:]
        res = res[::-1]
        res.insert(0, first)

    else:
        res.insert(0, val)

print(res)