# -*- coding: utf-8 -*-
from qt_widgets_init import *
import my_names

class Screen():
    def __init__(self):
        self._slider = Slider(my_names.slider_name)
        self._dial = Dial(my_names.dial_name)
        self._progress_bar = ProgressBar(my_names.progress_bar_name)
        self._tone_controls_spin_box = ToneControlsSpinBox(my_names.tone_controls_spin_box_name)
        
    def move_slider(self, value):
        self._slider.set_value(value)
      
    def get_slider_value(self):
        return self._slider.get_value()
    
        
    def move_dial(self,value):
        self._dial.set_value(value)
        
    def get_dial_value(self):
        return self._dial.get_value()
        
    def get_progress_bar_value(self):
        return self._progress_bar.get_value()
        
    def set_value_tone_controls_spin_box(self,value):
        self._tone_controls_spin_box.setValue(value)
        