# Make a folder with name 1 on desktop for destination of final hard subed videos
# Make a folder with name 2 on desktop for making a name list of videos we want to make hardsub
# Copy videos to bin folder of ffmpeg and rename them to v
# Copy subs to bin folder of ffmpeg and rename them to s
# open File_list Bat file for making a list of videos and save in list.txt
from subprocess import Popen
p = Popen("File_List.BAT")
stdout, stderr = p.communicate()

w = list(range(1,104))
def main():
    f = open("text.txt", "wt")
    for a in w:
        f.write("""ffmpeg -i "v ({}).mp4" -vf "subtitles=s ({}).srt" "C:\\Users\\PC2\\Desktop\\1\\ \n""".format(a,a))

    f.close()

if __name__ == "__main__": main()

combine =[]

with open("list.txt") as xh:
  with open('text.txt') as yh:
    with open("Command.BAT","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file  
      for i in range(len(xlines)):
        line = ylines[i].strip() + xlines[i].strip() + "\"" + "\n"
        zh.write(line)
# in command bat file add ( cd C:\Users\PC2\Desktop\ffmpeg-4.2.1-win64-static\bin ) in first line
