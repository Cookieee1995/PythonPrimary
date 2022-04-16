from greenlet import greenlet

def eat(name):
    print('%s eat 1' % name)
    g2.switch('alex')
    print('%s eat 2' % name)

def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)

g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('alex')