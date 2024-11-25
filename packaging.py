
class Packaging:
    def init(self):
        if isinstance(self,Candy):
            self.packaging = "bag"
        elif isinstance(self,Cookie):
            self.packaging  = "box"
        elif isinstance(self,IceCream):
            self.packaging = "bowl"
        elif isinstance(self,Sundae):
            self.packaging = "boat"
        else:
            self.packaging = None