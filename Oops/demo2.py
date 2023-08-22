class parent:
    def vehicles(self):
        self.context=["passion pro","swift"]
        return self.context
    
class child(parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("hunder")
        return self.context
c=child()
print(c.vehicles())    