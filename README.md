# batch_subtitle
With this script and ffmpeg you can hard subbed your videos in a batch

# Setup:
First Install ffmpeg from https://ffmpeg.org/

Change the ffmpeg address and your desktop address in BAT and py file
# How to use:

1. Make a folder with name 1 on desktop for destination of final hard subbed videos

2. Make a folder with name 2 on desktop for making a name list of videos we want to make hardsub

3. Copy videos to bin folder of ffmpeg and rename them to v (select all of them press F2 and enter v)

4. Copy subs to bin folder of ffmpeg and rename them to s (select all of them press F2 and enter s)

5. open File_list Bat file for making a list of videos and save in list.txt

6. run ffmpeg command maker.py

7. Command.BAT  file will be created on your desktop open it with notepad and add this line to the first line of this and save this:           
cd ffmpeg_address/bin

8. run Command.BAT

9. after finishing process you can find your hard subbed videos with orginal names on folder 1 on your desktop
