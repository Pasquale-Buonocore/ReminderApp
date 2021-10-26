# sets the windows configuration
from WindowConfig import * 

# Import kivy and all the necessary objects
import kivy
import json
import pymongo
from pymongo import MongoClient
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder


# Definition of the classes, whose graphics is described in the Note.kv

class CustomPopup(Popup):
    def printCiao():
        print('Ciao')
    pass

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

class Scroll(ScrollView):
    # Define a list which contains all the elelements in the grid
    Grid_elements = []

    # Define properties
    grid_wid = ObjectProperty(None)

    # Initialize
    def __init__(self, **kwargs):
        super(Scroll,self).__init__(**kwargs)  

    def UpdateGridheight(self):
        print('Updating height')
        #sum([c.height for c in self.children]) + self.spacing[1]*len(self.children)

class PersonalButton(Button):
    # Define a list which contains all the buttons in the menu
    Menu_buttons_elements = 0
    Menu_button_selected = "Deadlines"
    Button_configuration = {}

    # Define element for all the button, label and button image!
    button_image = ObjectProperty(None)
    button_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PersonalButton,self).__init__(**kwargs)
        self.ButtonName = ''
        self.Button_Selected = ''
        self.Button_not_Selected = ''

        # SET CLASS ATTRIBUTES 
        PersonalButton.Menu_buttons_elements = PersonalButton.Menu_buttons_elements + 1

        if not len(PersonalButton.Button_configuration.keys()):
            # Open the menu configuration file
            with open('./Configuration/MenuButton_setting.json') as json_file:
                PersonalButton.Button_configuration = json.load(json_file)
        
    # DEFINE FUNCTIONS
    def do_action(self):
        self.label_wid.text = 'My label after button press'
    
    def setImage(self,root):
        for children in root.ids['menu_buttons_id'].children:
            if children.ButtonName == self.ButtonName:
                print(f"Sto cambiando l'icona di {children.ButtonName}")
                children.ids['image_id'].source = children.Button_Selected
                PersonalButton.Menu_button_selected = children.ButtonName
                root.FillTheList()
            else:
                print(f"Non cambio l'icona di {children.ButtonName}")
                children.ids['image_id'].source = children.Button_not_Selected


class LayoutApp(StackLayout):
    # Define onject to access the grid that contains the buttons
    menu_buttons_wid = ObjectProperty(None)
    scroll_wid = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(LayoutApp,self).__init__(**kwargs)

        # Load the DataBase (Should it be updated when something is inserted?)
        client = MongoClient('localhost', 27017)
        self.db = client.NoteAPP

        # Load the Database configuration file
        with open('./Configuration/DataBase_Structure.json') as json_file:
            self.db_configuration = json.load(json_file)
        

    def InitializeMenu(root):
        # Extract dictionary
        ButtonConfiguration_dict = root.ids['menu_buttons_id'].children[0].Button_configuration

        # Initialize the menu buttons!
        for p in range(len(root.ids['menu_buttons_id'].children)):
            # Define current children to modify
            children = root.ids['menu_buttons_id'].children[len(root.ids['menu_buttons_id'].children) - 1 -p]

            # Actually modify the attribute of the children
            try:
                # Set object attributes
                children.ButtonName = ButtonConfiguration_dict['MenuButtons'][p]['name']
                children.Button_not_Selected = ButtonConfiguration_dict['MenuButtons'][p]['image_not_selected']
                children.Button_Selected = ButtonConfiguration_dict['MenuButtons'][p]['image_selected']

                if not ButtonConfiguration_dict['MenuButtons'][p]['name'] == 'Deadlines':
                    # Initialize button as not selected
                    children.ids['lbl_id'].text = ButtonConfiguration_dict['MenuButtons'][p]['name']
                    children.ids['image_id'].source = ButtonConfiguration_dict['MenuButtons'][p]['image_not_selected']
                else:
                    # Initialize DEADLINE button as selected
                    children.ids['lbl_id'].text = ButtonConfiguration_dict['MenuButtons'][p]['name']
                    children.ids['image_id'].source = ButtonConfiguration_dict['MenuButtons'][p]['image_selected']
            except:
                print(f"The {p} -th button has no configuration in the .json file")
    
    def FillTheList(root):
        print('Initializing ScrollView using MongoDB')

        # First clear the list
        root.ids['scroll_id'].ids['scroll_grid_id'].children = []

        # Then fill the list
        Actual_button = root.ids['menu_buttons_id'].children[0].Menu_button_selected
        for i in range(root.db[Actual_button].count_documents({})):
            root.ids['scroll_id'].ids['scroll_grid_id'].add_widget(Deadlineclass())
    
    def UpdateDatabase(root):
        # We need to find which collection is needed to update
        # We can retrive such information from the menu button selected
        Actual_selected_button = root.ids['menu_buttons_id'].children[2].Menu_button_selected

        # We need to add a widget in the collection, which format does it have to have?
        # Let's retrive such information from the db configuration
        try:
            Basic_widget_definition = root.db_configuration[Actual_selected_button][0] 
            root.db.get_collection(Actual_selected_button).insert_one(Basic_widget_definition)
        except:
            print('Impossible to append since ')

        # Refresh the list before exist
        root.FillTheList()
        print("You want to update the repository")


class NoteApp(App):
    
    def build(self):
        # Set the window properties
        self.title = 'Ciao Caro'
        Window.clearcolor = BackgroudColor

        # Initilize the root layout
        root = LayoutApp()

        # Initilize the Menu buttons
        LayoutApp.InitializeMenu(root)
        
        # Initialize the ScrollView
        LayoutApp.FillTheList(root)

        return root

if __name__ == '__main__':
    NoteApp().run()



