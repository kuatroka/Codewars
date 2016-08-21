# my code
def mango(quantity, price):
    #
    # mod = quantity % 3
    # print(mod)
    # even = quantity - mod
    # print(even)
    # even_price = ((quantity - (quantity % 3)) / 3) * 2 * price
    # mod_price = (quantity % 3) * price
    return int((((quantity - (quantity % 3)) / 3) * 2 * price) + ((quantity % 3) * price))
# test.assert_equals(mango(3, 3), 6)
# test.assert_equals(mango(9, 5), 30)
print(mango(10, 5))

# best practices solution. it uses floor division and in the end it multiplies the number of "needed" mangoes by price
# the number by which we do the floor division is the number of "supermarket offer" in this case - 3 for 2.
# we take 3 but pay for 2 mangoes. Floor division brings only the whole part after division, leaving out the decimals
def mango(quantity, price):
    return (quantity - quantity // 3) * price
print(mango(12, 2))

# below is another "smart solution" with lambda
"""
mango=lambda q,p:q//3*2*p+q%3*p
"""
mango=lambda q,p:q//3*2*p+q%3*p
print(mango(10,5))





