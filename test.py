#-*- coding: utf-8 -*-
import moviepy.editor as mp

# this fileName is copied from audio-extract.txt 
# OSError: MoviePy error: the file /Users/stardust/git-repos/audio-extractor/【720P】Kate Bush - Cloudbusting.flv could not be found!
# Please check that you entered the correct path.
fileName = '/Users/stardust/git-repos/audio-extractor/【720P】Kate Bush - Cloudbusting.flv'
my_clip = mp.VideoFileClip(filename=fileName)                         
my_clip.audio.write_audiofile('Cloudbusting' + ".mp3")
my_clip.close()
