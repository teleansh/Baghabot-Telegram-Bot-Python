from telegram import*
from telegram.ext import*
import random as r
import praw


api="...."  # <<< add your bot's API token here

bot=Bot(api)

updater=Updater(b,use_context=True)
ds= updater.dispatcher


#reddit details
reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')


def memes(update:Update,context:CallbackContext):
	sublists = ['terriblefacebookmemes','2meirl4meirl','marvelmemes','Memes_of_the_dank','fffffffuuuuuuuuuuuu','BikiniBottomTwitter','me_irl','memes','dankmemes','antimeme','shitposting','comedyheaven','wholesomememes','MemesIRL']
	subreddit = reddit.subreddit(r.choice(sublists))
	random_post=posts[r.randint(0, 49)]
	if (".gif" in random_post.url):
        	bot.sendAnimation(chat_id = update.effective_chat.id,animation = random_post.url,caption = random_post.title+' (r/'+str(subreddit)+')')
	else:
		bot.sendPhoto(chat_id = update.effective_chat.id,photo = random_post.url,caption = random_post.title+' (r/'+str(subreddit)+')')


def intro(update:Update,context:CallbackContext):
	bot.send_message(chat_id=update.effective_chat.id,text=("Hello Seth Ji , Myself Bhageshwar Undhaiwala"))
	bot.send_photo(chat_id=update.effective_chat.id,photo='https://static.toiimg.com/thumb/msid-84669263,imgsize-527899,width-800,height-600,resizemode-75/84669263.jpg')

def cele(update:Update,context:CallbackContext):
    celelist=['https://c.tenor.com/bXwaPdcTgc8AAAAM/jethalal-funny-dance-tarak-mehta-ka-ooltah-chashmah.gif'
              , 'https://c.tenor.com/KWO0NRq_zHoAAAAC/congratulations-and-celebrations-bagha-nattu-kaka.gif' 
              , 'https://c.tenor.com/dZZJ7m3a3lwAAAAM/jetha-jethalal-champaklal-gada.gif'
              , 'https://c.tenor.com/-MaYk8xpYCQAAAAd/tmkoc.gif']
    
    bot.sendAnimation(chat_id=update.effective_chat.id,animation=r.choice(celelist))
	
def hi(update:Update,context:CallbackContext):
    hilist=['https://c.tenor.com/3rXzVicDEQ0AAAAM/kem-palty-wave.gif']
    
    bot.sendAnimation(chat_id=update.effective_chat.id,animation=r.choice(hilist))

def sad(update:Update,context:CallbackContext):
    sadlist=['https://c.tenor.com/gZ9CSDfVg6kAAAAd/jethalal-tmkoc.gif' , 'https://c.tenor.com/FqCZEtnZp10AAAAd/jethalal-jethalal-face-expression.gif',
             'https://c.tenor.com/QzJbUMt9krEAAAAM/jethalal-tmkoc.gif']
    
    bot.sendAnimation(chat_id=update.effective_chat.id,animation=r.choice(sadlist))

def shock(update:Update,context:CallbackContext):
    shock=['https://c.tenor.com/j-f-vaSz3egAAAAM/denial-heart.gif' , 'https://c.tenor.com/fVBphFK19H8AAAAd/jethalal-jethalal-shocked.gif',
             'https://c.tenor.com/dNx_eOiwN54AAAAM/jethalal-tmkoc.gif' , 'https://c.tenor.com/Ksa41lPMsssAAAAM/jethalal-tmkoc.gif'
             ]
    
    bot.sendAnimation(chat_id=update.effective_chat.id,animation=r.choice(shock))    

def angry(update:Update,context:CallbackContext):
    angry=['https://c.tenor.com/EQ1eDjBvEwsAAAAM/champak-champaklal.gif' , 'https://c.tenor.com/5ABfcvboCSIAAAAC/champaklal-champak-angry.gif',
             'https://c.tenor.com/njujsDup0ugAAAAC/champaklal-champak.gif' , 'https://c.tenor.com/E7d3w2yf7HgAAAAC/champaklal-champak.gif'
             , 'https://c.tenor.com/96H5g9JcobEAAAAM/jethalal-angry-tarak-mehta-ka-ooltah-chashmah.gif' , 'https://c.tenor.com/58ELO44SbFoAAAAd/angry-jethalal-beating-goli-punishment.gif'
             'https://c.tenor.com/yZq0zVvWKysAAAAC/chup-jethalal.gif', 'https://c.tenor.com/My0ftntIPr4AAAAC/jethalal-tmkoc.gif','https://c.tenor.com/ubf3OOZEjacAAAAM/champaklal-champak.gif']
    
    bot.sendAnimation(chat_id=update.effective_chat.id,animation=r.choice(angry))   
 
def pd(update:Update,context:CallbackContext):
    pdl=['Yes' , 'absolutely no' , 'a big NO' , 'maybe' , 'depends on your hardwork' , 'chances are 50%' , 'i dont think so , sorry' , 'i think it will' ,'my 6th sense says yes']
    bot.send_message(chat_id=update.effective_chat.id,text=r.choice(pdl))   

def ship(update:Update,context:CallbackContext):

    
    shipt=str(r.randint(1,100)) + "%"
    bot.send_message(chat_id=update.effective_chat.id,text=shipt)      

def help(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text="Commands :\n/intro\n/celebrate\n/hi\n/sad\n/shock\n/angry\n/predict\n/ship")   
    
def status(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text="I am alive")   

ds.add_handler(CommandHandler('intro',intro))
ds.add_handler(CommandHandler('start',intro))
ds.add_handler(CommandHandler('celebrate',cele))
ds.add_handler(CommandHandler('hi',hi))
ds.add_handler(CommandHandler('sad',sad))
ds.add_handler(CommandHandler('shock',shock))
ds.add_handler(CommandHandler('angry',angry))
ds.add_handler(CommandHandler('predict',pd))
ds.add_handler(CommandHandler('ship',ship))
ds.add_handler(CommandHandler('help',help))
ds.add_handler(CommandHandler('status',status))



updater.start_polling()

