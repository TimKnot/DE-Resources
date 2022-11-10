import time

class Coffee():
    def __init__(self, bean_type):
        self.bean_type = bean_type
    
    def describe(self):
        print(f"A lovely fresh pot of {self.bean_type} coffee")
        
class Beans():
    def __init__(self, bean_type):
        print(f"Getting some {bean_type} beans...")
        time.sleep(2)
        self.bean_type = bean_type
        
class Grinder():
    def grind(self, bean: Beans):
        print(f"Grinding the {bean.bean_type} beans...")
        time.sleep(2)
        return Grounds(bean.bean_type)
    
class Grounds():
    def __init__(self, bean_type):
        self.bean_type = bean_type
        
class Brewer():
    def brew(self, grounds: Grounds) -> Coffee:
        print("Adding hot water...")
        time.sleep(2)
        print("Your coffee is nearly ready...")
        time.sleep(2)
        return Coffee(grounds.bean_type)

class CoffeeMachine():
    def brew_coffee(self, bean_type) -> Coffee:
        
        # Get the right beans
        beans = Beans(bean_type)
        
        # Grind the beans to get grounds
        grinder = Grinder()
        grounds = grinder.grind(beans)
        
        # Brew the grounds to get coffee
        brewer = Brewer()
        coffee = brewer.brew(beans)
        
        return coffee