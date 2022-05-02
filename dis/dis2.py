# Q5: Make Keeper
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def do_keep(cond):
    	i = 1
    	while i <= n:
    		if cond(i):
    			print(i)
    		i += 1
    return do_keep


# Q8: Match Maker
def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
    	i = 0
    	while 10 ** (i + k) < x:
    		if (x // 10**i) % 10 != (x // 10 ** (i+k)) % 10:
    			return False
    		i += 1
    	return True
    return check
