class Product:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

product1 = Product()

name, code = input().split()

product2 = Product(name, int(code))

print('product {} is {}'.format(product1.code, product1.name))
print('product {} is {}'.format(product2.code, product2.name))