import praw
import config

messageTotal = open('message.txt', 'r').read()
message = ''.join(messageTotal.split('\n')[1:])
subject = open('message.txt', 'r').read().split('\n')[0]
recipients = open('recipients.txt', 'r').read().split()
messageCount = len(recipients)

reddit = praw.Reddit(client_id = config.client_id, 
                     client_secret = config.client_secret, 
                     user_agent = config.user_agent, 
                     username = config.username,  
                     password = config.password
                    )

for recipient in recipients:
  reddit.redditor(config.username)
  reddit.redditor(recipient).message(subject, message)

print('Message sent to ',messageCount, ' reddit users.')


