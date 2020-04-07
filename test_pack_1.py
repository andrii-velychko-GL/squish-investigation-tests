# -*- coding: utf-8 -*-
from tone_control import *

def test_scroll_dial_moving():
    Screen().move_slider(17)
    Screen().move_dial(12)
    test.compare(Screen().get_progress_bar_value(), 12)
    
def test_scroll_moving():
    Screen().move_slider(99)
    test.compare(Screen().get_slider_value(), 99)

def test_dial_moving():
    Screen().move_dial(1)
    Screen().move_dial(99)
    test.compare(Screen().get_dial_value(), 99)
    
    Screen().move_dial(100)
    test.compare(Screen().get_dial_value(), 100)

def test_dial_moving_loop():
    
    for i in range(10):
        Screen().move_dial(i)
        test.compare(Screen().get_dial_value(), i)

    