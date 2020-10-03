class SingletonType(type):
    _instance = None

    def __call__(self, *args, **kwargs):        
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
    
        return self._instance


class TestClass(metaclass=SingletonType):
    def __init__(self):
        print('__init__ called.')


if __name__ == "__main__":
    s1 = TestClass()
    s2 = TestClass()

    if s1 is s2:
        print("It works. Got same object")
    else:
        print("Failure. It's not same object")

