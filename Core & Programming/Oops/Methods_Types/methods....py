class A:
    @classmethod
    def cm(cls):
        print('Class Method')
    def im(self):
        print('Instance Method')
    @staticmethod
    def sm(x):
        print('Static method')
a1=A()
a1.cm()
a1.im()
a1.sm(10)
A.cm()
# A.im()
A.sm(2)
