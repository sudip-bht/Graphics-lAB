import numpy as np
class TwoDTransformations:
    def twoDTranslation(self, tx, ty):
        return np.matrix([[1, 0, tx],
                          [0, 1, ty],
                          [0, 0, 1]])

    def twoDRotation(self, angle):
        radians = np.radians(angle)
        return np.matrix([[np.cos(radians), -np.sin(radians), 0],
                          [np.sin(radians), np.cos(radians), 0],
                          [0, 0, 1]])

    def twoDScaling(self, sx, sy):
        return np.matrix([[sx, 0, 0],
                          [0, sy, 0],
                          [0, 0, 1]])

    def twoDReflectionXAxis(self):
        return np.matrix([[1, 0, 0],
                          [0, -1, 0],
                          [0, 0, 1]])

    def twoDReflectionYAxis(self):
        return np.matrix([[-1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]])

    def twoDReflectionYEqualX(self):
        return np.matrix([[0, 1, 0],
                          [1, 0, 0],
                          [0, 0, 1]])

    def twoDReflectionAboutOrigin(self):
        return np.matrix([[-1, 0, 0],
                          [0, -1, 0],
                          [0, 0, 1]])

    def twoDShearingXaxis(self, shx):
        return np.matrix([[1, shx, 0],
                          [0, 1, 0],
                          [0, 0, 1]])

    def twoDShearingYaxis(self, shy):
        return np.matrix([[1, 0, 0],
                          [shy, 1, 0],
                          [0, 0, 1]])



