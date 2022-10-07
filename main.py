# © @riz4d
import requests as req
from pyrogram import *
from Config import *
from constant import base_url,type_url,help_msg


def base():   
    ur_req=req.get(base_url)
    url_js=ur_req.json()
    global activity
    activity=str(url_js['activity'])
    activity_type=str(url_js['type'])
    participants=str(url_js['participants'])
    global result
    result='Category : '+activity_type+'\n\nActivity : `'+activity+'`'



def education():
    cat='education'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_education
    var_education=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def recreational():
    cat='recreational'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_recreational
    var_recreational=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def social():
    cat='social'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_social
    var_social=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def diy():
    cat='diy'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_diy
    var_diy=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def charity():
    cat='charity'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_charity
    var_charity=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def cooking():
    cat='cooking'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_cooking
    var_cooking=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def relaxation():
    cat='relaxation'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_relaxation
    var_relaxation=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def music():
    cat='music'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_music
    var_music=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    
def busywork():
    cat='busywork'
    url=type_url+cat
    url_req=req.get(url)
    url_json=url_req.json()
    global var_busywork
    var_busywork=str('**Category : '+cat+'**\n\n`'+url_json['activity']+'`')
    

app=Client('find-a-hoby',
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN)



@app.on_message(filters.command('start'))
async def start_msg(client,message):
    
    await message.reply('__Hey **'+message.from_user.first_name+'**🙋🏻‍♀️__')
    await message.reply("__I'm [Hoby Bot](https://github.com/riz4d/Hoby-Bot)\n\n**Purpose** \n\nI can find a hoby for you while you're bored or ....__")
    await message.reply(" - /help :- __help menu__\n - /source :- __source code__")
@app.on_message(filters.command('random'))
async def random_msg(client,message):
    base()
    await message.reply('**'+result+'**')
    
@app.on_message(filters.command('help'))
async def random_msg(client,message):
    await message.reply(help_msg)
    
@app.on_message(filters.command('source'))
async def random_msg(client,message):
    await message.reply("Source Code : [Github Repo](https://github.com/riz4d/Hoby-Bot)")
    
@app.on_message(filters.command('education'))
async def edu_msg(client,message):
    education()
    await message.reply(var_education)

@app.on_message(filters.command('recreational'))
async def rec_msg(client,message):
    recreational()
    await message.reply(var_recreational)
    
@app.on_message(filters.command('social'))
async def soc_msg(client,message):
    social()
    await message.reply(var_social)
    
@app.on_message(filters.command('diy'))
async def diy_msg(client,message):
    diy()
    await message.reply(var_diy)   
    
@app.on_message(filters.command('charity'))
async def char_msg(client,message):
    charity()
    await message.reply(var_charity)  
    
@app.on_message(filters.command('cooking'))
async def cook_msg(client,message):
    cooking()
    await message.reply(var_cooking)  
    
@app.on_message(filters.command('relaxation'))
async def rela_msg(client,message):
    relaxation()
    await message.reply(var_relaxation)  
    
@app.on_message(filters.command('music'))
async def misc_msg(client,message):
    music()
    await message.reply(var_music)  
    
@app.on_message(filters.command('busywork'))
async def bcwrk_msg(client,message):
    busywork()
    await message.reply(var_busywork)  
    
@app.on_message(filters.text)
async def othr_msg(client,message):
    if message.text=='rizad':
        await message.reply('[@riz4d](https://t.me/riz4d) ,He is my master')
    else:
        await message.reply("**__I think u don't know to operate  me\n\n see help menu by using \n -**__ /help")
    

app.run()
