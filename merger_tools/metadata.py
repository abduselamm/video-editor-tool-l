#from .views import * 
import ffmpeg
import random
from .models import *
import os
from datetime import datetime
from moviepy.editor import *
import string

def metadata_changer(v,v_name,spin,mute,foldr,formats,first_timestamp,second_timestamp):
    ext = v_name[-3:]
    print(v_name)
    x=v_name
    s=''
    for j in x:
        if  j.isdigit():
            s+=j
        elif s and j=='.':
            s+='.'
            
        else:
            if s and j.lower() in ['k','m'] and s[-1].isdigit():
                s+=j
                break
            else:
                s=''

    print(s)
    if len(s)>=1:    
        if s[-1].lower() not in ['k','m']:
            s=''
    viral=s
    print(viral)
    N=7
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    full_name=name
    if viral != '':
        full_name=viral+'_'+full_name
    
    resolution=VideoFileClip(v)
    (w,h)=resolution.size
    for i in range(spin):
        random_timestamp = random.randint(first_timestamp, second_timestamp)
        random_timestamp = datetime.fromtimestamp(random_timestamp)
        random_timestamp = str(random_timestamp)+'.000000Z'

        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)

        full_name+=str(rand_name)
        if ext=='mp4':
            stream = ffmpeg.input(v)
            if w<h:    
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',720,1280)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,1920)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,2048)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')
            elif w>h:   
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',1280,720)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1920,1080)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',2048,1080)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')
            elif w==h:
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,1080)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1920,1920)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',2048,2048)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')

            if mute == 'dont_mute':
                try:
                    audio = stream.audio
                    stream = ffmpeg.output(audio,video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+random_timestamp)
                    ffmpeg.run(stream)
                except:
                    pass
            else:
                try:
                    stream = ffmpeg.output(video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+random_timestamp)
                    ffmpeg.run(stream)
                except:
                    pass
            try:
                md=os.path.abspath("static/assets/newVideo/"+full_name+".mp4")
                file = open(md, 'rb').read()
                with open(md, 'wb') as new_file:
                    new_file.write(file+'\0'.encode('ascii'))  
            except:
                pass

            if formats == '4k':
                final=VideoFileClip(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
                if w<h:
                    final=final.fx(vfx.resize,(2160,3840))
                elif w>h:
                    final=final.fx(vfx.resize,(3840,2160))
                elif w==h:
                    final=final.fx(vfx.resize,(2160,2160))
                final.write_videofile(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), fps = 30, codec = 'mpeg4')
            
            ff=Folder.objects.get(folder=foldr)
            oo=New_Metadata.objects.create(fold=ff,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
            oo.save()
        

def metadata_changer_byc(v,v_name,spin,mute,formats,first_timestamp,second_timestamp):
    ext=v_name[-3:]
    print(ext)
    x=v_name
    s=''
    for j in x:
        if  j.isdigit():
            s+=j
        elif s and j=='.':
            s+='.'
            
        else:
            if s and j.lower() in ['k','m'] and s[-1].isdigit():
                s+=j
                break
            else:
                s=''
    if len(s)>=1:
        if s[-1].lower() not in ['k','m']:
            s=''
    viral=s
    N = 8
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    full_name=name

    resolution=VideoFileClip(v)
    (w,h)=resolution.size

    if viral != '':
        full_name=viral+'_'+full_name
    print(full_name)

    ff=Folder.objects.all()
    for i in range(spin):
        random_timestamp = random.randint(first_timestamp, second_timestamp)
        random_timestamp = datetime.fromtimestamp(random_timestamp)
        random_timestamp = str(random_timestamp)+'.000000Z'

        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)
        full_name+=str(rand_name)
        if ext=='mp4':
            stream = ffmpeg.input(v)
            if w<h:    
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',720,1280)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,1920)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,2048)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')
            elif w>h:   
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',1280,720)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1920,1080)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',2048,1080)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')
            elif w==h:
                if formats=='1080p':
                    video = stream.filter('fps', fps,round='up').filter('scale',1080,1080)
                elif formats=='full_hd':
                    video = stream.filter('fps', fps,round='up').filter('scale',1920,1920)
                elif formats=='2k':
                    video = stream.filter('fps', fps,round='up').filter('scale',2048,2048)
                elif formats=='4k':
                    video = stream.filter('fps', fps,round='up')

            if mute == 'dont_mute':
                try:
                    audio = stream.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
                    stream = ffmpeg.output(audio,video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+random_timestamp)
                    ffmpeg.run(stream)
                except:
                    pass
            else:
                try:
                    stream = ffmpeg.output(video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+random_timestamp)
                    ffmpeg.run(stream)
                except:
                    pass
            try:
                md=os.path.abspath("static/assets/newVideo/"+full_name+".mp4")
                file = open(md, 'rb').read()
                with open(md, 'wb') as new_file:
                    new_file.write(file+'\0'.encode('ascii'))  
            except:
                pass

            if formats == '4k':
                final=VideoFileClip(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
                if w<h:
                    final=final.fx(vfx.resize,(2160,3840))
                elif w>h:
                    final=final.fx(vfx.resize,(3840,2160))
                elif w==h:
                    final=final.fx(vfx.resize,(2160,2160))
                final.write_videofile(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), fps = 30, codec = 'mpeg4')
            
            k=ff[i].folder
            y=Folder.objects.get(folder=k)
            oo=New_Metadata.objects.create(fold=y,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
            oo.save()


