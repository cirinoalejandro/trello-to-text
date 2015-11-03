from trello import TrelloApi

APP_KEY = "YOUR APP_KEY"

trello = TrelloApi(APP_KEY)
print trello.get_token_url('Trello2Text', expires='never', write_access=True)
