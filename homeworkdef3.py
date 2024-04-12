def print_params(a, b, c):
    print(a, b, c)
print_params(a = 1, b = 'string', c = True)
print_params(a = 'fklbjmlsnhjl;0', b = False, c = [1,'f',True])
#print_params(b = 25)

values_list = [(1,2,'open'), True, 1.234]
values_dict = {'a': '1', 'b': 1, 'c': True}
def print_params(a, b, c):
    print(a, b, c)
print_params(*values_list)
print_params(**values_dict)

def values_list_2(a=2, b='True'):
    print (a, b)
values_list_2(*values_list_2, 42)