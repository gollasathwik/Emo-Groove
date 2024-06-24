import shutil
import pandas as pd
import numpy as np

songs = pd.read_csv(r"D:\Semester\SEM 4\Facesongsproject\rf_predicted.csv")
song_names = songs.loc[:,["song_name","class"]]

folder_angry = r"D:\Semester\SEM 4\Facesongsproject\Folders\Angry"
folder_sad = r"D:\Semester\SEM 4\Facesongsproject\Folders\Sad"
folder_relax = r"D:\Semester\SEM 4\Facesongsproject\Folders\Neutral"
folder_happy = r"D:\Semester\SEM 4\Facesongsproject\Folders\Happy"

song_src = "D:\\Semester\\songs"

for i in range(len(song_names.index)):
    name = song_names.loc[i][0]
    if(song_names.loc[i][1]=='happy'):
        des=folder_happy
    elif(song_names.loc[i][1]=='sad'):
        des=folder_sad
    elif(song_names.loc[i][1]=='angry'):
        des=folder_angry
    elif(song_names.loc[i][1]=='relax'):
        des=folder_relax
    source = song_src + '\\' + name
    shutil.copy(source,des)
