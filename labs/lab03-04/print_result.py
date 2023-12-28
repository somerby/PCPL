def print_result(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        if type(func_result) == list:
            print(f'{func.__name__}\n' + '\n'.join([str(i) for i in func_result]))
        elif type(func_result) == dict:
            print(f'{func.__name__}\n' + '\n'.join([f'{i} = {func_result[i]}' for i in func_result]))
        else:
            print(f'{func.__name__}\n{func_result}')
        return func_result
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()