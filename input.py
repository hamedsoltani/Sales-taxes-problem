exemptTax = [1,2,3]
input = {
    #Type: book: 1, foods: 2, medical: 3, others: 0
	'factor1': {'item1': {'name': 'Book', 'count': 2, 'price': 12.49, 'type': 1, 'imported': 0},
                'item2': {'name': 'CD', 'count': 1, 'price': 14.99, 'type': 0, 'imported': 0},
                'item3': {'name': 'Chocolate bar', 'count': 1, 'price': 0.85, 'type': 2, 'imported': 0}},

    'factor2': {'item1': {'name': 'Imported box of chocolates', 'count': 1, 'price': 10.00, 'type': 2, 'imported': 1},
                'item2': {'name': 'Imported bottle of perfume', 'count': 1, 'price': 47.50, 'type': 0, 'imported': 1},
                },

    'factor3': {'item1': {'name': 'Imported bottle of perfume', 'count': 1, 'price': 27.99, 'type': 0, 'imported': 1},
                'item2': {'name': 'Bottle of perfume', 'count': 1, 'price': 18.99, 'type': 0, 'imported': 0},
                'item3': {'name': 'Packet of Headache pills', 'count': 1, 'price': 9.75, 'type': 3, 'imported': 0},
                'item4': {'name': 'Box of imported chocolates', 'count': 3, 'price': 11.25, 'type': 2, 'imported': 1}
                },

}