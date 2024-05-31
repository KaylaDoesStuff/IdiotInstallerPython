from variables import *
from functions import *

def main():
    distro = check_distro()
    print("Detected derivative of "+distro)
    type_print()

main()