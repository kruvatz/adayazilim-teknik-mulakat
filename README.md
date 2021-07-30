# adayazilim-teknik-mulakat
database


mysql installation : pip install mysql-connector-python

TestVerisiOlustur(musteriAdet, sepetAdet) : database'e random sekilde istenen adetlerde urun eklemesi yapar.

SehirBazliAnalizYap() : sehir bazlı analiz

Örnek response:

```python
[ {'SehirAdi': 'Edirne', 'SepetAdet': 724, 'ToplamTutar': 1193425},
  {'SehirAdi': 'Van', 'SepetAdet': 664, 'ToplamTutar': 1087681},
  {'SehirAdi': 'Konya', 'SepetAdet': 398, 'ToplamTutar': 660751},
  {'SehirAdi': 'Bursa', 'SepetAdet': 282, 'ToplamTutar': 494902},
  {'SehirAdi': 'İzmir', 'SepetAdet': 291, 'ToplamTutar': 475543},
  {'SehirAdi': 'Rize', 'SepetAdet': 181, 'ToplamTutar': 297845},
  {'SehirAdi': 'Antalya', 'SepetAdet': 140, 'ToplamTutar': 224019},
  {'SehirAdi': 'Ankara', 'SepetAdet': 121, 'ToplamTutar': 195296},
  {'SehirAdi': 'Diyarbakır', 'SepetAdet': 98, 'ToplamTutar': 166081},
  {'SehirAdi': 'İstanbul', 'SepetAdet': 1, 'ToplamTutar': 2390}]
```
