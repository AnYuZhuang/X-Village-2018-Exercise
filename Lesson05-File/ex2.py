import csv
with open('aqi.csv','r',encoding='utf-8-sig') as f:       #'utf-8-sig'
    reader=csv.reader(f)
    
    x=60
    
    for row in reader:
        aqi=row[2]         
        if aqi!='AQI':       #排除AQI
          if int(aqi)<x:
            x=int(aqi)
            y=row[0]
            z=row[1]
    print(y,z,"空氣最好")
    print("AQI是",x)

    
    