import requests
import json
import random
import string

sehirler=["Ankara", "İstanbul", "İzmir", "Bursa", "Edirne", "Konya", "Antalya", "Diyarbakır", "Van", "Rize"]

def x_y_dagit(x,y):
    dagitim=[]
    
    for e in range(x):
        tmp_y = random.randint(0,y)
        dagitim.append(tmp_y)
        y-=tmp_y
    return dagitim

def TestVerisiOlustur(musteriAdet, sepetAdet): #(int musteriAdet, int sepetAdet)
    
    musteri_list=[{"Ad":"".join(random.sample(string.ascii_letters,random.randint(5,20))), "Soyad":"".join(random.sample(string.ascii_letters,random.randint(5,20))),"Sehir":random.choice(sehirler)} for e in range(musteriAdet)]
    

    musteri_ids=requests.post("http://127.0.0.1:105/insert_musteri_with_ids/",json=musteri_list).json()
    
    sepet_list=[]
    
    dagitim=x_y_dagit(musteriAdet,sepetAdet)
    

    for musteri_id,musteri_idye_gore_adet in zip(musteri_ids,dagitim):
        for adet in range(musteri_idye_gore_adet):
            sepet_list.append({"MusteriId":musteri_id})
            
    sepet_ids=requests.post("http://127.0.0.1:105/http_insert_sepet_with_ids/",json=sepet_list).json()

    sepeturun_list=[]
    
    for sepet_id in sepet_ids:
        #1-5 arasında 
        adet=random.randint(1,5)
        
        tmp_sepeturun_list=[{"SepetId":sepet_id , "Tutar":random.randint(100,1000), "Aciklama": "".join(random.sample(string.ascii_letters,20))  } for e in range(adet)]
        
        sepeturun_list.extend(tmp_sepeturun_list)
    
    resp=requests.post("http://127.0.0.1:105/insert_sepeturun/",json=sepeturun_list)
    
    return True


def SehirBazliAnalizYap():
    return requests.get("http://127.0.0.1:105/SehirBazliAnalizYap/").json()




if __name__ == "__main__":
    test_resp=TestVerisiOlustur(100,1000)
    analiz_resp=SehirBazliAnalizYap()
    
    print(f"Analiz Sonucu: \n {analiz_resp}")