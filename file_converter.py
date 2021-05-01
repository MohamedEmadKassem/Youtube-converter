# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:43:12 2021

@author: moham
"""
from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()