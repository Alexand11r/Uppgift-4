import csv
import os
import locale
import time

       #lista
def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []    
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products 

def view_products(products):
     for index, products in enumerate(products):
         print()

def list_all_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx} {product['name']} {product['price']} {product['desc']} {product['price']}")

def add_product(products,):
   found_max = max(products, key=lambda id: id['id'])
   max_id = found_max['id']
   new_id = max_id + 1
   name = input("Namn: ")
   desc = input("Beskrivning:")
   price = float(input("Pris:"))
   quantity = int(input("Antal: "))
   
   product = {}
   
   product['id'] = new_id
   product['name'] = name
   product['desc'] = desc
   product['price'] = price
   product['quantity'] = quantity
   
   products.append(product)
   print(f"Produkt har lagt till!")
   
def remove_product(products):
    remove_id = int(input("Vilken produkt vill du ta bort? (ange ID): "))
    for i, product in enumerate(products):
        if product['id'] == remove_id:
            removed = products.pop(i)
            print(f"Produkten '{removed['name']}' har tagits bort.")
            return
    print("Produkt finns inte.")
        
    
 
#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')

os.system('cls')
list_all_products(products)

while True:
    print("\n1. Visa produkter\n2. Lägg till produkt\n3. Ta bort produkt\n4. Välj produkt\n5. Avsluta")
    choice = input("Välj: ")
    if choice == "1":
        list_all_products(products)
    elif choice == "2":
        add_product(products)
    elif choice == "3":
        remove_product(products)
    elif choice == "4":
        idx = int(input("Välj produkt: "))
        if 1 <= idx <= len(products):
            product = products[idx-1]
            print(f"ID: {product['id']}\n Namn: {product['name']} \nBeskrivning: {product['desc']} \n Pris: {product['price']} \n Kvantitet: {product['quantity']}")
        else:
            print("Ogiltigt nummer.")
    elif choice == "5":
        break

