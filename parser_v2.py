from grab import *
import colorama
from colorama import Fore
from time import *
from pydub import AudioSegment
from pydub.playback import play
colorama.init()
g = Grab()
settings_question = input("Юзать прокси? y/n ")
security_question = input('Использовать звуковое оповещение? y/n ')
song = AudioSegment.from_wav("sound.wav")
if security_question == 'y' or security_question == 'н':
    print("хорошо")
else:
    print("ладно")
if settings_question.lower() == "y" or settings_question.lower() == "н":
    #g.setup(proxy='88.99.220.218:1080', proxy_type='socks5', connect_timeout=5, timeout=5)
    g.proxylist.load_file('proxi.txt', proxy_type='socks5', connect_timeout=5, timeout=5)
    print("ок")
elif settings_question.lower() == "n" or settings_question.lower() == "т":
    pass
else:
    print("не ок")
    pass
buying_options = {
    'out_of_stock': '//*[@id="outOfStock"]/div/div[1]/span',
    'official_drop': '//*[@id="submit.add-to-cart"]',
    'cannot_ship': '//*[@id="deliveryMessageMirId"]/span',
    'price': '//*[@id="price_inside_buybox"]', 
    'product_name': '//*[@id="productTitle"]'
}
items = open('items_to_parse.txt', 'r').read().split('\n')  
prices = []
def parse_cost():
    return g.doc(buying_options["price"]).text()

def parse_stock(link):
    try:
        try:
            if g.doc(buying_options["official_drop"]).text() or g.doc(buying_options["cannot_ship"]).text():
                return f"{Fore.GREEN}IN STOCK {link} {parse_cost()}"
        except:
            return f"{Fore.RED}OUT OF STOCK"
    except:
        return f"{Fore.YELLOW}CONNECTION TIMEOUT"
def parse_name():
    try:
        return g.doc(buying_options["product_name"]).text()
    except:
        return "CANNOT GET ITEM_NAME"
while True:
    for item in range(len(items)):
        g.go(items[item])
        sleep(2)
        quantity = parse_stock(items[item])
        if quantity.find('IN STOCK') != -1 and security_question == 'y' or security_question == 'н':
            play(song)
        print(f"{Fore.BLUE}[AMAZON] {Fore.WHITE}{parse_name()}: {parse_stock(items[item])}{Fore.WHITE}")