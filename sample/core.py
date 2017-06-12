import util

from div_costant import CHAMPION, TOP_HEROES_CATEGORY

def generic_stats(user):
    tree = util.base_tree(user);
    rank = tree.xpath('//div[@class="competitive-rank"]/div')[0].text
    level = tree.xpath('//div[@class="player-level"]/div')[0].text
    return {
        "rank" : rank,
        "level" : level
    }

def featured_stat(user, _par=None):
    print(_par)
    if _par is None:
        mode = "quickplay"
    else:
        mode = _par
    print(mode)
    tree = util.base_tree(user);
    values = tree.xpath('//div[@id="{}"]//h3[@class="card-heading"]/text()'.format(mode))
    keys = tree.xpath('//div[@id="{}"]//p[@class="card-copy"]/text()'.format(mode))
    return dict(zip(keys, values))

def top_heroes(user, _cat=None, _mode=None):
    if _cat is None:
        category = TOP_HEROES_CATEGORY["time_played"]
    else:
        category = TOP_HEROES_CATEGORY[_cat]
    if _mode is None:
        mode = "quickplay"
    else:
        mode = _mode
    tree = util.base_tree(user);
    keys = tree.xpath('//div[@id="{}"]//div[@data-category-id="{}"]/div/div/div/div[@class="title"]/text()'.format(mode,category))
    values = tree.xpath('//div[@id="{}"]//div[@data-category-id="{}"]/div/div/div/div[@class="description"]/text()'.format(mode,category))
    return dict(zip(keys, values))

def carreer_stats(user, champ = CHAMPION["all"], mode="quickplay"):
    tree = util.base_tree(user);
    keys = tree.xpath('//div[@id="{}"]//div[@data-category-id="{}"]//tbody/tr/td[1]/text()'.format(mode,champ))
    values = tree.xpath('//div[@id="{}"]//div[@data-category-id="{}"]//tbody/tr/td[2]/text()'.format(mode,champ))
    return dict(zip(keys, values))

if __name__ == '__main__':
    exit()
# print(generic_stats())
# print(featured_stat('Aren-2596'))
# print(top_heroes(top_heroes_category["time_played"]))
# print(carreer_stats(champion["reaper"]))