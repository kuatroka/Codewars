"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
containing distinct letters, - each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

"""

def longest(a1, a2):
    print a1
    print a2
    print 'set', set(a1 + a2) # set() will create a set of unique letters in the string
    print 'sorted', sorted(set(a1 + a2)) # sorted() - sorts characters
    print 'final', "".join(sorted(set(a1 + a2))) # "".join() will join the letters back to a string in arbitrary order.


longest("loopingisfunbutdangerous", "theresapairoffunctions")



