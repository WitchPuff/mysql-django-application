company = 'General Motors'
brands = {'Chevrolet':('Redline','Malibu','Waldo','Cavalier','Captiva','Cruze'),
          'Pontiac':('Sunfire','Grand am','Grand Prix','Bonnevi 11e'),
          'Buick':('Enclave','LaCrosse','Lucerne'),
          'Cadillac':('Evoq','Imaj','Vizon','Cien','Sixteen','Ciel'),
          'Saturn':('Carla','Jasper','GM EV1','lon','Aura','Flextreme'),
          'Hummer':('H1','H2','H3'),
          'Saab':('Saab9-4X','Ursaab','Saab 9-X Air','Saab 98'),
          'Holden':('Monaro','Commondore'),
          'Vauxhall':('DX','Meriva'),
          'Opel':('Aglia','Corsa','Astra','Insignia','Meriva','Zafira','Antara','Combo')
          }
styles = ('4-door', 'Wagon','SUV')

dealers = (('00001','Mike'),('09302','Jane'),('03842','Yoko'),('39284','Phoebe'),('46237','Camille'),('58292','Kim'),('10294','Harry'))
plants = (('04721','Bjork'),('23842','Obito'),('34521','Kks'),('73821','Carino'),('01283','Sisley'))
suppliers = (('48290','John'),('10384','Arthur'),('68291','Daniel'),('01924','Rin'),('03912','Greta'))
colors = ('Green','Black','White','Silver','Pink','Purple','Yellow','Red','Blue')
names = []
with open('car/name_list.txt','r') as f:
    for i in f.readlines():
        names.append(i.replace('\n',''))
cities = []
with open('car/city_list.txt','r') as f:
    for i in f.readlines():
        cities.append(i.replace('\n',''))
import random
import time

a1=(2010,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2015,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

def random_time(a,b):
    t=random.randint(a,b)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串
    return t,date
egn = []
tsm = []
def supplier(k):
    egiter = random.sample(range(10000,99999),k)
    tmiter = random.sample(range(10000,99999),k)

    # supplier
    for i in range(k):
        # engine
        engine = 'EG'+str(random.randint(100,131))
        id,name = random.choice(suppliers)
        eg,egd = random_time(start,end)
        supplier1 = (str(egiter[i]),engine,id,name,egd,eg)
        if supplier1 in egn:
            
            continue
        # transmission
        id,name = random.choice(suppliers)
        transmission = 'TM'+str(random.randint(150,199))
        tm,tmd = random_time(start,end)
        supplier2 = (str(tmiter[i]),transmission,id,name,tmd,tm)
        if supplier2 in tsm:
            
            continue

        egn.append(supplier1)
        tsm.append(supplier2)
        with open('relations.sql','a') as f:
            f.write(f'insert into engines values {supplier1[:-1]};\n')
            f.write(f'insert into transmissions values {supplier2[:-1]};\n')
    print('Supplier generated!')

vehicles = []
options = []
plant_inventory = []
prices = []
def cars(k):
    vin = random.sample(range(100000,999999),k)

    for v in vin:
        brand = random.choice(list(brands.keys()))
        model = random.choice(brands[brand])
        style = random.choice(styles)
        vehicle = (v,brand,model,style)
        howmuch = random.randint(1000,999999)
        price = (brand,model,style,howmuch)
        if vehicle in vehicles:
            continue
        

        color = random.choice(colors)
        engine = random.choice(egn)
        trans = random.choice(tsm)
        option = (v,color,engine[0],trans[0])
        if option in options:
            
            continue

        t,date = random_time(max(engine[-1],trans[-1]),end)
        id,name = random.choice(plants)
        plant = (id,name,date,v,t)
        if plant in plant_inventory:
            
            continue

        vehicles.append(vehicle)
        with open('relations.sql','a') as f:
            f.write(f'insert into vehicle values {vehicle};\n')
        if price[:-1] not in prices:
            prices.append(price[:-1])
            with open('relations.sql','a') as f:
                f.write(f'insert into price values {price};\n')
        options.append(option)
        with open('relations.sql','a') as f:
            f.write(f'insert into options values {option};\n')
        plant_inventory.append(plant)
        with open('relations.sql','a') as f:
            f.write(f'insert into plant_inventory values {plant[:-1]};\n')
    print('Vehicles generated!')

dealer_inventory = []
deal = []
customer = []
def deals(k):
    for i in range(k):
        id,name = random.choice(dealers)
        _, _, _, vin,build_date = random.choice(plant_inventory)
        t,date = random_time(build_date,end)
        dealer = (id,name,date,vin)
        if dealer in dealer_inventory:
            
            continue
        dealer_inventory.append(dealer)
        with open('relations.sql','a') as f:
            f.write(f'insert into dealer_inventory values {dealer};\n')
        is_sold = random.choice((0,1))
        if is_sold:
            t,date = random_time(t,end)
            name = random.choice(names)
            cust = str(names.index(name)+10000)
            d = (date,id,cust,vin)
            if d in deal:
                
                continue 

            city = random.choice(cities)
            phone = str(random.randint(1000000000,9999999999))
            gender = random.choice(('Male','Female'))
            annual_income = random.randint(0,9999999)
            c = (cust,name,city,phone,gender,annual_income)
            if c[:1] in customer:
                
                continue


            deal.append(d)
            with open('relations.sql','a') as f:
                f.write(f'insert into deal values {deal[-1]};\n')
            customer.append(c[:1])
            with open('relations.sql','a') as f:
                f.write(f'insert into customer values {c};\n')

    print('Deals generated!')
    
def dealer():
    with open('relations.sql','a') as f:
        for i in dealer:
            st = f'insert into dealers value ("{i[0]}","{i[1]}","{"test"}");\n'
            f.write(st)

def generate():
    dealer()
    print('Supplier generating...')
    supplier(800)
    print('Vehicles generating...')
    cars(40000)
    print('Deals generating...')
    deals(30000)

generate()

            