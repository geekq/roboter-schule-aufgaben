# Processing

Erstelle ein Programm, wo die Maus eine Spur aus Rechtecken hinterlässt.

<img src='https://py5coding.org/_images/index_example.gif'>

Du brauchst dafür:


```
from p5 import *
def setup():
    size(400, 400)
    rect_mode(CENTER)

def draw():
    square(mouse_x, mouse_y, 10)

def mouse_clicked():
    fill(random_int(255), random_int(255), random_int(255))

run_sketch()
```

1. Versuche, die Größe der Rechtecke zu verändern
2. Versuche, die Größe der Rechtecke zufällig zu machen, aber in einem
   bestimmten Bereicht, z.B. von 10 bis 20
