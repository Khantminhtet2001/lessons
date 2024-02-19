#decorator
def greet(fun):
    def wrapper(name):
        #before
        print('hello')
        fun(name)
        #after
        print('good bye')
        
    return wrapper

@greet
def sayName(name):
    print(name)


sayName('Khant Min Htet')