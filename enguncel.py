from gps import *
import time


running = True

def getPositionData(gps):
    nx = gpsd.next()
    
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        
        with open(r'dosya adresi', "a+") as file_object:
            
            file_object.seek(0)
            
            
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
                     
            
            info=" Position: lon = " + str(longitude) + ", lat = " + str(latitude)
            print (info)
            
            file_object.write(info)
            

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print ("Application started!")
    while running:
        getPositionData(gpsd)
        time.sleep(1)
       
        

except (KeyboardInterrupt):
    running = False
   