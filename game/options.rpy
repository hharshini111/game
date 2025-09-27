define config.name = _("sacrifice")
define config.version = "0.0.1"
define build.name = "sacrifice"

# Boot straight into the game without a main menu.

# Keep the dialogue window hidden; we are using a single custom screen.
define config.window = "hide"

# Disable transitions to keep it minimal.
define config.enter_transition = None
define config.exit_transition = None
define config.intra_transition = None
define config.after_load_transition = None
define config.end_game_transition = None

# Minimal save directory name.
define config.save_directory = "sacrifice-min"
## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("sacrifice")
define config.version = "1.0"
define build.name = "sacrifice"

define config.window_icon = None
#define config.main_menu_screen = None
define config.end_game_transition = None
define config.after_load_transition = None
define config.enter_transition = None
define config.exit_transition = None
define config.intra_transition = None
define config.window = "hide"

default preferences.text_cps = 0
default preferences.afm_time = 15

define config.save_directory = "sacrifice-minimal"
