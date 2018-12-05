from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

time = 0.0
import numpy as np
import math

nRays = 50

aperture = 0.1;
jitter = np.zeros(shape=(nRays,2))
for i in range(nRays) :
    theta = i*2.0*3.141592 / nRays
    c = math.cos(theta)
    s = math.sin(theta)
    jitter[i][0] = c*aperture*np.random.rand(1)
    jitter[i][1] = s*aperture*np.random.rand(1)

print(jitter)

def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)


def myDisplay():
    global nRays


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_ACCUM_BUFFER_BIT)

    glColor3f(1,1,0)
    for iter in range(nRays) :
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(0+jitter[iter][0],2+jitter[iter][1],5,
                  0,0,0,
                  0,1,0)
        for i in range(10):
            for j in range(10) :
                glPushMatrix()
                glTranslatef(i-5,0,j-5)
                glutSolidTeapot(0.25)
                glPopMatrix()
        glAccum(GL_ACCUM, 1./nRays)

    glAccum(GL_RETURN, 1.0)

    glFlush()

    return

def GLInit() :
    global tex

    # clear color setting
    glClearColor(0, 0, 0, 1)
    glClearAccum(0,0,0,1)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0,0,0,1)


def main(arg) :
    # opengl glut initialization
    glutInit(arg)

    # window setting
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH | GLUT_ACCUM)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Accum")

    GLInit()

    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myDisplay)

    glutMainLoop()


if __name__ == "__main__" :
    main(sys.argv)