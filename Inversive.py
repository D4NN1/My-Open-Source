import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption('Rotating Hyperbolic Line Emoji')

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

lineanflerotate = 0

def draw_hypernolar():
    glBegin(GL_LINES)
    for t in range(-180, 181, 10):  
        x = t / 50.0
        y = 1 / (x + 0.01)  
        glVertex3f(x, y, 0)
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_hypernolar()


    lineanflerotate += 1

    glPushMatrix()
    glRotatef(lineanflerotate, 1, 1, 1)
    draw_hypernolar()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
