from moviepy.editor import *
from moviepy.video.fx.all import *

def cropp9_16(clip,n):
    (w, h) = clip.size
    try:
        if w>h:
            clip=clip.fx(vfx.resize,(h,h))

        if n=="top":
            left = 0
            top = 0
            right = w
            bottom = w
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=="middle":
            clip = vfx.crop(clip, width=w, height=w, x_center=w/2, y_center=h/2)
        elif n=="bottom":
            left = 0
            top = h-w
            right = w
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=='right':
            (w, h) = clip.size
            left = w/2
            top = 0
            right = w
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
        elif n=='middle_side':
            (w, h) = clip.size
            left = w/4
            top = 0
            right = w-w/4
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=='left':
            (w, h) = clip.size
            left = 0
            top = 0
            right = w/2
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

    except:
        pass

    return clip

v1=VideoFileClip()
v2=VideoFileClip()
m=input("enter place:")
cropp9_16(v1,v2)