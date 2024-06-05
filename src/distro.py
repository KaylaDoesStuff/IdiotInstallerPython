import os

class Arch():
    def __init__(self, package):
        self.package = package

    def install(self):
        command = "sudo pacman -S"+self
        os.system(command)
