class SingletonType(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):        
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
    
        return self._instance


class ClassOne(metaclass=SingletonType):
    def __init__(self):
        print('ClassOne __init__ called.')


class ClassTwo(metaclass=SingletonType):
    def __init__(self):
        print('ClassTwo __init__ called.')


if __name__ == "__main__":
    o1 = ClassOne()
    o2 = ClassTwo()
    o3 = ClassOne()

    assert o1 is o3, "o1 and o3 should be same object"
    assert o1 is not o2, "o1 and o2 shouldn't be same object"
    
    print('Success!')


    
