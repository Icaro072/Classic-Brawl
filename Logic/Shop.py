class Shop:
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems

    """



    offers = [

        {
            'ID': 4,
            'OfferTitle': 'Special Offer',
            'Cost': 2,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 52,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 69420
        },
        
        {
            'ID': 10,
            'OfferTitle': 'Power Points',
            'Cost': 20,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 1,
            'Timer': 69420
        },
        
        {
            'ID': 8,
            'OfferTitle': 'Coins',
            'Cost': 10,
            'Multiplier': 5,
            'BrawlerID': 0,
            'SkinID': 0,
            'ShopType': 1,
            'ShopDisplay': 1,
            'Timer': 69420
        },
        
        {
            'ID': 6,
            'OfferTitle': 'SPECIAL OFFER',
            'Cost': 20,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 99999
        },

        {
            'ID': 10,
            'OfferTitle': 'SPECIAL OFFER',
            'Cost': 1500,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 0,
            'ShopType': 3,
            'ShopDisplay': 0,
            'Timer': 99999
        },


    ]


    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        },

        {
            'Cost': 280,
            'Amount': 2600
        },

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 3
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 10
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }


    def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            self.writeVint(1)

            self.writeVint(item['ID']) # ItemID
            self.writeVint(item['Multiplier']) # Ammount
            self.writeScId(16, item['BrawlerID'])
            self.writeVint(item['SkinID'])
            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer

            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)
            
            self.writeInt(0)
            self.write_string_reference(item['OfferTitle'])
            self.writeBoolean(False)
            self.writeString()
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(2)
            self.writeVint(0) # % Extra Text
            