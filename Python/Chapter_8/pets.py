def describe_pet(petname, animal='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal + ".")
    print("My " + animal + "\'s name is " + petname.title() + ".")

describe_pet('harry')
describe_pet('chester')
