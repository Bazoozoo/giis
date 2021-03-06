__author__ = 'drain'

import math

class CDA:

    @staticmethod
    def getPixels(points):
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        pixels = []
        len = max(abs(x2 - x1), abs(y2 - y1))
        dx = (x2 - x1) / len
        dy = (y2 - y1) / len
        x = x1
        y = y1
        i = 1.0
        while i <= len:
            pixels.append((x,y))
            x = x + dx
            y = y + dy
            i += 1.0
        pixels.append((x2,y2))
        return pixels

    @staticmethod
    def getMinPointsCount():
        return 2

class Bresenham:

    @staticmethod
    def getPixels(points):
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        pixels = []
        dx = x2 - x1
        dy = y2 - y1
        incx = math.copysign(1.0,dx)
        incy = math.copysign(1.0,dy)
        if dx < 0 : dx = -dx
        if dy < 0 : dy = -dy
        if dx > dy :
            pdx = incx
            pdy = 0
            es = dy
            el = dx
        else:
            pdx = 0
            pdy = incy
            es = dx
            el = dy
        x = x1
        y = y1
        pixels.append((x,y))
        err = el/2.0
        t = 0.0
        while t < el:
            t += 1.0
            err -= es
            if err < 0.0:
                err += el
                x += incx
                y += incy
            else:
                x += pdx
                y += pdy
            pixels.append((x,y))
        return pixels

    @staticmethod
    def getMinPointsCount():
        return 2
