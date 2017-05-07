class CardCollectionUtils(object):

    @staticmethod
    def assert_in_order_from_string(cls, card_collection_strings):
        for x, y in zip(card_collection_strings, card_collection_strings[1:]):
          if not cls.from_string(x) < cls.from_string(y):
            raise AssertionError("{} is not less than {}".format(x, y))
