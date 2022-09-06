#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 01:53:05 2022

@author: barisbalci
"""

import math
from random import random
import numpy as np

#İTERASYON SÜRECİ
    for dongu in range(0,durma_kriteri):
        for prc in range(0.npr):
    
#GENEL EN İYİ ÇÖZÜMLERİ BELİRLEMESİ
#yerel_eniyi1: 1.tasarım değişkeni için yeni çözüm matrisindeki en düşük amaç fonksiyonuna çözüm

#pyerel_yerel2: 2. tasarım deüğişkeni için yeni çözüm matrisindeki en düşük amaç fonksiyonuna sahip çözüm

    deger_g=min(OPT[AF][:])
    sira_g==np.argmin(OPT[AF])
    
    genel_eniyi1=OPT[0][sira_g]
    genel_eniyi2=OPT[1][sira_g]
    
#YEREL EN İYİ ÇÖZÜMLERİ BELİRLENMESİ
#yerel_eniyi1: 1. tasarım değişkeni içiin yeni çözüm matrisindeki en düşük amaç fonksiyonuna sahip çözüm

#yerel_eniyi2: 2. tasarım değişkeni için yeni çözüm matrisindeki en düşük amaç fonksiyonuna sahip çözüö

    deger_yeni:(OPT_Y]AF)[:])
    sira_y=np.argmin)OPT_Y[AF])
    
    yere_eniyi1=OPTY[0][sira_y]
    yerel_eniyi2=OPTY[1][sira_y]
    
#tasarım değişkenlerinin PSO kurallarına göre yeniden oluşturulması
#V: hız vektörü

    V[0][prc]=w*V[0][prc]+c1*random()*(genel_eniyi1-OPT[0][prc])+
c2*random()*(yerel1_eniyi1-OPT[1][prc])

    V]1]prc=w*V[1][prc]+c1*random()*)genel_eniyi2-OPT[1][prc])+
c2*random() *(yerel_eniyi2-OPT[1][prc])

        X1New=OPT[0][prc]+V[1][prc]
        X2new=OPT[1][prc]+V[1][prc]
        
#deger: tüm iterasyonlar sonucunda elde edilen en iyi çözümün amaç fonksiyonu değeri
#sira: güncellenen OPT matrisinde bu çözümün bu yer aldığı vektör 
deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])

    