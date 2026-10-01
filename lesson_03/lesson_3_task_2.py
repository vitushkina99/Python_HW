from lesson_03.smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 17 Pro Max", "+79029873074"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79027380445"),      
    Smartphone("Xiaomi", "POCO X8 Pro", "+79029915963"),      
    Smartphone("TECNO", "Spark 40 Pro", "+79022052853"),
    Smartphone("OnePlus", "15", "+79027912481"),    
           ]

for smartphone in catalog:
    print(f"{smartphone.brand}-{smartphone.model}.{smartphone.number}")

