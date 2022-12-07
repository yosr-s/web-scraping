from bs4 import BeautifulSoup
import requests
import re
import requests
from pprint import pprint
from twilio.rest import Client

app=input("sasir le nom de l'appareil que vous cherchez:")
prix=int(input("saisir le prix"))
msg="hey, "+app+" is under "+str(prix)+" TND!"
def send(msg):
    account_sid="AC0e5bcf4fafd8593d2cc24faa941a25dc"
    auth_token="0ec54481f204ccfb541f7bbe88b22c03"
    twilio_number="+19088276738"
    my_number="+21656899869"
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body=msg,
        from_=twilio_number,
        to=my_number)


items_found={}
l=[]
l1=[]
l2=[]
ch=""
url="https://www.jumia.com.tn/catalog/?q=smartphones"
page=requests.get(url).text
doc=BeautifulSoup(page,"html.parser")
page_text=doc.find_all(class_="pg")
pages=str(page_text).split(";")[-1]
pages1=str(pages).split("#")[0]
pages2=str(pages1).split("=")[1]
print(pages2)
x=int(pages2)
search="samsung"
#items=doc.find_all(text=re.compile(search))
#print(items)
for page in range(1,x+1):
    url = "https://www.jumia.com.tn/catalog/?q=smartphones&page="+str(page)+"catalog-listing"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    #avoir div qui contient les produits
    div=doc.find(class_="-paxs row _no-g _4cl-3cm-shs")
    #filtrer les samsung dans div
    search=app
    items=div.find_all(text=re.compile(search))
    #filtrer les prix des samsung
    for item in items:
        parent1=item.parent
        #print(parent1)
        parent2=parent1.parent
        price=parent2.div.string
        l=price.split()
        price=l[0]
        l1=price.split(".")
        price=l1[0]
        print(price)
        l2.append(price)
        items_found[item]={"price":price}
print(items_found)
print(l2)
for i in range(len(l2)):
    if l2[i]=="Boutique":
        l2[i]=0
    else:
        if "," in l2[i]:
            ch=""
            for j in range(len(l2[i])):
                if l2[i][j]!=",":
                    ch=ch+l2[i][j]
            l2[i]=int(ch)
print(l2)
for i in range(len(l2)):
    l2[i]=int(l2[i])
l2.sort()

print(l2)

for i in range(len(l2)):
    if l2[i]!=0:
        if l2[i]<prix:
            send(msg)
            break

