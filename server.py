import mysql.connector
import random

from flask import Flask, request, jsonify
import json

app = Flask(__name__)


"""Musteri tablosu
--------------
Id (int)
Ad (varchar)
Soyad (varchar)
Sehir (varchar)


CREATE_TABLE_Musteri= "CREATE TABLE Musteri \
                        (Id INT NOT NULL AUTO_INCREMENT, \
                        Ad VARCHAR(255) NOT NULL, \
                        Soyad VARCHAR(255) NOT NULL, \
                        Sehir VARCHAR(255) NOT NULL, \
                        PRIMARY KEY (Id)) \
                        "

"""



"""Sepet tablosu
----------
Id (int)
MusteriId (int)


CREATE_TABLE_Sepet= "CREATE TABLE Sepet \
                        (Id INT NOT NULL AUTO_INCREMENT, \
                        MusteriId INT NOT NULL, \
                        PRIMARY KEY (Id), \
                        FOREIGN KEY (MusteriId) REFERENCES Musteri(Id) ON DELETE CASCADE) \
                        "

"""


"""SepetUrun tablosu
--------------
Id (int)
SepetId (int)
Tutar (numeric)
Aciklama (varchar)


CREATE_TABLE_SepetUrun= "CREATE TABLE SepetUrun \
                        (Id INT NOT NULL AUTO_INCREMENT, \
                        SepetId INT NOT NULL, \
                        Tutar FLOAT NOT NULL, \
                        Aciklama VARCHAR(1024) , \
                        PRIMARY KEY (Id), \
                        FOREIGN KEY (SepetId) REFERENCES Sepet(Id) ON DELETE CASCADE) \
                        "
                        
"""




INSERT_Musteri = "INSERT INTO Musteri (Ad, Soyad, Sehir) VALUES (%s, %s, %s)"

def insert_musteri(info_tuple_list):
    
    for info_tuple in info_tuple_list:
        mycursor.execute(INSERT_Musteri, info_tuple)

    mydb.commit()
    
    #print(f"{len(info_tuple_list)} müşteri eklendi.")
    



def insert_musteri_return_ids(info_tuple_list):
    musteri_ids=[]
    
    for info_tuple in info_tuple_list:
        mycursor.execute(INSERT_Musteri, info_tuple)
        musteri_ids.append(mycursor.lastrowid)

    mydb.commit()
    
    #print(f"{len(info_tuple_list)} müşteri eklendi.")

    return musteri_ids


INSERT_Sepet = "INSERT INTO Sepet (MusteriId) VALUES (%s);"

def insert_sepet(info_tuple_list):
    
    for info_tuple in info_tuple_list:
        mycursor.execute(INSERT_Sepet, info_tuple)
        
        #print(f"{info_tuple[0]} Musteri Id'li, {mycursor.lastrowid} Id'li sepet eklendi.")

    mydb.commit()
    
    #print(f"{len(info_tuple_list)} sepet eklendi.")


def insert_sepet_return_ids(info_tuple_list):
    
    sepet_ids=[]
    
    for info_tuple in info_tuple_list:
        mycursor.execute(INSERT_Sepet, info_tuple)
        
        #print(f"{info_tuple[0]} Musteri Id'li, {mycursor.lastrowid} Id'li sepet eklendi.")
        sepet_ids.append(mycursor.lastrowid)

    mydb.commit()
    
    #print(f"{len(info_tuple_list)} sepet eklendi.")
    
    return sepet_ids

    

INSERT_SepetUrun = "INSERT INTO SepetUrun (SepetId,Tutar,Aciklama) VALUES (%s,%s,%s);"

def insert_sepeturun(info_tuple_list):
    
    for info_tuple in info_tuple_list:
        
        #print(info_tuple)
        mycursor.execute(INSERT_SepetUrun, info_tuple)
        
        #print(f"{info_tuple[0]} Sepet Id'li, {mycursor.lastrowid} Id'li urun eklendi.")

    mydb.commit()
    
    #print(f"{len(info_tuple_list)} urun eklendi.")

    
    
    
    
