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
