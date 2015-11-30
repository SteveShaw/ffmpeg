rem ffmpeg -i DVD14/VIDEO_TS/VTS_01_1.VOB -map 0:v -map 0:a -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.0 -c:a libvo_aacenc DVD13_01.mp4
REM ffmpeg -i DVD14/VIDEO_TS/VTS_02_1.VOB -map 0:v -map 0:a -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.0 -c:a libvo_aacenc DVD13_02.mp4
REM ffmpeg -i DVD14/VIDEO_TS/VTS_03_1.VOB -map 0:v -map 0:a -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.0 -c:a libvo_aacenc DVD13_03.mp4
REM ffmpeg -i DVD14/VIDEO_TS/VTS_04_1.VOB -map 0:v -map 0:a -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.0 -c:a libvo_aacenc DVD13_04.mp4
ffmpeg -ss 00:1:00 -i "caribpr-100815_389-high1.mp4" -c:v libx264 -crf 21 -preset slow -profile:v high -vf scale=960:-1 -c:a copy out.mp4