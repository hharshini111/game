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
    show fox at char_left
    show ariel at char_right

    # Short dialogue intro using characters defined in separate files.
    fox "Hey Ariel, ready to try our new scene?"
    ariel "Absolutely, Fox. Keeping it simple with a basic chat."
    fox "Yup. Just us talking, then we demo the screens."
    ariel "Sounds good. You start."
    fox "Okay. Hello, player!"
    ariel "Hi there. Enjoy the minimal setup."

screen blank():
    add Solid("#000")
