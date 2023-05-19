import os

# * Limpia la consola segun el sistema
def clear():
    # windows
    if os.name =="nt":
        os.system("cls")
          
    # linux
    else:
        os.system("clear")