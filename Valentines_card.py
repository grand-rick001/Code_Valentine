# This program uses very simple graphics to create a simple valentine's card using shapes.

from graphics import *

def main():
    # Set the window and its background
    wndw = GraphWin("Valentine's Card", 800, 800)
    wndw.setBackground(color_rgb(0,0,0))
    
    # Draw a line for letter "I"
    ln = Line(Point(400,50), Point(400,250))
    ln.setFill(color_rgb(229,84,81))
    ln.setWidth(10)
    ln.draw(wndw)

    # Draw the lines for letter "L"
    ln1 = Line(Point(100,300), Point(100,500))
    ln1.setOutline(color_rgb(0,255,200))
    ln1.setWidth(10)
    ln1.draw(wndw)

    ln2 = Line(Point(95,500), Point(250,500))
    ln2.setOutline(color_rgb(0,255,200))
    ln2.setWidth(10)
    ln2.draw(wndw)
    
    # Draw the circle representing letter "O"
    pnt = Point(400,400)
    crc = Circle(pnt,100)
    crc.setFill(color_rgb(229,84,81))
    crc.draw(wndw)
    
    # Draw the lines for letter "V"
    ln3 = Line(Point(510,300), Point(600,500))
    ln3.setOutline(color_rgb(0,255,200))
    ln3.setWidth(10)
    ln3.draw(wndw)

    ln4 = Line(Point(700,300), Point(597,500))
    ln4.setOutline(color_rgb(0,255,200))
    ln4.setWidth(10)
    ln4.draw(wndw)

    # Add an image of the person you love
    img = Image(Point(400,600), "Kiz_outing.png")
    img.draw(wndw)

    # Add the sender's name
    txt = Text(Point(750,630), "From: ")
    txt.setFace("courier")
    txt.setTextColor(color_rgb(0,255,100))
    txt.draw(wndw)

    txt1 = Text(Point(730,650), "Ridhiwan MSEYA")
    txt1.setFace("courier")
    txt1.setTextColor(color_rgb(0,255,100))
    txt1.draw(wndw)

    wndw.getMouse()
    wndw.close()

main()