library(plyr)
library(ggmap)
library(googleway)
setwd("/Users/Ziqi/Desktop/geocoding")

#df = read.csv("AssistanceDetailWithDemographics 5.1-current.csv",stringsAsFactors=FALSE)
#df = read.csv("AssistanceDetailWithDemographics 5.1-4.30.16.csv",stringsAsFactors=FALSE)
#df = read.csv("AssistanceDetailWithDemographics 5.1-4.30.17.csv",stringsAsFactors=FALSE)
###17
df = read.csv("AssistanceDetailWithDemographics 5.1-4.30.18.csv",stringsAsFactors=FALSE)

phx_list = c("Phx","Phoenix ","Phjx","Phoeix ","Phoeniz","Phoenx ","Pheonix","Phoeinx","Px","Phownix ","Phoneix","Px," ,"Pgoenix","phoenix","Phoenox","Phoeniz","Phoenxi","Pheonix ","Phoenixc","Phoeinix","Phoenx","Pheoenix","Pjoenix","Phoeniz ","Phoenix")

df[df$City %in% phx_list,]$City = "Phoenix"
for (i in seq(1:dim(df)[1]))(
df$Address[i] = strsplit(df$Address[i], "#")[[1]][1]
)

df$full_address = paste(df$Address,df$City,df$State, sep=",")
#Geocode on unique addresses
unq = data.frame(unique(df$full_address))
colnames(unq) = "full_address"
unq$full_address = as.character(unq$full_address)
unq$lat = NA
unq$lon = NA
key = "my_google_geocode_api_key"

for (i in c(1:dim(unq)[1])){
    print(i)
    loc = google_geocode(address = unq$full_address[i], simplify = T,key=key)
    unq[i,]$lat = loc$results$geometry$location$lat
    unq[i,]$lon = loc$results$geometry$location$lng
}

geocoded = merge(df, unq,by="full_address",all.x=T)
write.csv("geocoded.csv",geocoded,row.names=F)

