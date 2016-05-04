import pygame, sys, glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
pygame.init()

def displayImage(screen, px, topleft, prior):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width =  pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn't moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    # return current box extents
    return (x, y, width, height)

def setup(path):
    px = pygame.image.load(path)
    screen = pygame.display.set_mode( px.get_rect()[2:] )
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px

def mainLoop(screen, px):
    topleft = bottomright = prior = None
    n=0
    while n!=1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    n=1
        if topleft:
            prior = displayImage(screen, px, topleft, prior)
    return ( topleft + bottomright )

if __name__ == "__main__":
    filelist = glob.glob('img/*.png')
    if len(filelist) == 0:
        print ('Not found any *.png file')
    else:
        input_loc = filelist[0];
        screen, px = setup(input_loc)
        left, upper, right, lower = mainLoop(screen, px)

    # ensure output rect always has positive width, height
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower

    for filename in filelist:
        im = Image.open(filename)
        filename = filename.split('/')
        filename = filename[1]
        im = im.crop((left, upper, right, lower))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf", 24)
        #Screenshot from 2016-04-22 00-03-07-80.png
        tempstring = filename.split(".")
        tempstring = tempstring[0].split(" ");
        text = tempstring[2] + ' ' + tempstring[3]
        tcolor = (255, 0, 0)
        draw.text((100, 100), text, fill = tcolor, font = font)
        del draw
        pygame.display.quit()
        im.save('out/' + filename)
