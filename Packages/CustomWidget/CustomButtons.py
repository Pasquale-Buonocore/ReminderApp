from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
import json

# Designate Out .kv design file
Builder.load_file('Packages/CustomWidget/CustomButtons.kv')

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