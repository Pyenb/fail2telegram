from fail2ban.server.actions import ActionBase
import requests, json

class telegramAction(ActionBase):
    def __init__(self, jail, name):
        self.installpath = '/etc/fail2ban/action.d/'
        try: self.config = json.loads(open(self.installpath + 'telegram_config.json', 'r').read())
        except Exception as e: print(f'Config file not found: {e}')
        self.token = self.config['telegram_api_token']
        self.get_chat_id()

    def get_chat_id(self):
        self.chat_id = self.config['telegram_chat_id']
        if self.chat_id == '' or self.chat_id == None:
            try:
                self.chat_id = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates').json()['result'][0]['message']['chat']['id']
                self.config['telegram_chat_id'] = self.chat_id
                open(self.installpath + 'telegram_config.json', 'w').write(json.dumps(str(self.config))).close()
            except Exception as e:
                self.get_chat_id()
                print(f'Logged: {e}')
        print(f'Got chat ID: {self.chat_id}')
        
    def send_message(self, message):
        try: requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage', params={"chat_id": self.chat_id, "text": message})
        except Exception as e:
            self.send_message(message)
            print(f'Logged: {e}')
    
    def start(self):
        self.send_message("Fail2ban started")
    
    def stop(self):
        self.send_message("Fail2ban stopped")
        
    def ban(self, aInfo):
        location = self.get_location(aInfo['ip'])
        self.send_message(f"{aInfo['ip']} from {location} banned.")
        
    def get_location(self, ip):
        response = requests.get(f'https://ipapi.co/{ip}/json/').json()
        return response['country_name']

Action = telegramAction