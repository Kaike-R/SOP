import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from threading import Thread

import time

def Media(x,y):
    i=0
    time.sleep(0.1)
    while(cotac[0][l] != null)
    	i=i+1
	if(cotac[1] = y)
	    cont=cont+1
	    conf=conf+cotac[i][3]
    conft=conf/cont

def Escrever(x):
    arquivo = open("cota.txt","w")
    arquivo.write(str(x))
csv = "Brasil.csv"
cotac = pd.read_csv(csv)
key = True

while key == True:
    y =  datetime.date(datetime.today).isocalendar()[1] 
    compY= y-1
    if compY<=0 
        compY=51
    media = Thread(target=Media,args=[cotac,y])
    mediaC = Thread(target=Media,args=[cotac,compY])
    media.start()
    mediaC.start()
    resul=mediaC-media
    if (resul <=0)
        resul = "Queda"
    else
	resul = "Subida"
    Escrever(resul)    
        time.sleep(1.5)






