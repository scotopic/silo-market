from chia.wallet.trading.offer import Offer

offer_file_contents='offer1...'

offr=Offer.from_bech32(offer_file_contents)
print('----------- OFFER FILE -----------')
print(o)
print('----------- OFFER IDENTIFIER / NAME ----------------')
print(o.name())