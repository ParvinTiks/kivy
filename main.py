import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
 
class MainWidget(GridLayout):
    pass
    def press(self):

        maksimum = float(self.ids.max_input.text)
        opilane = float(self.ids.min_input.text)
        vastus = (int(opilane * 100)) / (int(maksimum))
        lõpp = round(vastus, 1)
        print(vastus)
        if lõpp >= 90:
            hinne = "5"
        elif lõpp >= 75:
            hinne = "4"
        elif lõpp >= 50:
            hinne = "3"
        elif lõpp < 50:
            hinne = "2"


        self.ids.name_label.text = f'Protsent: {lõpp} ja hinne: {hinne}'
        self.ids.min_input.text = ''
class myApp(App):
    def build(self):

        return MainWidget()
 
if __name__ == '__main__':
     
    
    myApp().run()