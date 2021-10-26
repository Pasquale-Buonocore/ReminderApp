from WindowConfig import * # sets the windows configuration
from CustomFunctions import fromRGBtoList # returns the normalized RGB list
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line, Rectangle, RoundedRectangle
from kivy.properties import StringProperty, ReferenceListProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image
import random


# **************************** DEFINE CLASSES FOR THE i-th TASK ****************************
class DealLineClass(Widget):
    # This class define a widget that contains all the infos for a determined task

    def __init__(self,task_name = '', exp_date = '---', status = '---', **kwargs):
        # Call superclass init function
        super(DealLineClass,self).__init__(**kwargs)

        # Define constant string
        self.Widsize = (270, 35)
        self.DeadLine_name_str = 'TASK NAME'
        self.DeadLine_ExpireDate_str = 'EXPIRATION DATE'
        self.DeadLine_Status_str = 'STATUS'

        # Define the canvas properties to show
        with self.canvas:
            #\ Main Rect definition \#
            rgb_wid = fromRGBtoList(DeadlineListColor)
            Color(rgb_wid[0],rgb_wid[1],rgb_wid[2])
            Deadline_board = RoundedRectangle(size = self.Widsize)

            #\ Fixed labels \#
            Deadline_name = Label(text = self.DeadLine_name_str,
                                  size = (len(self.DeadLine_name_str),0), 
                                  color = (0,0,0), font_size = 10, bold = True, 
                                  pos = (30 , Deadline_board.size[1] - 10))

            Deadline_ExpireDate = Label(text = self.DeadLine_ExpireDate_str,
                                        size = (len(self.DeadLine_ExpireDate_str),0),
                                        color = (0,0,0), font_size = 10, bold = True,
                                        pos = (160 , Deadline_board.size[1] - 10))

            Deadline_ExpireDate = Label(text = self.DeadLine_Status_str,
                                        size = (len(self.DeadLine_Status_str),0),
                                        color = (0,0,0), font_size = 10, bold = True,
                                        pos = (250 , Deadline_board.size[1] - 10))

            #\ Information from DB \#
            Deadline_task_name = Label(text = task_name,
                                       color = (0,0,0),
                                       size = (200,13),
                                       text_size = (200,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (5, 5),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )

            Deadline_task_exp_date = Label(text = exp_date,
                                       color = (0,0,0),
                                       size = (100,13),
                                       text_size = (100,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (150,5),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )
            
            Deadline_task_status = Label(text = status,
                                       color = (0,0,0),
                                       size = (100,13),
                                       text_size = (100,13),
                                       font_size = 12, 
                                       halign = 'left',
                                       pos = (250,5),
                                       italic = True,
                                       font_name = 'RobotoMono-Regular' )

class MenuClass(RelativeLayout):
    def __init__(self,size = [Window.width,Window.height/3], **kwargs):
        # Call superclass init function
        super(MenuClass,self).__init__(**kwargs)
        self.line_width = 1.5
        with self.canvas:
            # Print the rectangles
            Base_color = fromRGBtoList([30,60,70])
            Color(Base_color[0],Base_color[1],Base_color[2])
            Rectangle(size = size, pos = [0,Window.height*2/3])

            # Print the rectangles and lines
            line_color = fromRGBtoList([0,0,0])
            Color(line_color[0],line_color[1],line_color[2])

            # Whole rectangle base
            Line(rectangle = [self.line_width,Window.height*2/3,Window.width - self.line_width * 2,Window.height/3 - self.line_width], width = self.line_width)
            
            # Line in the middle
            Line(points = [0,Window.height*5/6,Window.width,Window.height*5/6], width = self.line_width)
            for i in range(1,5):
                Line(points = [Window.width/4 * i,Window.height*2/3,Window.width/4 * i, Window.height], width = self.line_width)
            
class RoundedButton(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        # Call superclass init function
        super(RoundedButton,self).__init__(**kwargs)
        self.source = './Note_not_Selected_55.png'
        self.bind(on_press = self.printClicco)
        self.bind(on_release = self.printRilascio)
        #self.pos = [-112,167]
        
    def printClicco(self,touch):
        self.source = './Note_Selected_55.png'
        print('Clicco')

    def printRilascio(self,touch):
        print('Rilascio')
        self.source = './Note_not_Selected_55.png'

# **************************** REMINDER APP TO CALL **************************** 
class ReminderApp(App):
    def build(self):
        # Window properties
        self.title = 'First App'
        Window.clearcolor = BackgroudColor

        # Define the main Grid which will contains the Menu and the list retrieved from the MongoDB
        # root = BoxLayout(orientation = 'vertical') # , size_hint = [None,None])
        # root = GridLayout(cols = 1)
        # root = StackLayout()
        root = FloatLayout()

        # Define and add the Menu Widget
        MenuRelative = MenuClass()

        # Define the button grid which will contains the buttons 
        MenuRelative.add_widget(RoundedButton())
       
        #root.add_widget(MenuRelative2)
        # Define the ScrollList to show as second element of the 
        ScrollView_Layout = ScrollView(bar_color = [1,0,0,1], size = [Window.width,Window.height*2/3] )
        Deadline_list_lay = GridLayout(cols = 1, spacing = 5)

        # Deadline_list_lay = BoxLayout(orientation = 'vertical', spacing = 10)
        for i in range(3):
            Deadline_list_lay.add_widget(DealLineClass(task_name = 'Bolletta Linkem', exp_date = '01/11/2021', status = 'W.P'))

        ScrollView_Layout.add_widget(Deadline_list_lay)

        
        root.add_widget(MenuRelative)
        root.add_widget(ScrollView_Layout)
        return root
        
if __name__ == '__main__':
    # Launch the app
    ReminderApp().run()