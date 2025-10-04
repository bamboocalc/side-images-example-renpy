# Place this in an "init python" block
###############################################################################

init python:
    previous_speaker = None
    current_speaker = None

    def preload_speaker_assets(who):
        if who is None:
            return

        # Try to preload talk image
        talk_image_path = f"images/talk_{who}.png"
        if renpy.loadable(talk_image_path):
            renpy.cache_pin(talk_image_path)

        # Try to preload side image
        side_image_path = f"images/{who}_side.png"
        if renpy.loadable(side_image_path):
            renpy.cache_pin(side_image_path)

        # Also quote image if needed
        quote_image_path = "images/quote.png"
        if renpy.loadable(quote_image_path):
            renpy.cache_pin(quote_image_path)

# Place this in your screens.rpy file, so that it replaces your existing "screen say(who, what)"
###############################################################################

screen say(who, what):

    on "show" action [
        SetVariable("previous_speaker", current_speaker),
        SetVariable("current_speaker", who),
        Function(preload_speaker_assets, who)
    ]

    # This is logic for displaying a background image behind the character
    if renpy.loadable(f"talk_{who}.png", directory="images"): 
        if previous_speaker != current_speaker:
            add "images/talk_[who].png" at bg_fadein # The backround image fades in on the character's first dialogue block
        else:
            add "images/talk_[who].png" at bg_rest
    
    if previous_speaker != current_speaker:
        add SideImage() xalign 0.0 yalign 1.0
    else:
        add SideImage() xalign 0.0 yalign 1.0 at jumper # The character does a little bounce for each dialogue block they have

    # This is logic for displaying a speech bubble next to the character image
    if renpy.loadable(f"talk_{who}.png", directory="images"):
        if previous_speaker != current_speaker:
            add "images/quote.png" at quote_slide # The speech bubble slides in on the character's first dialogue block
        else:
            add "images/quote.png" at quote_rest

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

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

transform quote_slide:
    xoffset -400
    yalign 1.0
    alpha 0
    pause 0.2
    ease 0.4 xoffset 0 alpha 1

transform quote_rest:
    yalign 1.0
    xoffset 0
    alpha 1

transform bg_fadein:
    xalign 0.0
    alpha 0.0
    ease 0.5 alpha 0.5

transform bg_rest:
    xalign 0.0
    alpha 0.5

transform jumper:
    ease 0.1 yzoom 1.08
    ease_back 0.2 yzoom 1.0

###############################################################################


# Make sure you define an "image side _______" for every character who you want a side image for.
# Here is an example of what that might look like:
###############################################################################

layeredimage grant:
    group arms:
        attribute point:
            Image("images/grant/grant_point.png")
        attribute bag default:
            Image("images/grant/grant_bag.png")
    group face:
        attribute sus:
            Image("images/grant/grant_sus.png")
        attribute despair:
            Image("images/grant/grant_despair.png")
        attribute happy:
            Image("images/grant/grant_happy.png")
        attribute horrified:
            Image("images/grant/grant_horrified.png")
        attribute jokester:
            Image("images/grant/grant_jokester.png")
        attribute serious:
            Image("images/grant/grant_serious.png")
        attribute ponder:
            Image("images/grant/grant_ponder.png")
        attribute neutral default:
            Image("images/grant/grant_neutral.png")
        attribute what:
            Image("images/grant/grant_what.png")
        attribute worried:
            Image("images/grant/grant_worried.png")

image side grant = LayeredImageProxy("grant", Transform(crop=(325,-150,900,1350),zoom=1.5))

define grant = Character("Grant", image='grant', color="#556c9f")
