from my_test import *
import time
from tone_control import *
from test_pack_1 import *


def main():
    startApplication("cmakeqtapp")
    
    test_scroll_dial_moving()
    test_scroll_moving()
    test_dial_moving()
    test_dial_moving_loop()
    