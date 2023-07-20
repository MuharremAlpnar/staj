#bu kısımda kütüphaneleri .py dosyasına yüklüyoruz
from gps import *
    #gpsden gelecek bilgiler için gereklidir
    #* işareti gps'modülünün içindeki bütün değişkenler veya fonksyonların da import edileceğini söyler
import time
    # Zamanla ilgili işlevleri sağlayan bir modüldür.


running = True
#running adlı bir değişkene true mantıksal değeri verildi

def getPositionData(gps):
    nx = gpsd.next()
    #GPS verilerinin sürekli güncellenmesini ve her defasında güncel veriyi almasını sağlar
    
    if nx['class'] == 'TPV':
        #gps'den bilgileri değişkenlere aktarıyoruz
        #GPS verilerinin kendi veri tipleri vardır bu ise TPVdir
        #veri akışı başladıktan sonra bu veriler TPV veri türündeyse bu if bloğunun içine girerek alt tarafdaki değişkenlere değerle verecektir.
        latitude = getattr(nx,'lat', "Unknown")
        #getattr fonksyonu ile nesnenin lat özelliğini latitude değişkenine atar. lat özelliği mevcut değilse Unknown değerini döndürür. aşağıdaki değerler de aynı şekilde verinin içerisinden istenilen özelliği çeker."getattr: get attribute"

        longitude = getattr(nx,'lon', "Unknown")
        

        #verilerin kaydedeceğimiz yerin adresini belirtiyoruz
        with open(r'/home/pi/Desktop/GPS/newoutput.txt', "a+") as file_object:
        # Bu mod, dosyanın sonuna veri eklemenize olanak sağlar ve dosya zaten varsa içeriği silmeden devam eder. Eğer dosya yoksa, yeni bir dosya oluşturulur.
            .
            file_object.seek(0)
            #fareyi dosyanın başına getirir
            
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            #dosyanın başında veri varsa o verini aşşağı satıra geçmesini ve yeni verinin ilk satırdan başlamasını sağlar
            
            
            info=" Position: lon = " + str(longitude) + ", lat = " + str(latitude)
            print (info)
            #txt dosyasına yazdırmak için info adında bir değişken tanımladı ve diğer değişkenleri buraya kaydetti

            #info değişkenini tanımladığımız dosyaya yazdırdı
            file_object.write(info)
            

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
#mode:veri akışını başlatmak ve verinin JSON formatında olmasını sağlar. bu değrler gps sınıfında oluşturulan gpsd nesnesinde tutulur


#hata yakalama sözdizimidir, except try'a dahildir
try:
    #hatanın oluşabileceği kod buraya yazılır
    print ("Application started!")
    while running:
        getPositionData(gpsd)
        time.sleep(1)
        #verilerin 1 sn aralıklarla güncellenmesini sağlar
        

except (KeyboardInterrupt):
    #hiçbir hata yoksa çalışacak kod
    running = False
    #CTRL-C KOMUTUYLA bir interript oluşturup running değişkenine false değeri vererek programı durdurur.
    