class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        list_file = open(self.__file_name, 'r')
        adding = list_file.read()
        list_file.close()
        return adding


    def add(self, *products):
        file1 = open(self.__file_name, 'a')
        for_adding = self.get_products()
        for i in products:
            if i.name not in for_adding:
                file1.write(str(p1)), file1.write('\n'), file1.write(str(p2)), file1.write('\n'), file1.write(str(p3)),
                file1.write('\n'), file1.write(str(p4)), file1.write('\n')
                return
            else:
                print(f'Продукт {i} уже есть в магазине')
        file1.close()
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Banana', 43.7, "Fruits")
print(p2)
s1.add(p1, p2, p3, p4)
s1.get_products()
