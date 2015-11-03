#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""trello2text

Usage:
  trello2text [write <filename>| output] [--template=<template_name>] --board=<board_id> --list=<list_name>
  trello2text get-app-token <app_key>
  trello2text -h | --help
  trello2text --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --template=<template_name>  Template name [default: moin].
"""

from __future__ import unicode_literals, print_function

import io
import os
import sys
from ConfigParser import SafeConfigParser

from docopt import docopt
from trello import TrelloApi


__version__ = "0.1.0"
__author__ = "Alejandro Cirino"
__license__ = "MIT"


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


def get_trello_app_token(app_key):
    trello = TrelloApi(app_key)
    print (trello.get_token_url('Trello2Text', expires='never', write_access=True))
    print ("Now got to the url above and authorize the app")


def get_config():
    user_home = os.path.expanduser("~")
    config_file_path = os.path.join(user_home, '.config', 'trello2text', 'trello2textrc')

    config = SafeConfigParser()
    config.read(config_file_path)

    return config


def main():
    """Main entry point for the trello2text CLI."""
    try:
        config = get_config()
        app_key = config.get("main", "app_key")
        token = config.get("main", "token")
    except Exception as err:
        sys.exit("Error on config file: {}".format(err))

    args = docopt(__doc__, version=__version__)
    write = args.get('write')
    get_app_token = args.get('get-app-token')
    output = args.get('output')
    filename = args.get('<filename>')
    board_id = args.get('--board')
    list_name = args.get('--list')

    if not get_app_token:
        trello_parser = TrelloParser(app_key, token, board_id)
        text = trello_parser.parse_cards(list_name)

    if write:
        with io.open(filename, 'w') as fp:
            fp.write(text)
    elif output:
        print(text)
    elif get_app_token:
        get_trello_app_token(app_key)

if __name__ == '__main__':
    main()
