from abc import ABC, abstractmethod

class Phone(ABC):  # Phone is an abstract class because it contains an abstract method
    @abstractmethod
    def call_friend(self): # Abstract method call_friend
        pass

# Smart phone inherits from phone because its a kind of phone.
class SmartPhone(Phone):
    # SmartPhone must have the call_friend function defined on it because its marked as an @abstractmethod
    def call_friend(self):
        print("Hi friend I'm calling from my Smart phone!")

class LandLinePhone(Phone):
    def call_friend(self):
        print("Hi friend I'm calling from my LandLine phone!")

class BurnerPhone(Phone):
    def call_friend(self):
        print("Hi friend I'm calling from my Burner phone!")

# arrange birthday party uses a phone, but it doesn't matter what kind of phone you use.
# All that matters is you can use it to call a friend.
def arrange_birthday_party(p: Phone):
    p.call_friend()

s = SmartPhone()
arrange_birthday_party(s)

l = LandLinePhone()
arrange_birthday_party(l)

b = BurnerPhone()
arrange_birthday_party(b)
