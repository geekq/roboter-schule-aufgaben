## Quadratzahlen ausgeben

```
for i in range(-10, 11):
    print(i**2)
```


## Schleife, `break`

```
while True:
    antwort = input("Gib ein 'stop' zum beenden: ")
    if antwort == 'stop':
        break
    print(antwort)
```

## Du denkst eine Zahl aus, dein Computerprogramm rät

```
min = 1
max = 200
print("Denke dir eine Zahl von 1 bis 200 aus")
while True:
    probiere = (min + max) // 2
    print(f"Ist es {probiere}?")
    antwort = input("Gib ein 'v' für zu viel, 'w' für zu wenig: ")
    if antwort == 'v':
        max = probiere
    elif antwort == 'w':
        pass # TODO ersetze diese Zeile durch richtige Anweisung
    else:
        print("Hinweis: TODO")
```


## Zahlen vs. Strings

Es gibt Unterschied zwischen Zahlen und den Zeichenfolgen, die eine Zahl
dartellen. Probiere aus:

```
>>> 15 * 4

>>> '15' * 4
```


## Lasse den Computer eine Zahl ausdenken, du musst die erraten

```
import random
geheim = random.randint(1, 200)

# print(geheim)
while True:
    eingabe = int(input("Gib die Zahl ein: "))
    if eingabe > geheim:
        print("Zu ...
    elif ...
```
