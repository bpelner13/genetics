"""This contains the class for creatures created by the player"""

class creature():
    """This it the class for all creatures"""


    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)


    def __str__(self):
        traits = ', '.join([f"{k}: {v}" for k,v in self.__dict__.items() if k != "name"])
        return f"This creature is a {self.name} and has the properties: {traits}"
