library(plyr)
library(ggplot2)
setwd("/Users/Ziqi/Desktop/activity-log-data")
#maps: https://www.darrinward.com/lat-long/

#Users
users = read.csv("users_0826.csv",stringsAsFactors=FALSE)
count(users[substr(users$X_created_at,6,10)>="08-13",]$platform)

#Logs
logs = read.csv("logs_0826.csv",stringsAsFactors=FALSE)
recentlogs = logs[logs$date>="08/13",]
count(recentlogs[complete.cases(recentlogs) & (recentlogs$hsi>0),]$user)

#Tracks
tracks = read.csv("tracks_0826.csv",stringsAsFactors=FALSE)
recenttracks = tracks[substr(tracks$loctime,6,10)>="08/13",]
count(recenttracks[(recenttracks$lon!=0),])
count(recenttracks[complete.cases(recenttracks) & (recenttracks$lon!=0),])

#Track Time-series
newdata = recenttracks[complete.cases(recenttracks),]
ggplot(data = newdata[newdata$hsi>0,], aes(x = loctime, y = temp, color = user)) +
geom_line(aes(group = user))