# select musteri

SELECT_musteri_all = "SELECT * FROM Musteri"
SELECT_musteri_ID = "SELECT * FROM Musteri Where Id = (%s)"

def select_musteri_all()  -> list:
    dict_list=[]
    
    mycursor.execute(SELECT_musteri_all)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"Ad":x[1],"Soyad":x[2],"Sehir":x[3]})
        
    return dict_list

def select_musteri_conditional_fetchone(sql,data_tuple)  -> dict:
    
    mycursor.execute(sql,data_tuple)

    result = mycursor.fetchone()
    
    return {"Id":result[0],"Ad":result[1],"Soyad":result[2],"Sehir":result[3]}


def select_musteri_custom_sql(sql) -> list:
    
    dict_list=[]
    
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"Ad":x[1],"Soyad":x[2],"Sehir":x[3]})
        
    return dict_list





# select sepet

SELECT_sepet_all = "SELECT * FROM Sepet"
SELECT_sepet_ID = "SELECT * FROM Sepet Where Id = (%s)"
SELECT_sepet_Musteri_ID = "SELECT * FROM Sepet Where MusteriId = (%s)"

def select_sepet_all()  -> list:
    dict_list=[]
    
    mycursor.execute(SELECT_sepet_all)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"MusteriId":x[1]})
        
    return dict_list

def select_sepet_conditional_fetchone(sql,data_tuple)  -> dict:
    
    mycursor.execute(sql,data_tuple)

    result = mycursor.fetchone()
    
    return {"Id":result[0],"MusteriId":result[1]}

def select_sepet_custom_sql(sql) -> list:
    
    dict_list=[]
    
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"MusteriId":x[1]})
        
    return dict_list




# select SepetUrun

SELECT_sepeturun_all = "SELECT * FROM SepetUrun"
SELECT_sepeturun_ID = "SELECT * FROM SepetUrun Where Id = (%s)"
SELECT_sepeturun_Sepet_ID = "SELECT * FROM SepetUrun Where SepetId = (%s)"

def select_sepeturun_all()  -> list:
    dict_list=[]
    
    mycursor.execute(SELECT_sepeturun_all)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"SepetId":x[1],"Tutar":x[2],"Aciklama":x[3]})
        
    return dict_list

def select_sepeturun_conditional_fetchone(sql,data_tuple)  -> dict:
    
    mycursor.execute(sql,data_tuple)

    result = mycursor.fetchone()
    
    return{"Id":result[0],"SepetId":result[1],"Tutar":result[2],"Aciklama":result[3]}

def select_sepeturun_custom_sql(sql) -> list:
    
    dict_list=[]
    
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        dict_list.append({"Id":x[0],"SepetId":x[1],"Tutar":x[2],"Aciklama":x[3]})
        
    return dict_list






def musteri_tutar_bul(sepetler,sepeturunler,MusteriId):

    
    
    toplam_tutar = 0
    sepet_adedi = 0
    
    for each_sepet in sepetler:
        
        if each_sepet["MusteriId"] == MusteriId:
            
            sepet_id=int(each_sepet["Id"])
            
            sepet_adedi += 1
            
            for each_sepeturun in sepeturunler:

                
                if int(each_sepeturun["SepetId"]) == sepet_id:
                    
                    toplam_tutar += int(each_sepeturun["Tutar"])
                    

                    
    return toplam_tutar,sepet_adedi

