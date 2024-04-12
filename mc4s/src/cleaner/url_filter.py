from tld import get_tld
# TLD で除去
# (機械翻訳の可能性が高い)
blacklist = ["cn", "ru", "tv", "hu", "pl", "info"]

# まとめ系サイト
matome_list = ["2ch.", "5ch.", "matome", "jin115", "115jin", "doorblog.jp", "umasoku.com", "fc2.com", "sokuhou", "huyosoku.com", "kumusoku", "kabu-sokuhou.com", "soku"]

# 詐欺的サイト
scam_list = ["paolabaertl.com", "ojiyama.com", "anpiacenza.org", "rojobermelo.com", "giscountry.com"
,"occupyapec.com"
,"testedevelocidadegvt.com"
,"buy-anabolic-steroid.biz"
,"recette-tunisienne.com"
]

ng_list=["wikipedia.org", "5ch.","tousatsu1032","kaola.jp","/juniaaidolkageki.blog","dougamax.com","ovovz","av-matome.","www.shinjuku-heart.com","www.rezubian-douga.com","http://lady5.jp"]



def u_filter(url: str):
    count=0
    try:
        tld_name = get_tld(url)
        if tld_name in blacklist:
            return True

    except Exception as exc:
        count+=0

    for m in matome_list:
        if m in url:
            return True

    for s in scam_list:
        if s in url:
            return True
        
    for s in ng_list:
        if s in url:
            return True

    # ok.
    return False

"""
ng_list=["wikipedia.org", "5ch.","tousatsu1032","kaola.jp","/juniaaidolkageki.blog","dougamax.com","ovovz","av-matome.","www.shinjuku-heart.com","www.rezubian-douga.com"]
def u_filter(url, strings=ng_list):
    return any(s in url for s in strings)
#ut1_black_listも追加するのが良い
"""