#include <GL/freeglut.h>
#include <math.h>

#define WIDTH 800
#define HEIGHT 600

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Set up a simple hyperbolic disk
    glColor3f(0.0, 0.5, 0.9); // Set color to blue
    glBegin(GL_POLYGON);

    float radius = 1.0;
    int sides = 100;

    for (int i = 0; i < sides; ++i) {
        float theta = 2.0 * M_PI * i / sides;
        float x = radius * cos(theta);
        float y = radius * sin(theta);

        glVertex2f(x, y);
    }

    glEnd();

    glFlush();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0); // Set the orthographic view
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("Non-Euclidean Geometry Engine");

    glClearColor(1.0, 1.0, 1.0, 1.0); // Set clear color to white
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0); // Set the orthographic view
    glMatrixMode(GL_MODELVIEW);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);

    glutMainLoop();

    return 0;
}
