from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle

def fromRGBtoList(rgb_list):
    return [color / 256 for color in rgb_list]

############
# Constant #
############
DeadlineListColor = [255,150,50]
BackgroudColor = fromRGBtoList(rgb_list = [44,44,50,256])
win_width = 400
win_height = 400

# **************************** DEFINE CLASSES FOR THE i-th TASK ****************************
class DealLineClass(Widget):
    # This class define a widget that contains all the infos for a determined task

    def __init__(self,task_name = '', pos = (0,0), exp_date = '---', status = '---', **kwargs):
        # Call superclass init function
        super(DealLineClass,self).__init__(**kwargs)

        # Define constant string
        self.Widsize = (300, 50)
        self.DeadLine_name_str = 'TASK NAME'
        self.DeadLine_ExpireDate_str = 'EXPIRATION DATE'
        self.DeadLine_Status_str = 'STATUS'

        # Define the canvas properties to show
        with self.canvas:
            #\ Main Rect definition \#
            rgb_wid = fromRGBtoList(DeadlineListColor)
            Color(rgb_wid[0],rgb_wid[1],rgb_wid[2])
            Deadline_board = RoundedRectangle(pos = pos, size = self.Widsize)

            #\ Fixed labels \#
            Deadline_name = Label(text = self.DeadLine_name_str,
                                  size = (len(self.DeadLine_name_str ),0), 
                                  color = (0,0,0), font_size = 10, bold = True, 
                                  pos = (Deadline_board.pos[0] + 30 , Deadline_board.pos[1] + Deadline_board.size[1] - 10))

            Deadline_ExpireDate = Label(text = self.DeadLine_ExpireDate_str,
                                        size = (len(self.DeadLine_ExpireDate_str ),0),
                                        color = (0,0,0), font_size = 10, bold = True,
                                        pos = (Deadline_board.pos[0] + 180 , Deadline_board.pos[1] + Deadline_board.size[1] - 10))

            Deadline_ExpireDate = Label(text = self.DeadLine_Status_str,
                                        size = (len(self.DeadLine_Status_str),0),
                                        color = (0,0,0), font_size = 10, bold = True,
                                        pos = (Deadline_board.pos[0] + 260 , Deadline_board.pos[1] + Deadline_board.size[1] - 10))

            #\ Information from DB \#
            Deadline_task_name = Label(text = task_name,
                                       color = (0,0,0),
                                       size = (200,13),
                                       text_size = (200,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (Deadline_board.pos[0] + 5, Deadline_board.pos[1] + 10),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )

            Deadline_task_exp_date = Label(text = exp_date,
                                       color = (0,0,0),
                                       size = (100,13),
                                       text_size = (100,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (Deadline_board.pos[0] + 150, Deadline_board.pos[1] + 10),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )
            
            Deadline_task_status = Label(text = status,
                                       color = (0,0,0),
                                       size = (100,13),
                                       text_size = (100,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (Deadline_board.pos[0] + 250, Deadline_board.pos[1] + 10),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )