class Car:
    color = 'black'
    
    def __init__(self, year, model,price):
        self.year = year
        self.model = model
        self.price = price

    @staticmethod
    def  check_car_type(car_type):
        if car_type == 'sport':
            print ("Let's go racing")
        else:
            print("Slow down")
    @classmethod
    def ins_price(cls, year, price):
        f_price=year*price*0.123
        return f_price

#Car.check_car_type('sport')
car1=Car(2020, 'Model X', 100500)
# print(car1.color)
car2=Car(2022, 'Model Z', 200500)
# print(car2.color)

ins_price=car1.ins_price(2022, 100400)
print(ins_price)
