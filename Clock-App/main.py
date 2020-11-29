# File: main.py

import kivy
from kivy.app import App
from kivy.core.text import LabelBase

from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.utils import get_color_from_hex
from kivy.clock import Clock

import time
from datetime import date

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

#Window.clearcolor = (1, 0, 0, 1)

LabelBase.register(name="Roboto",            # Adding Roboto Fonts for Clock
    fn_regular="fonts\Roboto-Thin.ttf",
    fn_bold="fonts\Roboto-Medium.ttf",
)

Window.clearcolor = get_color_from_hex("#101216")       # Changing the Window Background Color

#class ClockLayout(BoxLayout):
 #   time_prop = ObjectProperty(None)
  #  root.time_prop.text = "demo"

class RobotoButton():
    pass




class ClockApp(App):
    sw_seconds = 0

    def update(self, nap):
        self.sw_seconds += nap

    def update_time(self, nap):
        self.root.ids.time.text = time.strftime('[b]%I[/b]:%M:%S')
        self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %(int(minutes), int(seconds),int(seconds * 100 % 100)))

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start'
        if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0



if __name__ == "__main__":
    ClockApp().run()



