from grab import *
from time import *


g = Grab()
buying_options = {
    'out_of_stock': '//*[@id="outOfStock"]/div/div[1]/span',
    'from_resellers': '//*[@id="availability"]/span/span[2]',
    'official_drop': '//*[@id="price_inside_buybox"]'
}
items = {
    'Ryzen5600x': 'https://www.amazon.com/dp/B08166SLDF',
    'Ryzen5800x': 'https://www.amazon.com/dp/B0815XFSGK',
    'Ryzen5900x': 'https://www.amazon.com/dp/B08164VTWH',
}
def parse_cost(link_to):
    g.go(link_to)
    return g.doc(buying_options["official_drop"]).text()
def parse_stock(link):
    g.go(link)
    try:
        if g.doc(buying_options["out_of_stock"]).text():
            return "OUT OF STOCK"
    except:
        try:
            if g.doc(buying_options["official_drop"]).text():
                return f"IN STOCK FROM OFFICIAL STORE {link}, {parse_cost(link)}"
        except:
            return "IN STOCK FROM RESELLERS"
while True:
    print("[AMAZON] Ryzen5600X: " + parse_stock(items["Ryzen5600x"]))
    sleep(3)
    print("[AMAZON] Ryzen5800X: " + parse_stock(items["Ryzen5800x"]))
    sleep(3)
    print("[AMAZON] Ryzen5900X: " + parse_stock(items["Ryzen5900x"]))