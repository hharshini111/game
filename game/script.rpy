define alice = Character("Alice", color="#c8ffc8", image="alice")
define bob = Character("Bob", color="#c8c8ff", image="bob")
define fox = Character("Fox", color="#ff7f50", image="fox")
define ariel = Character("Ariel", color="#ffa500", image="ariel")
define gerald = Character("Gerald", color="#98fb98", image="gerald")
define computer = Character("Computer", color="#87cefa", image="computer")
define carpet = Character("Carpet", color="#d2b48c", image="carpet")
define nicky = Character("Nicky", color="#ff69b4", image="nicky")
define acorn = Character("Acorn", color="#8b4513", image="acorn")
define hidee = Character("Hidee", color="#9370db", image="hidee")

label start:
    scene black

    # Show character placeholders explicitly. This is the standard way.
    show alice at char_left
    show bob at char_right

    # Short dialogue intro using characters defined in separate files.
    alice "Hey Bob, ready to try our new scene?"
    bob "Absolutely, Alice. Keeping it simple with a basic chat."
    alice "Yup. Just us talking, then we demo the screens."
    bob "Sounds good. You start."
    alice "Okay. Hello, player!"
    bob "Hi there. Enjoy the minimal setup."

screen blank():
    add Solid("#000")
