from chatterbotapi import ChatterBotFactory, ChatterBotType
from random import randint

factory = ChatterBotFactory()
randint = randint(0,1)

# JabberWacky temporarily removed from the bot_list. It returns HTML instead of text.
bot_list = ['ChatterBotType.CLEVERBOT','ChatterBotType.PANDORABOTS']
if randint == '1': 
    bot1 = factory.create(ChatterBotType.PANDORABOT, 'b0dafd24ee35a477')
    bot1session = bot1.create_session()
else:
     bot1 = factory.create(ChatterBotType.CLEVERBOT)
     bot1session = bot1.create_session()
try:
    print 'Welcome to chatbot. Press Ctrl + C to exit chat at any time.'
    s = raw_input('You>: ')
    while(1):

        s = bot1session.think(s)
        print 'bot2> ' + s

        s = raw_input('You> ')
except KeyboardInterrupt:
    print 'Cheerio!'
    
