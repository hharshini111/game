
screen main_menu():
    tag menu
    timer 0.0 action Start()

screen say(who, what):
    window:
        id "window"
        vbox:
            xalign 0.5
            ypos 0.8
            spacing 6
            if who is not None:
                text who id "who"
            text what id "what"

