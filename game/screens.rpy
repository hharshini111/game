screen minimal_screen():
    add Solid("#202020")

    vbox:
        align (0.5, 0.5)
        spacing 20

        add Solid("#ffffff") xsize 300 ysize 200

        textbutton "Go to Circle":
            action Return("circle")

        textbutton "Quit":
            action Return("quit")

screen main_menu():
    tag menu
    timer 0.0 action Start()

screen circle_screen():
    add Solid("#202020")

    vbox:
        align (0.5, 0.5)
        spacing 20

        text "\u25CF":
            size 220
            color "#ffffff"
            xalign 0.5
            yalign 0.5

        textbutton "Back to Image":
            action Return("minimal")

