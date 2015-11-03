# trello2text


[![Fury](https://badge.fury.io/py/trello2text.png)](http://badge.fury.io/py/trello2text)


[![travis.ci](https://travis-ci.org/cirinoalejando/trello2text.png?branch=master)](https://travis-ci.org/cirinoalejando/trello2text)


[![pypy](https://pypip.in/d/trello2text/badge.png)](https://crate.io/packages/trello2text?version=latest)


# Trello Board List Output to Text
for now outputs to console in a  format suitable for MoinMoin Wiki

## Useful links:

* Trello API:
https://developers.trello.com/get-started
https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-lists
* Trello API Python lib:
https://pythonhosted.org/trello/trello.html
* See the full board as JSON:
https://trello.com/b/xcDievul/temas-a-tratar-en-reuniones.json
* Simple GET to see the board and cards JSON:
https://api.trello.com/1/boards/5373c7094676b4be1ba5032b/lists?cards=open&card_fields=name,due,idMembers&fields=name&key=KEY&token=TOKEN

## Usage:

00. Clone the repo :)

0. Install it
  ```
  python setup.py install
  ```
  if you are going to hack it

  ```
  python setup.py develop
  pip install -r dev-requirements.txt
  ```


1. Get app key (You will need it on the next step)
  https://developers.trello.com/get-started

2. Get token:
  ```
   trello2text get-app-token <YOURAPPKEY>
  ```
  copy and paste url to browser, to authorize the app

3. get board id (You'll need it later to pass it on the cli):
  
  add ".json" to the url of the board, like https://trello.com/b/xcDievul/temas-a-tratar-en-reuniones.json

4. Create a ~/.config/trello2text/tello2textrc file with the following content (replaced with your APP_KEY and TOKEN)
  ```
  [main]
  app_key = YOURAPPKEY 
  token =  OBTAINEDTOKEN
  ```

5. execute script, with:
  ```
    Usage:
        trello2text [write <filename>| output] [--template=<template_name>] --board=<board_id> --list=<list_name>
        trello2text -h | --help
        trello2text --version
  ```
  
  
## TO DO:
1. Add some tests
2. Have working version for assembly meetings, write to file for MoinMoin Wiki
3. Future: turn into generic trello serializer with more options, output string templates
