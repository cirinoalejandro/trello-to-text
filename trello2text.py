#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""trello2text

Usage:
  trello2text [write <filename>| output] [--template=<template_name>] --board=<board_id> --list=<list_name>
  trello2text -h | --help
  trello2text --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --template=<template_name>  Template name [default: moin].
"""

from __future__ import unicode_literals, print_function

import io

from docopt import docopt
from trello import TrelloApi

__version__ = "0.1.0"
__author__ = "Alejandro Cirino"
__license__ = "MIT"

APP_KEY = "FILL API KEY"
TOKEN = "FILL TOKEN"


class TrelloParser(object):
    def __init__(self, app_key, token, board_name):
        if not(all((app_key, token, board_name))):
            raise ValueError("app_key, token and board_name must be provided")
        else:
            self._app_key = app_key
            self._token = token
            self._board_name = board_name

        self.trello_handler = TrelloApi(self._app_key)
        self.trello_handler.set_token(self._token)
        super(TrelloParser, self).__init__()

    def output_moin(self, cards, members):
        output = ""
        for card in cards:
            output += "== " + card.get("name") + " =="
            output += "Asignados: " + ", ".join([members[m] for m in card.get("idMembers")])
            output += card.get("desc")
            comments = self.trello_handler.cards.get_action(card.get("id"), filter="commentCard")
            if comments:
                output += "Comments:"
            for comment in comments:
                output += comment.get("memberCreator").get("fullName") + "(" + comment.get("date") + ") :"
                output += comment.get("data").get("text")
            output += "\n"

        return output

    def parse_cards(self, list_name):
        members = self.trello_handler.boards.get(self._board_name, members="all").get("members")
        members = {m.get("id"): m.get("fullName") for m in members}

        list_id = None

        lists = self.trello_handler.boards.get_list(self._board_name, fields="name")

        for l in lists:
            if l.get("name") == list_name:
                list_id = l.get("id")

        cards = self.trello_handler.lists.get(list_id, cards="open",
                        card_fields="name,desc,shortUrl,idMembers").get("cards")

        text = self.output_moin(cards, members)

        return text


def main():
    """Main entry point for the trello2text CLI."""
    args = docopt(__doc__, version=__version__)
    write = args.get('write')
    output = args.get('output')
    filename = args.get('<filename>')
    board_id = args.get('--board')
    list_name = args.get('--list')

    trello_parser = TrelloParser(APP_KEY, TOKEN, board_id)
    text = trello_parser.parse_cards(list_name)

    if write:
        with io.open(filename, 'w') as fp:
            fp.write(text)
    elif output:
        print(text)

if __name__ == '__main__':
    main()
