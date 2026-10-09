#!/usr/bin/env bash
# 用法: ./make-vertical.sh a.png b.png c.png title.ttf body.ttf out.mp4
ffmpeg -y -f lavfi -i "color=c=0x0f1220:s=1080x1920:d=6:r=30" \
  -loop 1 -t 6 -i "$1" -loop 1 -t 6 -i "$2" -loop 1 -t 6 -i "$3" \
  -filter_complex "[1]scale=300:300[r];[2]scale=300:300[g];[3]scale=300:300[f];\
[0][r]overlay=x=140:y='900+60*sin(2*PI*t)':shortest=1[a];\
[a][g]overlay=x=390:y='900+60*sin(2*PI*t+2)':shortest=1[b];\
[b][f]overlay=x=640:y='900+60*sin(2*PI*t+4)':shortest=1[c];\
[c]drawtext=fontfile=$4:text='你的标题':fontsize=120:fontcolor=white:x=(w-tw)/2:y=420:alpha='min(1,t)',\
drawtext=fontfile=$5:text='你的副标题':fontsize=48:fontcolor=0xffd166:x=(w-tw)/2:y=1450" \
  -t 6 -c:v libx264 -pix_fmt yuv420p "$6"
