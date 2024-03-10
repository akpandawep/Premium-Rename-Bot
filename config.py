import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23941369") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7180148674:AAG4gO8_GTGBbIqq38yS7OgYfkHXDvw7Cb4") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "") #⚠️ Required 
    STRING_API_ID = os.environ.get("STRING_API_ID", "23941369") # ⚠️ Required
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd") # ⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Premium_Data")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1966867320').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Rokubotz") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002046934698")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
