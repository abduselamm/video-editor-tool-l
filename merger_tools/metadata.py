#from .views import * 
import ffmpeg
import random
from .models import *
import os
from datetime import datetime
from moviepy.editor import *
import hashlib

def metadata_changer(v,v_name,spin,mute,foldr,formats):
    
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
    if s[-1].lower() not in ['k','m']:
        s=''
    viral=s

    name='assazz5s'
    full_name=name
    if viral != '':
        full_name=viral+'_'+full_name
    print(full_name)
    for i in range(spin):
        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)

        N = 8
        #name = ''.join(random.choices(string.ascii_uppercase +
		#					string.digits, k=N))
        full_name+=str(rand_name)
        print(full_name)
        stream = ffmpeg.input(v)
        if formats=='1080p':
            w1=720
            h1=1280
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='full_hd':
            w1=1080
            h1=1920
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='2k':
            w1=1080
            h1=2048
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='4k':
            video = stream.filter('fps', fps,round='up')

        if mute == 'dont_mute':
            try:
                audio = stream.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
                stream = ffmpeg.output(audio,video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+str(datetime.now()))
                ffmpeg.run(stream)
            except:
                pass
        else:
            try:
                stream = ffmpeg.output(video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+str(datetime.now()))
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
            final=final.fx(vfx.resize,(2160,3840))
            final.write_videofile(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), fps = 30, codec = 'mpeg4')
        
        ff=Folder.objects.get(folder=foldr)
        oo=New_Metadata.objects.create(fold=ff,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
        oo.save()
        


def metadata_changer_byc(v,v_name,spin,mute,formats):
    
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
    
    if s[-1].lower() not in ['k','m']:
        s=''
    viral=s

    name='assazz5s'
    full_name=name
    if viral != '':
        full_name=viral+'_'+full_name
    print(full_name)

    ff=Folder.objects.all()
    for i in range(spin):
        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)

        N = 8
        #name = ''.join(random.choices(string.ascii_uppercase +
		#					string.digits, k=N))
        full_name+=str(rand_name)
        print(full_name)
        stream = ffmpeg.input(v)
        if formats=='1080p':
            w1=720
            h1=1280
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='full_hd':
            w1=1080
            h1=1920
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='2k':
            w1=1080
            h1=2048
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='4k':
            video = stream.filter('fps', fps,round='up')
        
        if mute == 'dont_mute':
            try:
                audio = stream.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
                stream = ffmpeg.output(audio,video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+str(datetime.now()))
                ffmpeg.run(stream)
            except:
                pass
        else:
            try:
                stream = ffmpeg.output(video, os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), metadata='creation_time='+str(datetime.now()))
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
            final=final.fx(vfx.resize,(2160,3840))
            final.write_videofile(os.path.abspath("static/assets/newVideo/"+full_name+".mp4"), fps = 30, codec = 'mpeg4')
        
        k=ff[i].folder
        y=Folder.objects.get(folder=k)
        oo=New_Metadata.objects.create(fold=y,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
        oo.save()


