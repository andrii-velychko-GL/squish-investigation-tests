# -*- coding: utf-8 -*-
import squish_module_helper

squish_module_helper.import_squish_symbols()

class Slider():
    def __init__(self, name):
        self.name = name
        self._slider = waitForObject(name)
        
    def set_value(self, value):
        self._slider.setValue(value)
        
    def get_value(self):
        return self._slider.value
    
class Dial():
    def __init__(self, name):
        self.name = name 
        self._dial = waitForObject(name)
        
    def set_value(self, value):
        self._dial.setValue(value)
        
    def get_value(self):
        return self._dial.value
    
class ProgressBar():
    def __init__(self, name):
        self.name = name 
        self._progress_bar = waitForObject(name)
        
    def get_value(self):
        return self._progress_bar.value
    
class ToneControlsSpinBox():
    def __init__(self, name):
        self.name = name 
        self._tone_controls_spin_box = waitForObject(name)
        
    def set_value(self, value):
        self._tone_controls_spin_box.setValue(value)
        
    def get_value(self):
        return self._tone_controls_spin_box.value
    
        
        
