# -*-coding:utf-8-*-
#!/usr/bin/env python

from OOP_pro.Property_pro.get_valid import get_valid_input

class Property:
    def __int__(self,square_feet='',bedroom='',bathroom='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = bedroom
        self.num_bathrooms = bathroom

    def display(self):
        print("PROPERTY DETALLS")
        print("================")
        print("square footages: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_bathrooms))
        print()

    def prompt_init():
        '''声明一个静态方法 所以不需要self参数'''
        return dict(
                    square_feet = input("Enter the square feet: "),
                    bedrooms=input("Enter number of bedrooms: "),
                    bathrooms = input("Enter number of bathsrooms: ")
        )

    prompt_init=staticmethod(prompt_init)


class Apartment(Property):
    valid_laundries = ("coin","ensuite","none")   #是否含有卫生间
    valid_balconies = ("yes","no","solarium")       #是否含有阳台

    def __init__(self,balcony = '',laundry='',**kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETALLS ")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)


        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("what laundry facilities does the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))

        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony?"
                "({})".format(", ".join(Apartment.valid_balconies))
            )

        parent_init.update(
            {
                "laundry":laundry,
                "balcony":balcony
            }
        )
        return parent_init
    # prompt_init = staticmethod(prompt_init)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have",Apartment.valid_laundries
        )

        balcony = get_valid_input(
            "Does the property have a balcony ",
            Apartment.valid_balconies
        )

        parent_init.update({
            "laundry":laundry,
            "balcony":balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

class House(Property):
    valid_garage=("attached","detached","none")  #是否含有车库
    valid_fenced = ("yes","no")                     #是否含有围栏

    def __init__(self,num_stories='',
                 garage='',fenced='',**kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETALLS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()    # 父类初始化
        fenced = get_valid_input(
            "Is the yard fenced? ",
            House.valid_fenced
        )
        garage = get_valid_input(
            "Is there a garage? ",
            House.valid_garage

        )

        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced":fenced,
            "garage":garage,
            "num_stories":num_stories
        })
        return parent_init


    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self,price='',taxes='',**kwargs):
        super().__init__(**kwargs)     # 初始化 房屋购买价格和纳税额
        self.price =price
        self.taxes = taxes

    def desplay(self):
        super().display()
        print("PURCHASE DATALLS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )

    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self,furnished='',utilities='',rent='',**kwargs):
        super().__init__(**kwargs)     #初始化 家具,公共设施,租金
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("RENTAL DETALLS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input(
                "Is the property furnished? ",("yes","no")
            )
        )
    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental,House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase,House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    def __init__(self):
        self.property_list = []
    def display_properties(self):
        for property in self.property_list:
            property.display()