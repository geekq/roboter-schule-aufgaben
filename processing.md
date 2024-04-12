= Processing

Starte `thonny Editor`, füge Folgendes ein (Ctrl+C, Ctrl+V), drücke F5 zum Ausführen

== Rechtecke

```
from p5 import *

def setup():
    size(500, 500)
    background('#004477')

def draw():
    fill('#FF0000')
    strokeWeight(-1)
    noStroke()
    rect(100, 150, 200, 300)
    print("Hello ")
    rect(200, 250, 250, 300)

run()
```

== Kreise

```
from p5 import *

def setup():
    size(1000, 1800)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=180)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

run()

```


