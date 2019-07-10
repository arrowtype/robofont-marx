W, H = 1000, 1000
newPage(W, H)

a = (0, 0.25, 1, 0.2)
b = (0, 0.4, 0.5, 0.8)
steps = 20


def i(a, b, f):
    return a+f*(b-a)


for step in range(0, steps):

    f = step / steps
    fill(i(a[0], b[0], f), i(a[1], b[1], f),
         i(a[2], b[2], f), i(a[3], b[3], f))

    rect(0, H/steps*(steps-step-1), W, H/steps)

fontSize(630)
font("Recursive Mono")
fontVariations(wght=801, ital=0.001, XPRN=0.01)
tracking(20)

fill(1, 1, 1, 0.5)
text("ma", (110, 530))
text("rx", (110, 110))

fill(0, 0, 0.1, 0.75)
text("ma", (125, 540))
text("rx", (125, 120))

saveImage("./readme-assets/marx-logo.png")
