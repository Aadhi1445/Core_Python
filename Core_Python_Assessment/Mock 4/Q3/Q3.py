class Artwork:
    def __init__(self,t,a,p):
        self.title=t
        self.artist=a
        self.price=p
    def __str__(self):
        return (f'Artwork Title : "{self.title}"\n'
                f'Artist Name : "{self.artist}"\n'
                f'Artwork Price : "{self.price}"')
    def __repr__(self):
        return (f'Artwork Title : "{self.title}"')
    def __add__(self, other):
        return f'Combined of "{self.title}" & "{other.title}" Artworks :-- {self.price+other.price}'
    def __lt__(self, other):
        if self.price<other.price:
            return f'"{self.title}" price  is Less than "{other.title}" price '
        else:
            return f'"{self.title}" price is not less than "{other.title}" price '
a1=Artwork('Sun','Shiva',400)
a2=Artwork('Moon','Saii',800)
a3=Artwork('Solar system','Satwik',600)
print(a1)
print()
print(a2)
print()
print(a3)
print()
print(a1.__repr__())
print(a2.__repr__())
print(a3.__repr__())
print()
print(a1+a2)
print(a3+a2)
print(a1+a3)
print()
print(a1<a2)
print(a3<a1)
print(a2<a3)