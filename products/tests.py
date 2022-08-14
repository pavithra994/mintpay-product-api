from django.test import TestCase

# Create your tests here.
# import csv
#
# from products.models import Product
#
# with open('products.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         # product_SKU,brand_name,product_slug,product_title,quantity
#
#         # print(f'\t{row}.')
#         obj = Product(**row)
#         obj.save()
#         line_count += 1
#     print(f'Processed {line_count} lines.')