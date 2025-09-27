label start:
    scene black

    while True:
        $ result = renpy.call_screen("minimal_screen")

        if result == "circle":
            $ back = renpy.call_screen("circle_screen")
            if back == "minimal":
                pass
        elif result == "quit":
            return

screen blank():
    add Solid("#000")
