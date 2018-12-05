from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

angle = 0.0

def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)

def drawQuad(x,y,z) :
    glPushMatrix()
    glTranslatef(x,y,z)
    glBegin(GL_QUADS)
    glVertex3f(-1, 1, 0)
    glVertex3f(-1,-1, 0)
    glVertex3f( 1,-1, 0)
    glVertex3f( 1, 1, 0)
    glEnd()
    glPopMatrix()

def myDisp ():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0,2,5, 0,0,0, 0,1,0)

    glClear(GL_STENCIL_BUFFER_BIT)
    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
    glDepthMask(GL_FALSE)
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()
    glStencilFunc(GL_EQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glDepthMask(GL_TRUE)
    glColor3f(1, 1, 0)
    glutSolidTeapot(0.7)

    glFlush()

def GLInit() :
    # clear color setting
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_STENCIL_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glClearColor(0,0,0,1)


def main(arg) :
    # opengl glut initialization
    glutInit(arg)

    # window setting
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH | GLUT_STENCIL)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Accum")

    GLInit()

    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisp)
    glutIdleFunc(myDisp)

    glutMainLoop()


if __name__ == "__main__" :
    main(sys.argv)