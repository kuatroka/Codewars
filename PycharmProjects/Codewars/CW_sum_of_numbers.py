## my implementation

# def get_sum(a,b):
#     total = []
#     if a == b:
#          return a
#
#     elif a > b:
#         return sum(range(b, a + 1))
#
#
#     else:
#
#         return sum(range(a, b + 1))
#
#
# print(get_sum(-1, 4))

## the best one

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))

print(get_sum(-1, 4))