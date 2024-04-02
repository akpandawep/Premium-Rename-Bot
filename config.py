import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22287041") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "c149386dcd58a40fa9fe60e632e161d4") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6590068990:AAG1uI2CHAvISuEBnyZAzQ5jwpbGQFtohPc") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "BQDa-FcAUUgvpOJGhG1jCLDDyOfLofOcw_21dQUUKWhhAu1DSxawig4rSftvpTskthbf_wCdKk-xpISCPMgaPNltTqC7QUch8I-fXkwCMHSuj84puhV0LRBGVSHRLXgWwppW1uyLYKQ9fkPN8lkpP-M8-mDHIV3nvTdP5-3DUQaS5trFAamM0JWBS-S39TGX89Som6Ex-2DcjckPCmPNvjA7WiyrX4pewKKlfrvbU_44UZxFEQq1NbHIDX07f--adYmQ6SuDMfWYaA6lQx599fr4HwGhaRgWjdYnQkKeETwpLwFZCzX3LSKQZlHsnTtgREvkXb6EVh7gvGQOQnvc2fkyb3kRyAAAAAGJzmhsAA") #⚠️ Required 
    STRING_API_ID = os.environ.get("STRING_API_ID", "22287041") # ⚠️ Required
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "c149386dcd58a40fa9fe60e632e161d4") # ⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Premium_Data")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6141937812').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Rokubotz") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001869105126")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
