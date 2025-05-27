class Main:
	def __call__(self, text, to_call = None):
		Main.side_effect("", text)
		if to_call:
			for ref in to_call:
				# A bound method will contain
				# the `__self__` property
				# referencing it's parent
				# class instance 
				try:
					if ref.__self__:
						ref("Hello, World")
				except AttributeError:
					ref("", "Hello, World")

	def entry(text):
		Main.side_effect("", text)

	def side_effect(self, text):
		print(f"{text}")
	

# Using the syntactic sugar for "emulating callable objects"
# by defining `__call__` on a class. This only works via an
# *instance*, since the first `()` on a class *always*
# constructs an instance—it does not invoke `__call__`.
Main()("Hello, World")	# Prints "Hello, World"

# No instantiation occurs here. We bypass the instance entirely
# by invoking the unbound method directly and supplying a dummy
# `self`. This only works because `self` is unused.
Main.__call__("", "Hello, World") # Prints "Hello, World"
Main.entry("Hello, World") # Prints "Hello, World"

# Prints address of the bound method suitable to be passed
# as a first class function
print(Main().__call__)	

# We can pass bounded or unbound methods to methods
# who themselves are either bound or unbound
# note the bound method implicitly performs a curry-like
# operation with `self`, the parent class instance
# Bound method:
Main()("Hello, World", [Main().side_effect, Main.side_effect])
# Unbound method:
Main.__call__("", "Hello, World", [Main().side_effect, Main.side_effect])
# Unbound method, taking the unbound method `__call__`
# internally calling itself with "Hello, World" 
Main.__call__("", "Hello, World", [Main.__call__])
