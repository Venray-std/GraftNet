class Test(object):
    name = 'stephen'

    """docstring for Test"""
    """
    def __init__(self, arg=None):
        super(Test, self).__init__()
        self.arg = arg
    """
    def say_hi(self):
        print ('[1]hello wrold')


    @staticmethod
    def say_bad():
        args = 2
        print (args)
        print ('[2]say bad')
        print ('[3]Test.name:%s'%Test.name) 
        Test().say_hi()

    @classmethod
    def say_good(cls):
        # args = 3
        print (args)
        print ('[4]say good')
        print ('[5]cls.name:%s'%cls.name) 
        cls.say_bad() 
        cls().say_hi()  

def main():
    Test.say_bad()
    print ("----------------------------------")
    Test.say_good()

if __name__ == '__main__':
    main()