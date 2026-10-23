class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        self.__balance=amount
        return self.__balance

