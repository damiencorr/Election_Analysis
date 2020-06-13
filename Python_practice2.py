products = ['Ball', 'Book', 'Chess set', 'Crayons', 'Doll', 'Play-Doh']
    
def product_len(product):
    return len(product)

print('\n',products)
print('\n',product_len(products))
products.sort(key = product_len)
print('\n',products)
products.sort(reverse = True, key = product_len)
print('\n',products)