def test_inner(x):
    def inner_func(y, z = 'A'):
        print(f'{x}, {y}, {z}')
    return inner_func

moj_test = test_inner('aaaa2')

moj_test('22','adsadds')