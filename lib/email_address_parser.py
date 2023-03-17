# your code goes here!
import re

class EmailAddressParser():

    def __init__(self, string):
        self.string = string

    def parse(self):
        pattern = r"[\w\.\w]+@[\w]+.com"
        regex = re.compile(pattern)
        match = regex.findall(self.string)
        match.reverse()
        return match