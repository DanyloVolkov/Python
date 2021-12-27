from functools import wraps

def type_logger(func):
   @wraps(func)
   def class_wrapper(a):
      result = func(a)
      print(f'{a}: {type(a)}, {func.__name__}')
      return result
   return class_wrapper

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
print(a)