def setup():
    size(2560, 1440)
    background(0)
    global peace_sign
    peace_sign = loadShape("peace.svg")
    peace_sign.disableStyle()

def mycolor():
    palletes = [
        ((254, 255), (0, 128),   (128, 255)), # pink/magenta
        ((254, 255), (0, 128),   (128, 255)), # pink/magenta
        ((0, 64),    (200, 255), (0, 64)), #    green
        ((64, 200),  (20, 30),   (64, 255)), #  purple
        ((64, 200),  (20, 30),   (64, 255)), #  purple
        ((0, 0),     (228, 255), (228, 255)), # blue-green
        ((0, 0),     (28, 88),   (200, 255)), # blue
        ((255, 255), (255, 255), (0, 64)), #    yellow
        ((255, 255), (128, 200), (0, 0)), #     orange
        ((254, 255), (0, 128),   (128, 255)), # pink/magenta
        ((0, 64),    (200, 255), (0, 64)), #    green
        ((64, 200),  (20, 30),   (64, 255)), #  purple
        ((0, 0),     (228, 255), (228, 255)), # blue-green
        ((0, 0),     (28, 88),   (200, 255)), # blue
        ((255, 255), (255, 255), (0, 64)), #    yellow
        ((255, 255), (128, 200), (0, 0)), #     orange
        ((255, 255), (255, 255), (255, 200)), # white
    ]
    (r, g, b) = palletes[int(random(len(palletes)))]
    return color(random(r[0], r[1]), random(g[0], g[1]), random(b[0], b[1]))

def draw():
    filter(BLUR, 2)
    translate(random(width), random(height))
    rotate(PI * random(-0.3, 0.3))
    scale(random(0.15, 3))
    noFill()
    stroke(mycolor())
    strokeWeight(21)
    shape(peace_sign, -140, -140)
    delay(100)
