import os
import sys
import subprocess
import random
try:
    import requests
    from random import choice as cc, randint as ref
    from threading import Thread as tt
    from bs4 import BeautifulSoup
    import time
    from user_agent import generate_user_agent
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    from rich.live import Live
    from faker import Faker
except:
    try:       
        os.system('pip install -r requirements.txt')
        os.system('clear')
        import requests
        from faker import Faker
        from random import choice as cc, randint as ref
        from threading import Thread as tt
        from bs4 import BeautifulSoup
        import time
        from user_agent import generate_user_agent
        from rich.console import Console
        from rich.table import Table
        from rich.text import Text
        from rich.live import Live
    except:
        try:
            os.system('pip install requests bs4 user_agent rich faker')
            os.system('clear')
            import requests
            from faker import Faker
            from random import choice as cc, randint as ref
            from threading import Thread as tt
            from bs4 import BeautifulSoup
            import time
            from user_agent import generate_user_agent
            from rich.console import Console
            from rich.table import Table
            from rich.text import Text
            from rich.live import Live
        except ImportError as e:
            print(f"Failed to install specific packages: {e}. Please install them manually.")
            sys.exit(1)


E = '\033[1;31m'
F = '\033[2;32m'  

class Dork:
    def __init__(self):
        
        self.hit = 0
        self.bb = 0
        self.erorr = 0

        
        os.system('clear')

        
        self.console = Console()
        self.table = Table(title=self.generate_title())

        
        self.table.add_column("Type", justify="center", style="cyan", no_wrap=True)
        self.table.add_column("Count", justify="center", style="magenta")

        
        self.table.add_row("Hits", Text(str(self.hit), style="green"))
        self.table.add_row("Bad", Text(str(self.bb), style="yellow"))
        self.table.add_row("Errors", Text(str(self.erorr), style="red"))
        self.table.add_row("Dev", "AHMED ~~ @maho_s9")

        
        self.live = Live(self.table, refresh_per_second=2, console=self.console)
        self.live.start()

    def generate_title(self):        
        color_code = random.randint(100, 300)
        return f"\x1b[38;5;{color_code}mGetting PaymentUrls\x1b[0m"

    def update_table(self):
        """Updates the table with the latest counts."""        
        self.table = Table(title=self.generate_title())

       
        self.table.add_column("Type", justify="center", style="cyan", no_wrap=True)
        self.table.add_column("Count", justify="center", style="magenta")

        
        self.table.add_row("Hits", Text(str(self.hit), style="green"))
        self.table.add_row("Bad", Text(str(self.bb), style="yellow"))
        self.table.add_row("Errors", Text(str(self.erorr), style="red"))
        self.table.add_row("Dev", "AHMED ~~ @maho_s9")

        self.live.update(self.table)

    def save(self, url, noa):
        """Saves the URL and payment method to a file."""
        try:
            with open('gate_pay.txt', 'a') as f:
                f.write(f"{url} ✓ {noa}\n")
        except Exception as e:
            print(E + f"Failed to save URL {url}: {e}" + F)
            self.erorr += 1
            self.update_table()

    def check_credit_card_payment(self, url):
        """Checks if the site has certain payment methods."""
        try:
            response = requests.get(url, timeout=10)
            payment_methods = {
                'stripe': 'Stripe',
                'cybersource': 'Cybersource',
                'paypal': 'Paypal',
                'authorize.net': 'Authorize.net',
                'bluepay': 'Bluepay',
                'magento': 'Magento',
                'woo': 'WooCommerce',
                'shopify': 'Shopify',
                'adyen': 'Adyen',
                'braintree': 'Braintree',
                'square': 'Square',
                'payflow': 'Payflow'
            }

            for key, value in payment_methods.items():
                if key in response.text.lower():
                    return value

            if 'payment by' in response.text.lower() or "credit card" in response.text.lower():
                return 'Generic Payment'

            return False
        except:
            self.erorr += 1
            self.update_table()
            return False

    def check_captcha(self, url):
        """Checks if the site has a CAPTCHA."""
        try:
            response = requests.get(url, timeout=10)
            captcha_type = [
                'https://www.google.com/recaptcha/api',
                'captcha',
                'verifyrecaptchatoken',
                'grecaptcha',
                'g-recaptcha',
                'www.google.com/recaptcha',
                'hcaptcha',
                'cloud'
            ]

            for cap in captcha_type:
                if cap in response.text.lower():
                    return True
            return False
        except:
            self.erorr += 1
            self.update_table()
            return False

    def doors(self):
        """Main function that generates URLs and processes them."""
        while True:
            try:
                rng = ref(1, 10)
                rda = "".join(cc('1234567890qwertyuiopasdfghjklzxcvbnm') for _ in range(rng))
                hh = cc(["cart.php", "price", "payment", "checkout", "addcart", "pay", "subscription"])
                
                self.Lol(rda, hh)
                
                keywords = [
                    'shop', 'رشق', 'تيك توك', 'Netflix', 'play', 'game', 'love', 'شدات',
                    'ببجي', 'شحن', 'رصيد', 'viwe', 'follower', 'instagram', "Facebook",
                    'توتير', 'like', 'دفع', 'pay', 'strip', 'clothe', 'ملابس',
                    'elctronic', 'كهربائيات', 'بيع', 'شراء', 'مصابيح', 'سيارات', 'اقمشه'
                ]

                pre_word = cc(keywords)             
                lan = ['ar', 'de_DE', 'es_ES', 'fr_FR', 'it_IT', 'ja_JP', 'ru_RU']
                for lo in lan:
                    fake = Faker(lo)
                    ass = (fake.word() + ' ' + fake.word())
                    pre = f"{pre_word} {ass}"
                    self.kill(pre)
                
            except:
                self.erorr += 1
                self.update_table()
                

    def Lol(self, rda, hh):
        """Generates and checks the constructed URL."""
        url = f"https://www.{rda}.com/{hh}"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'User-Agent': generate_user_agent()
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                payment = self.check_credit_card_payment(url)
                if payment:
                    captcha = self.check_captcha(url)
                    if not captcha:
                        self.hit += 1
                        self.save(url, payment)
                        self.update_table()
            else:
                self.bb += 1
                self.update_table()
        except:
            self.erorr += 1
            self.update_table()

    def kill(self, pre):
        """Searches for URLs using Google."""
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'User-Agent': generate_user_agent()
        }
        search_url = "https://www.google.com/search"
        params = {'q': pre, 'num': 25}

        try:
            response = requests.get(search_url, headers=headers, params=params)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = []
                for g in soup.find_all('div', class_='yuRUbf'):
                    a = g.find('a', href=True)
                    if a:
                        links.append(a['href'])

                for url in links:
                    payment = self.check_credit_card_payment(url)
                    if payment:
                        captcha = self.check_captcha(url)
                        if not captcha:
                            self.save(url, payment)
                            self.hit += 1
                            self.update_table()
            else:
                print(E + f"Bad search response for query: {pre} with status {response.status_code}" + F)
                self.bb += 1
                self.update_table()
        except Exception as e:
            print(E + f"Error searching with query {pre}: {e}" + F)
            self.erorr += 1
            self.update_table()

    def close_live(self):
        """Stops the Live context."""
        self.live.stop()

if __name__ == "__main__":
    dork = Dork()
    Threads = []
    try:
        for _ in range(3):
            t = tt(target=dork.doors)
            t.start()
            Threads.append(t)  
        for thread in Threads:
            thread.join()
    except KeyboardInterrupt:
        dork.close_live()
        exit(0)      
        print("\nProgram Finished by user.")
