
import os
import logging

log = logging.getLogger(__name__)



class SimpleExample():

    def __init__(self):
        self.multiplier = 5
        

    def get_result(self, input):
        self.value = input

        return self.value*self.multiplier
