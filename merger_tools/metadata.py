#from .views import * 
import ffmpeg
from io import BytesIO
import random
from .models import *
import os
from datetime import datetime
from moviepy.editor import *
import hashlib

def metadata_changer(v,v_name,spin,mute,foldr,formats):
    
    x=v_name

    s=''
    for k in x:
        if k.isdigit() or k=='.':
            if k=='.':
                s+=k
            else:
                s=s+k
        else:
            if k.lower() in ['k','m']:
                s=s+k
                break
            else:
                s=''
    fl=False
    if s[:-1]:
        try:
            float(s[:-1])
            fl=True
        except ValueError:
            pass
    viral=''
    if fl and s[-1].lower() in ['k','m']:
        viral=s  
        
    viral=''
    vid = VideoFileClip(v)
    w,h=vid.size
    print(w,h)
    #print(ffmpeg.probe(v))
    for i in range(spin):
        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)

        N = 8
        #name = ''.join(random.choices(string.ascii_uppercase +
		#					string.digits, k=N))
        name='assazz5s'
        full_name=str(name)+str(rand_name)
        if viral != '':
            full_name=viral+'_'+str(name)+str(rand_name)
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
            w=1080
            h=2048
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='4k':
            w=2160
            h=3840
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        
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
                print()
            except:
                pass
        md=os.path.abspath("static/assets/newVideo/"+full_name+".mp4")
        file = open(md, 'rb').read()
        with open(md, 'wb') as new_file:
            new_file.write(file+'\0'.encode('ascii'))  
        
        #print(ffmpeg.probe())
        #print(full_name,foldr)
        ff=Folder.objects.get(folder=foldr)
        oo=New_Metadata.objects.create(fold=ff,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
        oo.save()
        
    '''
    if 'creation_time' in vid['streams'][0]['tags']:
        print(vid['streams'][0]['tags']['creation_time']) 
    #ffmpeg.input('testsrc=size=192x108:rate=1:duration=10', f='lavfi').output('in.mp4').overwrite_output().run()
    ffmpeg.input(v).output('out.mp4', metadata='size=3200000', map=0, c='copy').overwrite_output().run()
    #ffmpeg -i input.mp4 -vf scale=-1:720 output.mp4
    # ffprobe -print_format json -show_format out.mp4'''


def metadata_changer_byc(v,v_name,spin,mute,formats):
    
    x=v_name
    s=''
    t=False
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
    fl=False
    if s[:-1]:
        try:
            float(s[:-1])
            fl=True
        except ValueError:
            pass
    viral=''
    if fl and s[-1].lower() in ['k','m']:
        viral=s  
        
    viral=''
    vid = VideoFileClip(v)
    w,h=vid.size
    print(w,h)
    #print(ffmpeg.probe(v))
    ff=Folder.objects.all()
    for i in range(spin):
        rand_name = random.randrange(12000000,28000000)
        fps=random.randrange(20,30)

        N = 8
        #name = ''.join(random.choices(string.ascii_uppercase +
		#					string.digits, k=N))
        name='assazz5s'
        full_name=str(name)+str(rand_name)
        if viral != '':
            full_name=viral+'_'+str(name)+str(rand_name)
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
            w=1080
            h=2048
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        elif formats=='4k':
            w=2160
            h=3840
            video = stream.filter('fps', fps,round='up').filter('scale',w1,h1)
        
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
                print()
            except:
                pass
        md=os.path.abspath("static/assets/newVideo/"+full_name+".mp4")
        file = open(md, 'rb').read()

        with open(md, 'wb') as new_file:
            new_file.write(file+'\0'.encode('ascii'))  
        
        
        k=ff[i].folder
        print(k,full_name)
        y=Folder.objects.get(folder=k)
        oo=New_Metadata.objects.create(fold=y,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
        oo.save()
        #print(ffmpeg.probe())
        #print(full_name,foldr)
        #ff=Folder.objects.get(folder=foldr)
        #oo=New_Metadata.objects.create(fold=ff,new_video=os.path.abspath("static/assets/newVideo/"+full_name+".mp4"))
        #oo.save()
        
    """
    if 'creation_time' in vid['streams'][0]['tags']:
        print(vid['streams'][0]['tags']['creation_time']) 
    #ffmpeg.input('testsrc=size=192x108:rate=1:duration=10', f='lavfi').output('in.mp4').overwrite_output().run()
    ffmpeg.input(v).output('out.mp4', metadata='size=3200000', map=0, c='copy').overwrite_output().run()
    #ffmpeg -i input.mp4 -vf scale=-1:720 output.mp4
    # ffprobe -print_format json -show_format out.mp4"""

