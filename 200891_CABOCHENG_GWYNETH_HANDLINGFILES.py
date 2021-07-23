# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
# CODE CELL
# PROBLEM 1
def get_product(code):
    return products[code]
# CODE CELL
# PROBLEM 2
def get_property(code,property):
    return products[code][property]

# CODE CELL
# PROBLEM 3
def main():
    with open("receipt.txt","a+") as f:
        total=0
        y=0
        orders={}
        f.write("\n==\n")
        f.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
        while True:
            order=input("{product_code},{quantity}: ")
            
            if order!="/":
                code=order.split(",")[0]
                quantity=int(order.split(",")[1])
                subtotal=get_property(code,"price")*int(quantity)
                registered=code in orders
                total+=subtotal
                if registered==True:
                    orders[code]["quantity"]+=quantity
                    orders[code]["subtotal"]+=subtotal
                    
                else:
                    orders[code]=get_product(code)
                    orders[code]["quantity"]=quantity
                    orders[code]["subtotal"]=subtotal
            else:
                orders_sort=sorted(orders)
                while y<len(orders):
                    f.write(orders_sort[y]+"\t\t")
                    if len(list(orders[orders_sort[y]]["name"]))>8:
                        f.write(orders[orders_sort[y]]["name"]+"\t\t")
                    else:  
                        f.write("\t"+orders[orders_sort[y]]["name"]+"\t\t\t")
                    f.write(str(orders[orders_sort[y]]["quantity"])+"\t\t\t")
                    f.write(str(orders[orders_sort[y]]["subtotal"])+"\n")
                    y+=1
                f.write("\nTotal:\t\t\t\t\t\t\t\t\t"+str(total))
                f.write("\n==")
                f.close()
                break
main()

