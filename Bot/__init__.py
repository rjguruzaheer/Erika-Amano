import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6004434070:AAFPRPWHTA_dVrlQnr27jajqkjvYReHtQGw') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 20738903)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', 'f14bc2de0f71c54d385ce25948058e52')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 800209209 5180429599))
MONGO_DB = os.environ.get("MONGO_DB", 'your mongodb') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001534093270)
BOT_NAME = os.environ.get('BOT_NAME', 'Alfeaon')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
