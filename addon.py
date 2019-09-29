from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.acast.com/ruleofthree"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://thumborcdn.acast.com/Ib7EKInHheWyrlcARzjgYjsZfVs=/500x500/https%3A%2F%2Fmediacdn.acast.com%2Fassets%2Fa18c2026-fb61-4cb6-a153-32d529de0a07%2F-jfcdlvsg-ruleofthree_rev_logo2.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://thumborcdn.acast.com/Ib7EKInHheWyrlcARzjgYjsZfVs=/500x500/https%3A%2F%2Fmediacdn.acast.com%2Fassets%2Fa18c2026-fb61-4cb6-a153-32d529de0a07%2F-jfcdlvsg-ruleofthree_rev_logo2.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
