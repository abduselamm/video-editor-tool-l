from django.shortcuts import render,redirect
from .form import *
from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import random
from zipfile import ZipFile
from os.path import basename
from .metadata import *
import os
import shutil
import zipfile
#from .videomerger import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        o_videos = request.FILES.getlist('original_video')
        m_videos = request.FILES.getlist('merged_video')

        O_Video.objects.all().delete()
        M_Video.objects.all().delete()
        Output_Video.objects.all().delete()

        dir_name1 = os.path.abspath("static/assets/merged_uploaded/")
        test1 = os.listdir(dir_name1)
        dir_name2 = os.path.abspath("static/assets/original_uploaded/")
        test2 = os.listdir(dir_name2)

        for item in test1:
            if item.endswith(".mp4") or item.endswith(".mkv") or item.endswith(".mov"):
                os.remove(os.path.join(dir_name1, item))
        for item in test2:
            if item.endswith(".mp4") or item.endswith(".mkv") or item.endswith(".mov"):
                os.remove(os.path.join(dir_name2, item))

        for o_video in o_videos:
            o_vid = O_Video.objects.create(
                original_video=o_video,
            )
            o_vid.save()

        for m_video in m_videos:
            m_vid = M_Video.objects.create(
                merged_video=m_video,
            )
            m_vid.save()
        return redirect('preview')

    context = {}
    return render(request, 'merger_tools/index.html', context)


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


def cropp1_1(clip,n):
    (w, h) = clip.size
    try:
        if w>h:
            clip=clip.fx(vfx.resize,(h,h))

        if n=="top":
            left = 0
            top = 0
            right = w
            bottom = w/2
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=="middle":
            clip = vfx.crop(clip, width=w, height=w/2, x_center=w/2, y_center=h/2)
        elif n=="bottom":
            left = 0
            top = h-w/2
            right = w
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=='right':
            (w, h) = clip.size
            if w<=h/2:
                return clip
            half=h/2
            left = w-half
            top = 0
            right = w
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=='left':
            (w, h) = clip.size
            if w<=h/2:
                return clip
            half=h/2
            left = 0
            top = 0
            right = h/2
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
        elif n=='middle_square':
            (w, h) = clip.size
            if w<=h/2:
                return clip
            half=h/2
            deduct=(w-half)/2
            left = deduct
            top = 0
            right = w-deduct
            bottom = h
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

    except:
        pass
    return clip

def byheight(clip,n):
    if n=="left":
        (clip_w, clip_h) = clip.size
        left = 0
        top = 0
        right = clip_h
        bottom = clip_h
        clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
    elif n=='right':
        (clip_w, clip_h) = clip.size
        left = clip_w-clip_h
        top = 0
        right = clip_w
        bottom = clip_h
        clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
    elif n=='middle_side':
        (clip_w, clip_h) = clip.size
        cutted_width=(clip_w-clip_h)/2
        left = cutted_width
        top = 0
        right = clip_w-cutted_width
        bottom = clip_h
        clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
    return clip

def alishoo9_16(clip,n,w):
    try:
        """         if w>h:
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
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom) """

        if n=='bottom':
            (clip_w, clip_h) = clip.size
            left = clip_w-w
            cutted_height=(clip_h-w)/2
            top = cutted_height
            right = clip_w
            bottom = clip_h-cutted_height
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)
        elif n=='middle':
            (clip_w, clip_h) = clip.size
            cutted_height=(clip_h-w)/2
            cutted_width=(clip_w-w)/2
            left = cutted_width
            top = cutted_height
            right = clip_w - cutted_width
            bottom = clip_h-cutted_height
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

        elif n=='top':
            (clip_w, clip_h) = clip.size
            cutted_height=(clip_h-w)/2
            left = 0
            top = cutted_height
            right = w
            bottom = clip_h-cutted_height
            clip = vfx.crop(clip,x1=left, y1=top, x2=right, y2=bottom)

    except:
        pass

    return clip


def temp1(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)

            d1=clip1.duration
            d2=clip2.duration

            w1,h1=clip1.size
            w2,h2=clip2.size
            print(clip1.size)
            print(clip2.size)
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))

            print(clip1.size)
            print(clip2.size)

            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1
    return n

