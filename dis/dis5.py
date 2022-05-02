def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    result = []
    for elem in seq:
    	result += [fn(elem)]
    return result


def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    result = []
    for elem in seq:
    	if pred(elem):
    		result += [elem]
    return result


def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    total = seq[0]
    for elem in seq[1:]:
    	total = combiner(total,elem)
    return total



class Button:
	def __init__(self,pos,key):
		self.pos = pos
		self.key = key
		self.times_pressed = 0

class Keyboard:
	"""A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """

    def __init__(self,*args):
    	self.buttons = {}
    	for button in args:
    		self.buttons[button.pos] = button

    def press(self, info):
    	if info in self.buttons.keys():
    		b = self.buttons[info]
    		b.times_pressed += 1
    		return b.key
    	return ''

    def typing(self,typing_input):
    	accumulate = ''
    	for pos in typing_input:
    		accumulate += self.press(pos)
    	return accumulate