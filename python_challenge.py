import sys

flushes = []

def encode_card(text):
    """
      Function encodes a card (eg.: "4D") into a number such that its
      binary representation follows the schema:

      +--------+--------+--------+--------+
      |xxxbbbbb|bbbbbbbb|cdhsrrrr|xxpppppp|
      +--------+--------+--------+--------+

      b = bit turned depending on rank of card
      cdhs = suit of card (bit turned on based on suit of card)
      r = rank of card (two=0, three=1, ..., ace=12)
      p = prime number of rank (two=2, three=3, four=5, ..., ace=41)

    """

    prime_number_dict = {"2":2, "3":3, "4":5, "5":7, "6":11, "7":13, "8":17,
                         "9":19, "T":23, "J":29, "Q":31, "K":37, "A":41}
    card_number_dict = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6,
                        "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}
    card_suit_dict = {"C":8, "D":4, "H":2, "S":1}
    card_bit_dict = {"2":1, "3":2, "4":4, "5":8, "6":16, "7":32, "8":64,
                     "9":128, "T":256, "J":512, "Q":1024, "K":2048, "A":4096}
    card_number = "2"
    card_suit = "C"

    try:
        card_prime_number = prime_number_dict[text[0]]
        card_number = card_number_dict[text[0]]
        card_suit = card_suit_dict[text[1]]
        card_bit = card_bit_dict[text[0]]
    except:
        print("Oops!",sys.exc_info()[0],"occured.")

    return (card_bit<<16)+(card_suit<<12)+(card_number<<8)+card_prime_number
