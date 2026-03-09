class Car:
    class_variable=2029
    def __init__(self,model,year, color, for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def display(self):
        print(self.model)
        print(self.year)
        print(self.color)
        print(self.for_sale)
    def drive(self):
        print("drivaing car")