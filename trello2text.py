#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""trello2text

Usage:
  trello2text ship new <name>...
  trello2text ship <name> move <x> <y> [--speed=<kn>]
  trello2text ship shoot <x> <y>
  trello2text mine (set|remove) <x> <y> [--moored|--drifting]
  trello2text -h | --help
  trello2text --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

from __future__ import unicode_literals, print_function

from docopt import docopt
from trello import TrelloApi

__version__ = "0.1.0"
__author__ = "Alejandro Cirino"
__license__ = "MIT"

APP_KEY = ""
TOKEN = ""
BOARD = "5373c7094676b4be1ba5032b"

def parse_cards(list_name):
    trello = TrelloApi(APP_KEY)
    trello.set_token(TOKEN)

    members = trello.boards.get(BOARD, members="all").get("members")
    members = {m.get("id"): m.get("fullName") for m in members}

    list_id = None

    lists = trello.boards.get_list(BOARD, fields="name")

    for l in lists:
        if l.get("name") == list_name:
            list_id = l.get("id")

    cards = trello.lists.get(list_id, cards="open", card_fields="name,desc,shortUrl,idMembers").get("cards")

    for card in cards:
        print ("== " + card.get("name") + " ==")
        print ("Asignados: " + ", ".join([members[m] for m in card.get("idMembers")]))
        print (card.get("desc"))
        comments = trello.cards.get_action(card.get("id"), filter="commentCard")
        if comments:
            print ("Comments:")
        for comment in comments:
            print (comment.get("memberCreator").get("fullName") + "(" + comment.get("date") + ") :")
            print (comment.get("data").get("text"))
        print ("\n")


def main():
    """Main entry point for the trello2text CLI."""
    args = docopt(__doc__, version=__version__)
    print(args)
    parse_cards("Deferred")


if __name__ == '__main__':
    main()
