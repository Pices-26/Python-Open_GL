import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import*



verticies = (
    (-1,-1,1),
    (1,-1,-1),
    (-1,1,-1),
    (-1,1,1),
    (1,1,-1),

)

edges = (
    (1,2),
    (1,3),
    (1,4),
    (2,3),
    (3,4),
    (4,2)
)

surfaces = (
    (1,2,3),
    (1,3,4),
    (1,2,4)
)

colors = (
    (0,0,0),
    (1,1,1),
    (0,0,0),
    (1,1,1),
    (0,0,0),
    (1,1,1),
    (0,0,0),
    (1,1,1),
    (0,0,0),
    (1,1,1),
    (0,0,0),
    (1,1,1)
)

def triangle():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    song = pygame.mixer.music.load('spin.mp3')
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.mixer.music.play(1,0)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glRotatef(25, 3, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # calls cube
        triangle()
        pygame.display.flip()
        pygame.time.wait(10)
main()