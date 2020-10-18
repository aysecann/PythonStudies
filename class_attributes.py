# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:58:06 2020

@author: AyseCan
"""

#SINIFLAR(CLASS)


class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    diller = []
    
# Sınıfların özelliklerine erişmek
VeriBilimci.bolum
VeriBilimci.sql
VeriBilimci.diller

# Sınıfların özelliklerini değiştirmek
VeriBilimci.sql = 'Hayır'
VeriBilimci.sql

# Sınıf Örneklendirmesi / Birbirinden farklı nesne oluşturmak için / Instantiation

ali = VeriBilimci()
ali.sql = 'Evet'
ali.sql    
ali.diller.append("python")    
ali.diller
ali.bolum = 'CRM'
ali.bolum


veli = VeriBilimci()
veli.diller # Veli'ye henüz dil eklememize rağmen aliyle yaptığımız değişiklik sınıfı etkiledi.

# ÖRNEK ÖZELLİKLERİ : örneklerin her biri kendi içinde değişebilir bilgiler içermesi !!!

class DataScientist():
    diller = ["R","Python"] # bunu eklersek attribute error vermez!
    def __init__(self): # herbir örneğin kendi içinde değişen özelliklerden oluşabilen olmasını sağlarız.
        self.diller = []

ayse = DataScientist()
ayse.diller

esma = DataScientist()       
esma.diller

ayse.diller.append("Python,C")
ayse.diller

esma.diller
esma.diller.append("R")
esma.diller

DataScientist.diller # attribute error verir!! ; diller listesine r python eklenince vermez.

