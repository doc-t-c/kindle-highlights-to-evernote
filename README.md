This program takes the highlight html file generated from exporting the Kindle highlignts and converts it to a note in Evernote. Note that this only works for accessing your own Evernote account, it will not let you access someone elses account (which would require oauth). 

This will work on both the free and paid versions of Evernote. For the free version, however, you will need to make sure you are not logged in on 2 other devices (eq phone and web browser) as the free version limits the number of connections allowed at one time). Since that can be a bit of a pain, a simple hack to get around that limit is to create an Evernote account dedicated to these book highlights and then share the notebook from that account with your primary Evernote account. That way you will always be able to connect and will have your highlights easily accessible on your primary account.  

Dependencies: 
This requires installing the Evernote python clients so they can be imported within python


Setting up with Evernote: 
You will need to establish an "application" with Evernote. This will allow you to get the tokens you need to interact with Evernote programmatically. The application process generates a public key and a secret id. You won't actually need that for using this script, but you will want to keep them in a safe place so you can access your account in the future (in particular, when you get the tokens). 

Once you have the account, you can generate a sandbox token by going to 
	https://www.evernote.com/api/DeveloperToken.action 
Once you have completed testing, you can request a dev token. This can take a week or so for processing. 
The dev token expires every 12 months, and you will need to go to 
	https://dev.evernote.com/get-token/ 
and use your secret key to gene

After generating these tokens, you store them in a configuration file. 
The default config file is named transform_kindle_highlights_config.py and contains 2 lines
	evernote_sandbox_dev_token = "your evernote sandbox token"
	evernote_dev_token = 'your evernote dev token' 


Getting the Kindle highlights: 
There are several ways that you can get your highlights from your Kindle. This script assumes that you have the resulting html file locally stored. 

What I have found easiest in practice is to generate that html file from the device and email it to myself. It seems awkward, but works pretty easily. On my device (a Kindle Fire) I double-tap to get to the book overview view, and then click on the "My Notebook" icon at the top (page with the corner folded). Once I am in My Notebook, I have access to the highlights I have made. I then tap the share icon, select export notebook, chose APA style, confirm the export, and then email the exported file to myself. 

Once I get the email on my computer, I save the attachment in the highlights.html file in the same directory that I have this script. 

Running the script: 
If the highlights.html file and the config file are all in the same directory (or you have updated the script so it knows where to find them) you can simply execute the script. It will generate a local copy of the highlights in the file reduced-highlights.txt. 

It will also create a note in the "Books" notebook associated with your account. If you don't have a Books notebook, it will create the note in the default notebook. This new note will be available effectively immediately in most cases, but may take up to a minute to be visible in the account. 

The format of the note is: 
	<Book Title> (as the note title) 
	<Author> (medium header) 
	<Today's date> (medium header) 

	Key highlights: 
	<All of your highlights as a bulleted list, one bullet per highlight> 


Support: 
This script is not actively supported. I use and will update it when it breaks for me, but I am not planning on providing active support for it. 
