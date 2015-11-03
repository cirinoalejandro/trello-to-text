#!/usr/bin/python
# -*- coding: utf-8 -*-

# usage so far:
# PYTHONIOENCODING=UTF-8 python -W ignore script.py > out.moin

#TODO: take as parameters: APP_KEY, TOKEN, BOARD, list_name

from trello import TrelloApi

APP_KEY = ""
TOKEN = ""
BOARD = "5373c7094676b4be1ba5032b"
list_name = "Deferred"

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
    print "== " + card.get("name") + " =="
    print "Asignados: " + ", ".join([members[m] for m in card.get("idMembers")])
    print "\n"
    print card.get("desc")
    comments = trello.cards.get_action(card.get("id"), filter="commentCard")
    if comments:
        print "\n"
        print "Comments:"
    for comment in comments:
        print "\n"
        print comment.get("memberCreator").get("fullName") + "(" + comment.get("date") + ") :"
        print comment.get("data").get("text")
    print "\n"
