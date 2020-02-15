class Vehicle(object):
    engine, passengers, doors, fuel_vol = "", "", "", ""

    def __init__(self):
        print("Created Vehicle")
        pass


class Car(Vehicle):
    wheels = ""

    def __init__(self):
        super().__init__()
        print("Created Car")

    def get_car(self):
        c = self
        return {"engine": c.engine,
                "passengers": c.passengers,
                "doors": c.doors,
                "fuel_vol": c.fuel_vol,
                "wheels": c.wheels}


class Plane(Vehicle):
    wings = ""

    # If you uncomment this method and comment the print on line 36 you'll see how __init__ is processed when
    # inheritance is in play and how the interpreter prioritises classes
    def __init__(self):
        super().__init__()
        print("Created Plane")
    """ """
    print("Created Plane")

    def get_plane(self):
        p = self
        return {"engine": p.engine,
                "passengers": p.passengers,
                "doors": p.doors,
                "fuel_vol": p.fuel_vol,
                "wheels": p.wings}


vh = Vehicle()
vh.engine = "good one"
car = Car()
plane = Plane()  # <-- notice the position of this method call in the terminal output
plane.fuel_vol = "lots"


print(plane.get_plane())




