import os
import re
import json
import discord
from logic.calendarLogic import CalendarLogic

with open('config.json', 'r') as f:
    config = json.load(f)
    discordToken = config['discord'].get('token')
    calendarText = config['calendar'].get('calendar_text')
    listText = config['calendar'].get('list_text')
    addEventText = config['calendar'].get('add_event_text')
    addLongEventText = config['calendar'].get('add_long_event_text')
    deleteEventText = config['calendar'].get('delete_text')

client = discord.Client(ws = int(os.environ.get('PORT', 5000)))

@client.event
async def on_ready():
    print('READY')

@client.event
async def on_message(message):
    content = message.content

    if content == calendarText:
        logic = CalendarLogic()
        result = logic.calendarUrl()

    if content == listText:
        logic = CalendarLogic()
        result = logic.get()
        
    elif re.search(addEventText, content):
        event = content.replace(addEventText, '')
        logic = CalendarLogic()
        logic.insert(event)

    elif re.search(addLongEventText, content):
        event = content.replace(addLongEventText, '')
        logic = CalendarLogic()
        logic.insertLongEvent(event)

    elif re.search(deleteEventText, content):
        eventId = content.replace(deleteEventText, '')
        logic = CalendarLogic()
        logic.delete(eventId)

client.run(discordToken)

