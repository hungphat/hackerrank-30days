def run(input, output):
    from abc import ABCMeta, abstractmethod
    class Book(object, metaclass=ABCMeta):
        def __init__(self, title, author):
            self.title = title
            self.author = author

        @abstractmethod
        def display(): pass

    #Write MyBook class
    class my_book(Book):                    # TODO the exercise told you that creating Clase MyBook(), I dont understand why you create a 'my_book'
                                            #      The Class name should be uppercase
        def __init__(self, title, author,  price):
            Book.__init__(self, title, author)
            self.price = price
        def display(self):
            print('Title: '+self.title)
            print('Autthor' +self.author)
            print('Price: ' + self.price)

    f = open(input, 'r')
    wr = open(output, 'w')
    title  = f.readline().rstrip('\n')
    author =f.readline().rstrip('\n')
    price  =f.readline().rstrip('\n')
    new_novel=my_book(title, author, price)
    new_novel.display()

if __name__ == '__main__':
    run('input.txt','output.txt')


