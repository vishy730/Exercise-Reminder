import webbrowser
import time
# open web browser every 30 minute
current_time = time.ctime() # get current time
print ("start time = " + current_time)
breaks = 0 
while(breaks<5): # how many times it should remind you
    time.sleep(1500) # break for every 25 minutes pomodoro technique
	# video that we wanted to play
    url="https://www.youtube.com/watch?v=at7QvbFy9fM"
    # opens the url
	webbrowser.open(url)
    breaks=breaks+1
    print ("current time = " + time.ctime())