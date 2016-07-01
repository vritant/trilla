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
        self.board = self._get_board("Testing Trilla")

    def _get_board(self, board_name):
        for board in self.client.list_boards():
            if board.name == board_name:
                return board
        return None

    def _get_list(self, list_name):
        for tlist in self.board.all_lists():
            if tlist.name == list_name:
                return tlist
        return None
    
    def create_card(self, list_name, title, description, labels=[]):
        t_list = self._get_list(list_name)
        if not t_list:
            return
        t_list.add_card(title, description)
    
    def get_cards(self, list_name):
        tlist = self._get_list(list_name)
        if not tlist:
            return []
        return tlist.list_cards()


