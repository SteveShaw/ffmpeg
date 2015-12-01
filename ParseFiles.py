# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:11:53 2015

@author: jshao
"""

import string 
import os
import sys

def concat_files(input,sep='@'):
    video_map = {}
    cmd_list = []
    with open(input,'r') as f:
        for l in f:
            path_name = string.rstrip(l)
            path_dir, path_file = os.path.split(path_name)
            video_items = path_file.split(sep)
            if len(video_items) == 2:
                serial_no = video_items[0]
                if serial_no not in video_map.keys():
                    video_map[serial_no] = []
                video_map[serial_no].append(path_name)
    for serial_no in video_map.keys():
        print serial_no
        print video_map[serial_no]
        pre, ext = os.path.splitext(video_map[serial_no][0])
        with open(r'.\jobs\%s.txt'%serial_no, 'w+') as f:
            for item in video_map[serial_no]:
                f.write("file '%s'\n"%item)
            cmd_list.append('ffmpeg -f concat -i %s.txt -c copy %s%s'%(serial_no,serial_no,ext))
            cmd_list.append('ffprobe -v quiet -show_format -show_streams %s%s >> videos_info.txt'%(serial_no,ext))
    return cmd_list

def gen_thumbnails_video(input,interval=2):
    cmd_list = []
    with open(input,'r') as f:
        for l in f:
            path_name = string.rstrip(l)
            path_dir,path_file=os.path.split(path_name)
            file_name,file_ext=os.path.splitext(path_file)
            print file_name, file_ext
            #generate thumbnail_images for each minute
            directory = './jobs/%s'%(file_name)
            if not os.path.exists(directory):
                os.mkdir(directory)
            cmd = 'ffmpeg -i "%s" -vf fps=1/30 %s/%%%%03d.png'%(path_name,file_name)
            cmd_list.append(cmd)
            #generate preview video by showing each picture for interval minutes
            cmd = r'ffmpeg -framerate %d/3 -i "%s/%%%%03d.png" -c:v libx264 -r 30 -pix_fmt yuv420p %s.Preview.mp4'%(interval, file_name, file_name)
            cmd_list.append(cmd)
    return cmd_list
    
def gen_video_info(input):
    cmd_list = []
    with open(input,'r') as f:
        for l in f:
            full_path = string.rstrip(l)
            cmd = 'ffprobe -v quiet -print_format json -show_format -show_streams "%s" >> videos_info.json'%full_path
            cmd_list.append(cmd)
    return cmd_list
            
#c -- concat video files
#r -- generate preview video
#normal usage: ParseFiles <input file> <option>
if __name__=='__main__':
    fun_map = {}
    fun_map['c'] = concat_files
    fun_map['r'] = gen_thumbnails_video
    fun_map['v'] = gen_video_info
    pass    
    input_file = 'av_files.txt'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    option = 'c'
    if len(sys.argv) > 2:
        option = sys.argv[2]

    cmd_list = fun_map[option](input_file)
    with open(r'c:\study\jobs\jobs_%s.bat'%option,'w+') as f:
        for cmd in cmd_list:
            f.write('%s\n'%cmd)
        
            