def temp2(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            d1=clip1.duration
            d2=clip2.duration

            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))


            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)       

            n+=1


def temp3(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            
            d1=clip1.duration
            d2=clip2.duration
            
            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))

            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
        
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1

def temp4(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            
            d1=clip1.duration
            d2=clip2.duration

            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))


            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1

def temp5(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)

            d1=clip1.duration
            d2=clip2.duration
            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))


            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)

            n+=1


def temp6(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            
            d1=clip1.duration
            d2=clip2.duration
            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))


            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1


def temp7(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            
            d1=clip1.duration
            d2=clip2.duration
            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1

def temp8(sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            
            d1=clip1.duration
            d2=clip2.duration
            w1,h1=clip1.size
            w2,h2=clip2.size
            if w1>h1 and w2>h2:
                clip1=byheight(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2<h2:
                widht,height=clip2.size
                clip1=alishoo9_16(clip1,crop_o,widht)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1<h1 and w2>h2:
                widht,height=clip1.size
                clip1=cropp9_16(clip1,crop_o)
                clip2=alishoo9_16(clip2,crop_m,widht)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1>h1 and w2==h2:
                clip1=byheight(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            elif w1==h1 and w2>h1:
                clip1=cropp9_16(clip1,crop_o)
                clip2=byheight(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))
            else:            
                clip1=cropp9_16(clip1,crop_o)
                clip2=cropp9_16(clip2,crop_m)
                w11,h11=clip1.size
                clip2=clip2.fx(vfx.resize,(w11,h11))

            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)            
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            n+=1


def select_sound(sound,o,m,n,clips,formats,resize,temp_size):
    if sound == 'no_sound':
        final1 = clips.without_audio()
    elif sound == "s_from_original": 
        AudioClip=AudioFileClip(o)
        final1 = clips.set_audio(AudioClip)
    elif sound == "s_from_merged":
        AudioClip=AudioFileClip(m)
        final1 = clips.set_audio(AudioClip)
    else:
        final1 = clips

    if temp_size == '9:16':
        if resize == 'HD':
            try:
                final1=final1.fx(vfx.resize,(1080,1920))
            except:
                pass
        else:
            try:
                final1=final1.fx(vfx.resize,(2160,3840))
            except:
                pass
    else:
        if resize == 'HD':
            try:
                final1=final1.fx(vfx.resize,(1080,1080))
            except:
                pass
        else:
            try:
                final1=final1.fx(vfx.resize,(2160,2160))
            except:
                pass
    try:
        final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+"."+formats), fps = 30, codec = 'mpeg4')
    except:
        pass
    oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".mp4"))
    oo.save()


def create_template(o_place,m_place,sound,formats,crop_o,crop_m,resize,temp_size):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0
    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)

            d1=clip1.duration
            d2=clip2.duration

            if temp_size == '9:16':
                if o_place=='left' or o_place=='right':
                    if crop_o=='middle' and crop_m=='middle':
                        crop_o='middle_square'
                        crop_m='middle_square'
                        clip1=cropp9_16(clip1,crop_o)
                        clip2=cropp9_16(clip2,crop_m)
                    elif crop_m=='middle':
                        crop_m='middle_square'
                        clip1=cropp9_16(clip1,crop_o)
                        clip2=cropp9_16(clip2,crop_m)
                    elif crop_o=='middle':
                        crop_o='middle_square'
                        clip1=cropp9_16(clip1,crop_o)
                        clip2=cropp9_16(clip2,crop_m)
                    else:
                        clip1=cropp9_16(clip1,crop_o)
                        clip2=cropp9_16(clip2,crop_m)
                else:
                    clip1=cropp9_16(clip1,crop_o)
                    clip2=cropp9_16(clip2,crop_m)
       
            elif temp_size == '1:1':
                if o_place=='left' or o_place=='right':
                    if crop_o=='middle' and crop_m=='middle':
                        crop_o='middle_square'
                        crop_m='middle_square'
                        clip1=cropp1_1(clip1,crop_o)
                        clip2=cropp1_1(clip2,crop_m)
                    elif crop_m=='middle':
                        crop_m='middle_square'
                        clip1=cropp1_1(clip1,crop_o)
                        clip2=cropp1_1(clip2,crop_m)
                    elif crop_o=='middle':
                        crop_o='middle_square'
                        clip1=cropp1_1(clip1,crop_o)
                        clip2=cropp1_1(clip2,crop_m)
                    else:
                        clip1=cropp1_1(clip1,crop_o)
                        clip2=cropp1_1(clip2,crop_m)
                else:
                    clip1=cropp1_1(clip1,crop_o)
                    clip2=cropp1_1(clip2,crop_m)

            w11,h11=clip1.size
            clip2=clip2.fx(vfx.resize,(w11,h11))

            if o_place=='top' and m_place=='bottom':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                else:
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)

            elif o_place=='bottom' and m_place=='top':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                else:
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)

            elif o_place=='left' and m_place=='right':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                else:
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)

            elif o_place=='right' and m_place=='left':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
                else:
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    select_sound(sound,o,m,n,clips,formats,resize,temp_size)
            else:
                return 'The selected merging is not correct, please! select the right one'                

            n+=1


