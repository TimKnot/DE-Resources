# Define a class Animal which outlines things that every animal can do.
class Animal():
    favourite_food = "Animal Feed"

    # All animals eat so we can define it on the Animal class.
    def eat(self):
        print("Mmmmmm today Im eating " + self.favourite_food)


# A wolf inherits from Animal because a Wolf is a specific type of Animal.
class Wolf(Animal):
    # This favourite_food variable overrides the favourite_food on Animal.
    favourite_food = "The 3 Little Piggies"

    def howl(self):
        print("Ah-wwwwwwwhooooooo")


# Instantiate a Wolf.
the_big_bad_wolf = Wolf()
# A wolf can howl because it has the function howl in it.
the_big_bad_wolf.howl()
# The wolf can also eat because it is an Animal.
the_big_bad_wolf.eat()

print(Animal.favourite_food)

# Program outputs:
# Ah-wwwwwwwhooooooo
# Mmmmmm today Im eating The 3 Little Piggies
