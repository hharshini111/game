init python:
    def placeholder_card(name: str, width: int = 480, height: int = 720, bg: str = "#202020", fg: str = "#ffffff", size: int = 72):
        base = Fixed(
            Transform(Solid(bg), xsize=width, ysize=height),
            Text(name, size=size, color=fg, xalign=0.5, yalign=0.5),
        )
        return Transform(base, anchor=(0.5, 1.0))

transform char_left:
    xalign 0.18
    yalign 1.0

transform char_right:
    xalign 0.82
    yalign 1.0

image fox = placeholder_card("Fox")
image ariel = placeholder_card("Ariel")
image gerald = placeholder_card("Gerald")
image computer = placeholder_card("Computer")
image carpet = placeholder_card("Carpet")
image nicky = placeholder_card("Nicky")
image acorn = placeholder_card("Acorn")
image hidee = placeholder_card("Hidee")
image alice = Fixed(
    Transform(Solid("#333"), xsize=400, ysize=600),
    Text("Alice", size=64, color="#ffffff", xalign=0.5, yalign=0.5),
)

image bob = Fixed(
    Transform(Solid("#333"), xsize=400, ysize=600),
    Text("Bob", size=64, color="#ffffff", xalign=0.5, yalign=0.5),
)

