from functools import wraps

def val_checker(lam_func):
   def value_checker(func):
      @wraps(func)
      def wrapper(number):
         if lam_func(number):
            print(func(number))
         else:
            raise ValueError (f'Неверное значение: {number}')
      return wrapper
   return value_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
