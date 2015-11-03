# trello2text


[![Fury](https://badge.fury.io/py/trello2text.png)](http://badge.fury.io/py/trello2text
)]


[![travis.ci](https://travis-ci.org/cirinoalejando/trello2text.png?branch=master)](https://travis-ci.org/cirinoalejando/trello2text)]


[![pypy](https://pypip.in/d/trello2text/badge.png)](https://crate.io/packages/trello2text?version=latest
)]


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

00. clone the repo :)

0. install requirements
  ```
  cd trello-to-text
  pip install -r requirements.txt
  ```

1. get app key
  https://developers.trello.com/get-started

2. get token:
  ```
  python
  from trello import TrelloApi
  trello = TrelloApi(APP_KEY)
  trello.get_token_url('NombreApp', expires='never', write_access=True)
  ```
  copy and paste url to browser, authorize app

3. get board id:
  
  add ".json" to the url of the board, like https://trello.com/b/xcDievul/temas-a-tratar-en-reuniones.json

4. replace APP_KEY, TOKEN, BOARD, list_name in the file script.py

5. execute script, with:
  ```
  PYTHONIOENCODING=UTF-8 python -W ignore script.py > out.moin
  ```
  
  
## TO DO:
1. Make into python package
2. Accept command line parameters
3. Set utf-8 as default output encoding
4. Modularize, add tests
5. Have working version for assembly meetings, write to file for MoinMoin Wiki
6. Future: turn into generic trello serializer with more options, output string templates
