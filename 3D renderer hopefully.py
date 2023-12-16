import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption('Rotating Cube Emoji')


gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

cube_angle = 0
sphere_angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw your 3D objects here
    def draw_sphere():
        glBegin(GL_QUADS)
        glVertex3fv((1, 1, -1))
        glVertex3fv((-1, 1, -1))
        glVertex3fv((-1, 1, 1))
        glVertex3fv((1, 1, 1))
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

    # Left face
        glBegin(GL_QUADS)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, -1, -1)
        glEnd()

    # Right face
        glBegin(GL_QUADS)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)
        glEnd()

    # Top face
        glBegin(GL_QUADS)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)
        glEnd()

    # Bottom face
        glBegin(GL_QUADS)
        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

    # Update the display
    cube_angle += 1
    sphere_angle += 1

    glPushMatrix()
    glTranslatef(0, 0, 0)
    glRotatef(sphere_angle, 1, 1, 1) 
    draw_sphere()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
