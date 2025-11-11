class List:
    def __init__(self, itens = []):
        self.__itens = itens
        
    def isEmpty(self):
        if len(self.__itens) == 0:
            return print('empty')
        return print('not empty')
        
    def add(self, item):
        if self.__itens.isEmpty():
            return print('empty list')
        return self.__itens.append(item)
    
    def print_list(self):
        if self.__itens.isEmpty():
            return print('empty list')
        else:
            for i in range (self.__itens):
                print (self.__itens[i])            

#Main program
l = List()


l.add(1)
l.print_list()
l.add('Homework')
l.print_list




            
        
    
