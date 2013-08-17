# Python imports
import json

class Emulator(object):
    """
    The emulator allow you to test complete Glass Application 
    without being part of Explorr Program
    """

    def __init__(self, app):
        self.app = app
        self.cards = []

    def post_card(self, card):
    	"""
    	Insert card
    	"""
    	self.cards.append(card)
