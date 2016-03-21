# -*- coding: UTF-8 -*-
"""
    Copyright (C) 2014  smokdpi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

""" Site information used for main menu if more than 1 site """
title = 'PlayPorn'
image = ''
art = ''
order = 6


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        home_url = 'http://playporn.to/'
        search_url = home_url + '?submit=Search&s='
        movies_url = home_url + 'category/xxx-movie-stream/'
        scenes_url = home_url + 'category/xxx-clips-scenes-stream/'
        false_positives = ['http://playporn.to/deutsche-milfs-anonym-sex/']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30003), 'content': '',
                          'url': home_url, 'cover_url': a.image('recent.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'sub', 'title': a.language(30001), 'content': '',
                          'url': movies_url, 'cover_url': a.image('movies.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'sub', 'title': a.language(30002), 'content': '',
                          'url': scenes_url, 'cover_url': a.image('scenes.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                          'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'sub':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': params['url'], 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'category', 'title': a.language(30005), 'content': '',
                          'url': home_url, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'category':
            index = 1
            if 'scenes' in params['url'].lower(): index = 2
            html = a.get_page(home_url)
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', 'nav fl'))
            item_list = []
            for item in soup.findAll('ul')[index].findAll({'a': True}):
                item_list.extend(
                    [{'site': 'playporn', 'mode': 'list', 'url': item.get('href'), 'content': '',
                      'title': item.contents[0].encode('UTF-8'), 'cover_url': a.image(image, image),
                      'backdrop_url': a.art(), 'type': 3}])
            if item_list:
                a.add_items(item_list)
                a.end_of_directory()

        elif mode == 'list':
            if params.get('content', '') == 'search':
                item = a.search_input()
                if item:
                    params['url'] = search_url + item
                else:
                    exit(1)
            elif params.get('content', '') == 'goto':
                last_item = re.search('/page/([0-9]+)/', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    params['url'] = re.sub('/page/[0-9]+/', '/page/' + str(item) + '/', params['url'])
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('body'))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            xbmcdict = XBMCDict(0).update(params)
            for item in soup.findAll('div', 'photo-thumb-image'):
                if not item.a.get('href') in false_positives:
                    _dict = xbmcdict.copy()
                    if 'scenes' in params['url']:
                        _dict['duration'] = '2700'
                        _dict['content'] = 'episodes'
                    _dict['url'] = item.a.get('href')
                    _dict['title'] = item.a.get('title').encode('UTF-8')
                    _dict['tvshowtitle'] = _dict['title']
                    _dict['originaltitle'] = _dict['title']
                    _dict['cover_url'] = a.image(item.img.get('src'))
                    _dict['thumb_url'] = _dict['cover_url']
                    _dict['poster'] = _dict['cover_url']
                    _dict['sub_site'] = site

                    item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', 'more_entries'))
            if soup:
                item = soup.find('a', 'previouspostslink')
                if item: item_list.extend(
                    [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                      'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                      'backdrop_url': a.art(), 'type': 3}])
                item = soup.find('a', 'nextpostslink')
                if item: item_list.extend(
                    [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                      'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                      'backdrop_url': a.art(), 'type': 3}])
                item = soup.find('a', 'last')
                if item: item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': 'goto',
                                            'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                            'backdrop_url': a.art(), 'type': 3}])
            if item_list:
                a.add_items(item_list)
                a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'loopedSlider'}))
            soup = soup.find(text=lambda text: isinstance(text, Comment))
            if soup:
                soup = re.sub('&lt;', '<', soup.encode('utf-8'))
                soup = re.sub('&gt;', '>', soup)
                soup = BeautifulSoup(soup, parseOnlyThese=SoupStrainer('div', 'video'))
                if soup:
                    item_list = []
                    xbmcdict = XBMCDict(0).update(params)
                    for item in soup.findAll('iframe'):
                        _dict = xbmcdict.copy()
                        _dict['url'] = item.get('src').replace('http://playporn.to/stream/all/?file=', '').encode(
                            'UTF-8')
                        if 'flashx.tv' in _dict['url'].lower():
                            item = re.search('hash=(.+?)&', _dict['url'])
                            if item: _dict['url'] = 'http://flashx.tv/video/' + item.group(1) + '/'
                        elif 'played.to' in _dict['url'].lower():
                            item = re.search('embed-([a-zA-Z0-9]+?)-.+?html', _dict['url'])
                            if item: _dict['url'] = 'http://played.to/' + item.group(1)
                        item_list.extend([_dict])
                    if item_list:
                        from playback import Playback
                        Playback().choose_sources(item_list)
                    else:
                        a.alert(a.language(30904, True), sound=False)
                else:
                    a.alert(a.language(30904, True), sound=False)
            else:
                a.alert(a.language(30904, True), sound=False)