def server_SehirBazliAnalizYap():
    
    sepetler=select_sepet_all()

    sepeturunler=select_sepeturun_all()

    sehirler=["Ankara", "İstanbul", "İzmir", "Bursa", "Edirne", "Konya", "Antalya", "Diyarbakır", "Van", "Rize"]
    
    return_dct = {}
    
    for sehir in sehirler:
        return_dct[sehir]={"SehirAdi":sehir,"SepetAdet":0,"ToplamTutar":0}
    

    musteriler=select_musteri_custom_sql("Select * From Musteri")
    
    for musteri in musteriler:
        musteri_sehri = musteri["Sehir"]
        musteri_id = musteri["Id"]
        
        tutar,sepet_adedi=musteri_tutar_bul(sepetler,sepeturunler,musteri_id)
        
        return_dct[musteri_sehri]["ToplamTutar"] += tutar
        return_dct[musteri_sehri]["SepetAdet"] += sepet_adedi
        
    
    data_list=[] 
    
    for each_sehir in return_dct:
        if return_dct[each_sehir]["ToplamTutar"] != 0:
            data_list.append(return_dct[each_sehir])
            
    data_list.sort(key=lambda e : e["ToplamTutar"],reverse=True)
    
    return data_list
    
    


@app.route('/insert_musteri/', methods=['POST'])  ## accepts json
def http_insert_musteri():
    """
        musteri info yapisi:
        
        {"Ad":...,
        "Soyad":...,
        "Sehir":...}
    
    """
    info=request.json
    try:
        insert_musteri( [(info["Ad"],info["Soyad"],info["Sehir"])] )
    except Exception as e:
        print("[-] http_insert_musteri")
        print("[-] Hata Olustu.")
        return f"Musteri Eklenemedi. \n {str(e)}"
    
    return "Musteri Eklendi"



@app.route('/insert_musteri_with_ids/', methods=['POST'])  ## accepts json
def http_insert_musteri_with_ids():
    """
        musteri info yapisi:
        
        list of dicts
        
        [{"Ad":...,
        "Soyad":...,
        "Sehir":...}]
    
    """
    info_request=request.json
    
    tuple_list=[(info["Ad"],info["Soyad"],info["Sehir"]) for info in info_request]
    try:
        musteri_ids=insert_musteri_return_ids( tuple_list )
    except Exception as e:
        print("[-] http_insert_musteri")
        print("[-] Hata Olustu.")
        return "[]"
    
    return str(musteri_ids)
    
    
    
@app.route('/insert_sepet/', methods=['POST'])  ## accepts json
def http_insert_sepet():
    """
        sepet info yapisi:
        
        {"MusteriId":...}
    
    """
    info=request.json
    try:
        insert_sepet( [(info["MusteriId"],)] )
    except Exception as e:
        print("[-] http_insert_sepet")
        print("[-] Hata Olustu.")
        return f"Sepet Eklenemedi. \n {str(e)}"
    
    return "Sepet Eklendi"


@app.route('/http_insert_sepet_with_ids/', methods=['POST'])  ## accepts json
def http_insert_sepet_with_ids():
    """
        sepet info yapisi:
        
        {"MusteriId":...}
    
    """
    info_request=request.json
    tuple_list=[(info["MusteriId"],) for info in info_request]
    try:
        sepet_ids=insert_sepet_return_ids( tuple_list )
    except Exception as e:
        print("[-] insert_sepet_return_ids")
        print("[-] Hata Olustu.")
        return f"Sepet Eklenemedi. \n {str(e)}"
    
    return str(sepet_ids)



@app.route('/insert_sepeturun/', methods=['POST'])  ## accepts json
def http_insert_sepeturun():
    """
        sepet info yapisi:
        
        {"SepetId":...,
        "Tutar":...,
        "Aciklama":...}
    
    """
    info_request=request.json
    tuple_list=[(info["SepetId"],info["Tutar"],info["Aciklama"]) for info in info_request]
    try:
        insert_sepeturun( tuple_list )
    except Exception as e:
        print("[-] http_insert_sepeturun")
        print("[-] Hata Olustu.")
        return f"Sepet Urun Eklenemedi. \n {str(e)}"
    
    return "Sepet Urun Eklendi"


@app.route('/SehirBazliAnalizYap/', methods=['GET'])
def http_SehirBazliAnalizYap():

    
    
    return json.dumps(server_SehirBazliAnalizYap())

    
if __name__ == '__main__':

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
        database="mydatabase2"
    )
    
    mycursor = mydb.cursor(buffered=True)
    app.run(host='127.0.0.1', port=105)