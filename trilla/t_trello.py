# -*- coding: utf-8 -*-

from trello import TrelloClient, Board, Card
from trello.util import create_oauth_token

def config(config):
    print "########## Configuring Trello API ##########"
    key = raw_input("API KEY:")
    secret = raw_input("API SECRET:")
    create_oauth_token(name="trilla", expiration="never", key=key, secret=secret)


class Trello(object):
    def __init__(self, config):
        self.client = TrelloClient(config.trello.api_key,
                                   config.trello.api_secret,
                                   config.trello.oauth_token,
                                   config.trello.oauth_token_secret)

        self.default_board = config.target_board
        self.default_list = config.target_list

    def get_board(self, board_name=None):
        board_name = board_name or self.default_board
        for board in self.client.list_boards():
            if board.name == board_name:
                return board
        return None

    def get_list(self, board_name, list_name):
        board = self.get_board(board_name)
        if not board:
            return None

        list_name = list_name or self.default_list
        for tlist in board.all_lists():
            if tlist.name == list_name:
                return tlist
        return None

    def create_card(self,title, description, labels=[], board_name=None, list_name=None):
        tlist = self.get_list(board_name, list_name)
        if not tlist:
            return None

        return tlist.add_card(title, description)

    def get_cards(self, board_name=None, list_name=None):
        tlist = self.get_list(board_name, list_name)
        if not tlist:
            return []
        return tlist.list_cards()

