# reddit-messager

Getting Started
1. git clone https://github.com/williamrmyers/reddit-messager
2. pip install praw
3. Create a file in the root directory called `config.py` with the below contents:

```
client_id=''
client_secret=''
user_agent=''
username=''
password=''
```

## Messages

### Subject
The first line of the file  will be used as the subject.

The rest of the message starts at the second line, and goes on indefinitely. 

## Recipients
recipients.txt
Contains the message recipiants. The file is a list of Reddit usernames deliminated by a return. (Just put each username on new line.)


