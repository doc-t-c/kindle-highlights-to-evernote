# Parses APA format citation attachement sent from Kindle and puts data
# into evernote
# Ideal would be to automatically pull the data from Amazon, but they don't
# seem to support direct programmatic access at this time and scraping causes
# password issues so I am going with what seems to be the best path forward
# at the moment, which is to have the highlights emailed to me, save them in
# the highlights.html file and then run this script to convert to evernote

import re
import datetime

from transform_kindle_highlights_config import evernote_dev_token, evernote_sandbox_dev_token

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

'''
generate a dev token for using
https://www.evernote.com/api/DeveloperToken.action
then you can request it be converted to production once you have
completed testing
'''

# sandbox token for testing changes before moving to production
# client = EvernoteClient(token=evernote_sandbox_dev_token)

# for access to your own account, you can use the dev token and
# do not need to deal with oauth.
# Note that you need the additional parameters for the dev token to work properly
client = EvernoteClient(token=evernote_dev_token, sandbox=False, china=False)


userStore = client.get_user_store()
user = userStore.getUser()
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    if (n.name == 'Books') :
        books = n

newNote = Types.Note()
newNote.notebookGUID = books.guid

with open ('highlights.html','r', encoding='utf-8') as highlights : 
    with open ('reduced-highlights.txt', "w") as outputFile :
        l = highlights.readline()
        while l :
            l = l.strip()
            if (re.match('.*class="bookTitle".*',l)) :
                title = ''
                l = highlights.readline().strip()
                while (not (re.match ('.*</div>.*', l))) :                   
                    title += (l)
                    l = highlights.readline().strip()
                newNote.title = title
                newNote.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
                newNote.content += '<en-note>'
                outputFile.write (title + '\n') 
            elif (re.match('.*class="authors"', l)) :
                author = ''
                l = highlights.readline().strip()
                while (not (re.match ('</div>', l))) :
                    author += (l + ' ')
                    l = highlights.readline().strip()
                newNote.content += ('<h2>' + author + '</h2>')
                curDate = datetime.datetime.now() 
                newNote.content += ('<h2>' + curDate.strftime('%x')+ '</h2>')
                newNote.content += ('Key highlights: \n')
                newNote.content += '<ul>'
                outputFile.write (author + '\n')
                outputFile.write (curDate.strftime('%x')+'\n')
                outputFile.write ('Key highlights: \n')
            elif (re.match ('.*class="noteText"', l)) :
                note = ''
                l = highlights.readline().strip()
                while (not (re.match ('</div>', l))) :                    
                    note += (l)
                    l = highlights.readline().strip()
                newNote.content += ('<li>' + note + '</li>')
                outputFile.write (note + '\n')
            l = highlights.readline()

newNote.content += '</ul>'
newNote.content +='</en-note>'
newNote = noteStore.createNote (newNote)

