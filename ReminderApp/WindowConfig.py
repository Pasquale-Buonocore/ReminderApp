# Import useful data for Windows setting
from CustomFunctions import fromRGBtoList 

# Define configuration constants
win_width = 300
win_height = 400
win_left = 800 # 1230
win_top = 15 # 5
win_borderless = False
win_resizable = True
BackgroudColor = fromRGBtoList(rgb_list = [44,44,50,256])
DeadlineListColor = [255,150,50]

# Set windows config
from kivy.config import Config
Config.set('graphics', 'resizable', win_resizable)
Config.set('graphics', 'height', win_height)
Config.set('graphics', 'width', win_width)
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', win_left)
Config.set('graphics', 'top', win_top)
Config.set('graphics', 'borderless', win_borderless)