def preview(request):
    o_video = O_Video.objects.all()
    m_video = M_Video.objects.all()
    
    context={'o_video':o_video, 'm_video':m_video}
    return render(request, 'merger_tools/preview.html', context)


def templates(request):
    #video = O_Video.objects.all()
    error = ''
    if request.method == 'POST':
        Output_Video.objects.all().delete()

        temp_name1 = request.POST.get('temp1')
        temp_name2 = request.POST.get('temp2')
        temp_name3 = request.POST.get('temp3')
        temp_name4 = request.POST.get('temp4')
        temp_name5 = request.POST.get('temp5')
        temp_name6 = request.POST.get('temp6')
        temp_name7 = request.POST.get('temp7')
        temp_name8 = request.POST.get('temp8')

        formats = request.POST.get('format')
        
        crop_o = request.POST.get('crop_original')
        crop_m = request.POST.get('crop_merged')
        resize = request.POST.get('resize')
        temp_size = request.POST.get('temp-size')

        o_place = request.POST.get('o_place')
        m_place = request.POST.get('m_place')
        sound = request.POST.get('sound')
        
        if o_place!=None and m_place!=None and temp_size!=None:
            print(o_place,m_place,sound,formats,crop_o,crop_m,resize,temp_size)
            create_template(o_place,m_place,sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name1:
            temp_size = '9:16'
            temp1(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name2: 
            temp_size = '9:16'
            temp2(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name3:
            temp_size = '9:16'
            temp3(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name4:
            temp_size = '9:16'
            temp4(sound,formats,crop_o,crop_m,resize,temp_size)  
        elif temp_name5:
            temp_size = '1:1'
            temp5(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name6:
            temp_size = '1:1'
            temp6(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name7:
            temp_size = '1:1'
            temp7(sound,formats,crop_o,crop_m,resize,temp_size)
        elif temp_name8:
            temp_size = '1:1'
            temp8(sound,formats,crop_o,crop_m,resize,temp_size) 
        else:
            print('Please select the correct template')
        return redirect('output')

    context = {'error':error}
    return render(request, 'merger_tools/template.html', context)

def output(request):
    outputs = Output_Video.objects.all()
    c=outputs.count()
    Zip_file.objects.all().delete()
    zip_name = 'allvideo.zip'
    with ZipFile(os.path.abspath('static/assets/zip/'+zip_name), 'w') as zipObj:
        for file in outputs:
                    filename=file.output.path
                    zipObj.write(filename, basename(filename))
    
    zipObj.close()

    if zip_name in os.path.abspath('static/assets/zip/'+zip_name):
        Zip_file.objects.create(file=zipObj.filename)
    zipf = Zip_file.objects.get()
    context = {'outputs':outputs,'zipf':zipf,'c':c}
    return render(request, 'merger_tools/output.html', context)
    
def home(request):
    return render(request, 'merger_tools/home.html')

from datetime import datetime
import random

def metadata(request):
    if request.method == 'POST':
        videos = request.FILES.getlist('video')
        spin = request.POST.get('spin')
        export = request.POST.get('export')
        mute = request.POST.get('gridRadios')
        formats = request.POST.get('format')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')

        print(start_date,end_date)
        if videos:
            MetaData_Video.objects.all().delete()
            New_Metadata.objects.all().delete()
            dir_name = os.path.abspath("static/assets/metadata/")
            test = os.listdir(dir_name)

            for item in test:
                if item.endswith(".mp4"):
                    os.remove(os.path.join(dir_name, item))
                    
            for vid_m in videos:
                vid = MetaData_Video.objects.create(video=vid_m)
                vid.save()

                    #try:
                    #    os.mkdir(os.path.join(os.path.abspath('static/assets'), v_name))
                    #except:
                    #    pass            

        if spin and export and formats and mute and start_date and end_date:
            start_date = start_date.replace("-", "/")
            start_date = start_date.replace('T', ' ')
            end_date = end_date.replace("-", "/")
            end_date = end_date.replace('T', ' ')

            start_date = datetime.strptime(start_date, '%Y/%m/%d %H:%M:%S')
            end_date = datetime.strptime(end_date, '%Y/%d/%m %H:%M:%S')

            first_timestamp = int(start_date.timestamp())
            second_timestamp = int(end_date.timestamp())

            dir_name = os.path.abspath("static/assets/newVideo/")
            test = os.listdir(dir_name)

            for item in test:
                if item.endswith(".mp4"):
                    os.remove(os.path.join(dir_name, item))

            Folder.objects.all().delete()
            if export=='by_original_name':
                v = MetaData_Video.objects.all()
                for i in v:
                    v_name = os.path.basename(i.video.name)
                    v_name=v_name[:-4]
                    fold = Folder.objects.create(folder=v_name)            
                    fold.save()

            elif export=='by_creator':
                for i in range(1,int(spin)+1):
                    fol = 'Creator '+str(i)
                    fold = Folder.objects.create(folder=fol)
                    fold.save()

            v = MetaData_Video.objects.all()
            f = Folder.objects.all()
            
            if export =='by_original_name':
                for i in range(len(f)):
                    v_name = os.path.basename(v[i].video.name)
                    foldr = f[i].folder
                    metadata_changer(v[i].video.path,v_name,int(spin),mute,foldr,formats,first_timestamp,second_timestamp)
            else:
                for j in v:
                    v_name = os.path.basename(j.video.name)
                    metadata_changer_byc(j.video.path,v_name,int(spin),mute,formats,first_timestamp,second_timestamp)

            return redirect('metadata_changed_video')
                    
    return render(request, 'merger_tools/metadata.html')



def meta_output(request):
    meta = New_Metadata.objects.all()
    fol = Folder.objects.all()
    c=meta.count()
    zip_name='Exported By Creator'
    dir1 = os.path.abspath('static/assets/download_zip/')
    shutil.rmtree(dir1, ignore_errors=True)
    if c != 0:
        for i in fol:
            f=i.folder
            if str(f[:-3]) not in zip_name:
                zip_name="Exported By Original File Name"
            for j in meta:
                v=j.fold
                if str(f)==str(v):
                    folde_name=f

                    dir = os.path.abspath('static/assets/download_zip/'+folde_name)
                    try:
                        os.makedirs(dir)
                        shutil.copy2(j.new_video.path, dir)
                    except:
                        shutil.copy2(j.new_video.path, dir)

    Zip_file.objects.all().delete()
    dir = os.path.abspath('static/assets/download_zip/')
    zipf = zipfile.ZipFile(os.path.abspath('static/assets/zip/'+zip_name+'.zip'), "w")
    lenDirPath = len(dir)
    for root, _ , files in os.walk(dir):
        for file in files:
            filePath = os.path.join(root, file)
            zipf.write(filePath , filePath[lenDirPath :] )
    zipf.close()

    if zip_name in os.path.abspath('static/assets/download_zip/'+zip_name):
        Zip_file.objects.create(file=zipf.filename)
    zipf = Zip_file.objects.get()
    context = {'meta':meta,'c':c,'zipf':zipf}

    return render(request, 'merger_tools/meta_output.html',context)
