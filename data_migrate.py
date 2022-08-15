import csv

from products.models import Product

with open('products.csv', mode='r') as csv_file:
    fieldnames = ["product_SKU", "brand_name", "product_slug", "product_title", "quantity"]
    csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames)

    for row in csv_reader:
        _product = {k:v.strip() for k,v in row.items()} # removing white spaces
        print(f'\t{_product}.')
        obj = Product(**_product)
        obj.save()

    # product_SKU, brand_name, product_slug, product_title, quantity
