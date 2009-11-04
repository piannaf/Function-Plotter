class World_Screen:
    def __init__(self, xmin, ymin, xmax, ymax, width, height):
        self._xmin, self._ymin = xmin, ymin
        self._xmax, self._ymax = xmax, ymax
        self._width, self._height = width, height

    def world2screen(self, x, y):
        self.xc = (x - self._xmin)*self._width/(self._xmax - self._xmin)
        self.yc = self._height - \
            (y - self._ymin)*self._height/(self._ymax - self._ymin)

        return (self.xc, self.yc)

    def screen2world(self, xc, yc):
        self._x = xc*(self._xmax - self._xmin)/self._width + self._xmin
        self._y = (self._height - yc)* \
            (self._ymax - self._ymin)/self._height + self._ymin

        return (self._x, self._y)
