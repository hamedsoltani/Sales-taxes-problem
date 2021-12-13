import numpy as np
import copy


class TaxModel():
    """

    """


    def __init__(self, items={}):

        # Load parameters
        self.selectedItem = items

    def taxDet(self, price, rate, type):
        tax = (price * type * rate) * 100
        if np.floor(tax) % 5 != 0:
            tax = (np.floor(tax) + (5 - np.floor(tax) % 5))
        return tax

    def calculateTax(self,exempt = []):
        for item in self.selectedItem:
            typeEf = 1
            if self.selectedItem[item]['type'] in exempt:
                typeEf = 0
            tax1 = self.taxDet(self.selectedItem[item]['price'], 0.1, typeEf)
            # tax1 = taxDet(self.selectedItem[item]['price']*typeEf*0.1)*100
            # if np.floor(tax1) % 5 != 0:
            #     tax1 = (np.floor(tax1) + (5 - np.floor(tax1) % 5))
            tax2 = self.taxDet(self.selectedItem[item]['price'], 0.05, self.selectedItem[item]['imported'])
            # tax2 = self.selectedItem[item]['price']*self.selectedItem[item]['imported']*0.05*100
            # if np.floor(tax2) % 5 != 0:
            #     tax2 = (np.floor(tax2) + (5 - np.floor(tax2) % 5))
            tax = (tax1 + tax2)/100
            self.selectedItem[item]['tax'] = round(tax*self.selectedItem[item]['count'],2)
            self.selectedItem[item]['wholePrice'] = round((self.selectedItem[item]['price'] + tax)*self.selectedItem[item]['count'],2)


        return self.selectedItem

    def printOut(self):
        totalTax = 0
        totalPrice = 0
        for item in self.selectedItem:
            print(self.selectedItem[item]['count'], ' ', self.selectedItem[item]['name'], ': ', format(self.selectedItem[item]['wholePrice'], '.2f'))
            totalTax = totalTax + self.selectedItem[item]['tax']
            totalPrice = totalPrice + self.selectedItem[item]['wholePrice']

        self.selectedItem['SalesTaxes'] = round(totalTax, 2)
        self.selectedItem['total'] = round(totalPrice, 2)
        print('Sales Taxes:',format(self.selectedItem['SalesTaxes'], '.2f'))
        print('Total:', format(self.selectedItem['total'], '.2f'),'\n')

