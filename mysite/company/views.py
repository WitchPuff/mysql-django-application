from django.shortcuts import render, redirect, HttpResponse
# from .models
import pymysql
import time
from django.views.decorators.csrf import csrf_exempt
from .models import Admins, Dealers, Customer
from django.db import connection

models = {'Chevrolet':('Redline','Malibu','Waldo','Cavalier','Captiva','Cruze'),
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
brands = models.keys()
tables = ('customer','deal','dealer_inventory',
            'dealers','engines','options','plant_inventory',
            'price','transmissions','vehicle')
def query(q):
    with connection.cursor() as cur:
        cur.execute(q)
        data = cur.fetchall()
    columns = [col[0] for col in cur.description]
    keys = dict(zip(columns, data[0])).keys()
    return data,keys

# Create your views here.
def home(request):
    ret = []
    if request.method == 'GET':
        q = f"select brand,model,style,price from vehicle natural join deal natural join price where deal_date >= '2015-01-01' and deal_date <= '2015-12-31' GROUP BY brand,model,style ORDER BY count(vin) DESC LIMIT 6"
        data,keys = query(q)
        for index,i in enumerate(data,1):
            a = f"/static/img/car{index}.jpg"
            ret.append({'car':' '.join(i[:-1]),'price':int(i[-1]),'img':a})
        return render(request, 'home.html',{'ret':ret})
    return render(request, 'home.html',{'ret':ret})

def admin(req):
    msg = ''
    data = {}
    q = ''
    keys = ''
    if req.method == "POST":
        q = req.POST.get("query",None)
        try:
            data,keys = query(q)
        except:
            msg = 'Error!'
    return render(req,'admin.html',{'data':data,'msg':msg,'query':q,'keys':keys})

def adminLogin(req):
    msg = ''
    if req.method == "POST":
        id = req.POST.get("name",None)
        pwd = req.POST.get("pwd",None)
        if not len(Admins.objects.filter(admin_name=id)):
            msg = "Admin Not Exist."
        elif not len(Admins.objects.filter(admin_name=id, passwd=pwd)):
            msg = "Password Error!"
        else:
            return redirect("http://127.0.0.1:8000/admin")
    return render(req, 'adminLogin.html',{'msg':msg})

def dealer(req):
    msg = ''
    data = {}
    keys = ''
    brand = model = style = ''
    if req.method == "POST":
        brand = req.POST.get("brand",None)
        model = req.POST.get("model",None)
        style = req.POST.get("style",None)
        if brand not in brands or model not in models[brand] or style not in styles:
            msg = 'No such choice.'
        else:
            q = f"select dealer_name as dealer,count(vin) as inventory from dealer_inventory natural join vehicle where vin not in (select vin from deal) and brand='{brand}' and model='{model}' and style='{style}' group by dealer_name"
            try:
                data,keys = query(q)
            except:
                msg = 'Error!'
    return render(req, 'dealer.html',{'msg':msg,'models':models,'styles':styles,'data':data,'keys':keys,'brand':brand,'model':model,'style':style})

def dealerLogin(req):
    msg = ''
    if req.method == "POST":
        id = req.POST.get("id",None)
        pwd = req.POST.get("pwd",None)
        print(Dealers.objects.all())
        if not len(Dealers.objects.filter(dealer_id=id)):
            msg = "Dealer Not Exist. Please register first."
        elif not len(Dealers.objects.filter(dealer_id=id, dlpasswd=pwd)):
            msg = "Password Error!"
        else:
            dealer_id = id
            return redirect("http://127.0.0.1:8000/dealer")
    return render(req, 'dealerLogin.html',{'msg':msg})

def dealerReg(req):
    msg = ''
    if req.method == "POST":
        id = req.POST.get("id",None)
        name = req.POST.get("name",None)
        pwd = req.POST.get("pwd",None)
        if not len(Dealers.objects.filter(dealer_id=id)):
            Dealers.objects.create(dealer_id=id,dealer_name=name,dlpasswd=pwd)
            msg = f"Dealer ID {id} successfully registered!"
            return redirect("http://127.0.0.1:8000/dealerLogin")
        else:
            msg = f"Dealer ID {id} already exists!"
    return render(req, 'dealerReg.html',{'msg':msg})

def search(req):
    msg = ''
    data = {}
    key = ''
    brand = model = style = ''
    if req.method == "POST":
        brand = req.POST.get("brand",None)
        model = req.POST.get("model",None)
        style = req.POST.get("style",None)
        if brand not in brands or model not in models[brand] or style not in styles:
            msg = 'No such choice.'
        else:
            q = f"select dealer_name as dealer,count(vin) as inventory,price as 'price($)' from dealer_inventory natural join vehicle natural join price where vin not in (select vin from deal) and brand='{brand}' and model='{model}' and style='{style}' group by dealer_name"
            try:
                data,key = query(q)
            except:
                msg = 'Error!'
    return render(req, 'search.html',{'msg':msg,'models':models,'styles':styles,'data':data,'keys':key,'brand':brand,'model':model,'style':style})

def customerSurvey(req):
    msg = ''
    if req.method == "POST":
        id = int(list(Customer.objects.all().values("cust_id"))[-1]["cust_id"])
        id += 1
        id = str(id)
        print(id)
        name = req.POST.get("name",None)
        address = req.POST.get("address",None)
        phone = req.POST.get("phone",None)
        gender = req.POST.get("gender",None)
        income = req.POST.get("income",None)
        if not len(Customer.objects.filter(cust_id=id)):
            Customer.objects.create(cust_id=id,cust_name=name,address=address,phone=phone,gender=gender,annual_income=int(income))
            msg = "Thanks for your cooperation!"
            return redirect("http://127.0.0.1:8000/search/")
        else:
            msg = f"Customer ID {id} already exists!"
    return render(req, 'custReg.html',{'msg':msg})

def market(req):
    msg = ''
    q = data = keys = ''
    if req.method == "POST":
        sl = req.POST.get("select",None)
        fr = req.POST.get("from",None)
        where = req.POST.get("where",None)
        group = req.POST.get("group",None)
        order = req.POST.get("order",None)
        if sl and fr and where and group and order:
            q = f"select {sl} from {fr} where {where} group by {group} order by {order} desc"
        elif fr and where and group:
            q = f"select {sl} from {fr} where {where} group by {group}"
        elif fr and where:
            q = f"select {sl} from {fr} where {where}"
        elif fr and sl:
            q = f"select {sl} from {fr}"
        else:
            msg = 'Invalid Input!'
        if q:
            try:
                data,keys = query(q)
            except:
                msg = 'Error!'
    return render(req,'market.html',{'msg':msg,'tables':tables,'data':data,'keys':keys,'query':q})
