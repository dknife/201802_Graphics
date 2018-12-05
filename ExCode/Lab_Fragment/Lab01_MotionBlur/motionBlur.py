from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

time = 0.0



def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)


def myDisplay():
    global time

    time += 0.5

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,3, 0,0,0, 0,1,0)

    glRotatef(time, 1,1,1)

    glutSolidTeapot(1.0)
    glAccum(GL_MULT, 0.975)
    glAccum(GL_ACCUM, 0.025)
    glAccum(GL_RETURN, 1.0)

    glFlush()

    return

def GLInit() :
    # clear color setting
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
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