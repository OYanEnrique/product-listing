print(f'{"Product Pricing":^40}')

listing = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Pencil Case', 25.00, 'Protractor', 4.20, 'Compass', 9.99, 'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)

for pos in range(0, len(listing), 2):
#	print(listing[pos])
#	print(listing[pos +1])
	print(f'{listing[pos]:.<30} $ {listing[pos + 1]:>7.2f}')