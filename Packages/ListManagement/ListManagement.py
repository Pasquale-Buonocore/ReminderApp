from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Out .kv design file
Builder.load_file('Packages/ListManagement/ListManagement.kv')

class Deadlineclass(Widget):
    # Define an array which contains all the istances of a class
    Element_list = []

    # Define propriety 
    task_wid = ObjectProperty(None)
    data_wid = ObjectProperty(None)
    state_wid = ObjectProperty(None)

    # Initialize it
    def __init__(self, name = '', **kwargs):
        super(Deadlineclass,self).__init__(**kwargs)
        self.name = name
        Deadlineclass.Element_list.append(self.name)