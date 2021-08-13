from random import randint

r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
f'#{r:01x}{g:01x}{b:01x}'.upper()
