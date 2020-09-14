import cv2
import numpy as np

def drawlines(im_points,pts,im_lines,lines,size=5):
    lines = lines.reshape(-1,3)
    _,c = im_lines.shape[:2]
    for r,ptr in zip(lines,pts):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        im_lines = cv2.line(im_lines, (x0,y0), (x1,y1), color,size)
        im_r = cv2.circle(im_points,tuple(ptr),size*size,color,-1)
    return im_lines,im_points
