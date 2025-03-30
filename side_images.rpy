

# Place this in your screens.rpy file, so that it replaces your existing "screen say(who, what)"
###############################################################################

screen say(who, what):

    if renpy.loadable(f"talk_{_last_say_who}.png", directory="images"):
        add "images/talk_[_last_say_who].png" at fadein

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if renpy.loadable(f"{_last_say_who}_side.png", directory="images"):
        add SideImage() xalign 0.0 yalign 1.0

    if renpy.loadable(f"talk_{_last_say_who}.png", directory="images"):
        add "images/quote.png" at quoteslide

###############################################################################




# Place this in your script.rpy file (or anywhere, really)
###############################################################################

transform hideside(old, new):
    contains:
        old
        alpha 1
        yalign 1.0
        xoffset 0
        ease 0.3 xoffset -900 alpha 0
    contains:
        new
        alpha 0
        yalign 1.0
        xoffset -900
        ease 0.3 xoffset 0 alpha 1

define config.side_image_change_transform = hideside

transform quoteslide:
    yalign 1.0
    xoffset -400
    alpha 0
    pause 0.2
    ease 0.4 xoffset 0 alpha 1

transform fadein:
    xalign 0.5
    yalign 1.0
    alpha 0.0
    ease 0.5 alpha 0.5

###############################################################################


# Make sure in your script.rpy file, you define an "image side _______" for every character who you want a side image for.
# Here is an example of what that might look like:
###############################################################################

image side grant = "images/grant_side.png"
image side lana = "images/lana_side.png"
image side burns = "images/burns_side.png"

image grant = "images/grant.png"
image lana = "images/lana.png"
image burns = "images/burns.png"

define grant = Character("Grant", image='grant', color="#556c9f")
define lana = Character("Lana", image="lana", color="#00ff55")
define burns = Character("Burns", image="burns", color="#b90000")