
from animal import Animal
from dog import Dog


if __name__ == "__main__":
    # Create an instance of the Animal class
    animal = Animal(name="Generic Animal", species="Unknown Species")
    
    # Print the Animal instance
    print(animal)
    
    # Call the method to make a generic animal sound
    animal.speak()

    # Create an instance of the Dog class
    dog = Dog(name="Buddy", species="Canine", breed="Golden Retriever")
    
    # Print the Dog instance
    print(dog)
    
    # Call the method to make the dog-specific sound
    dog.speak()

    # Print out all the animals (Animal and Dog)
    print("\nAll Animals:")
    animals = [animal, dog]
    for a in animals:
        print(a)
