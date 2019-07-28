class mynumber:
    def __init__(self,value):
        self.data=value
    def __str__(self):
        return 'ｈｅｌｌｏ'
    def __repr__(self):
        return 'ｗｏｒｌｄ'
n1=mynumber(100)
n2=mynumber(200)
print(repr(n1))
print(str(n1))