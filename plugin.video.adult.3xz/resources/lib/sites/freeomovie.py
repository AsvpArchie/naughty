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
title = 'freeomovie'
image = ''
art = ''
order = 4


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        home_url = 'http://www.freeomovie.com/'
        movies_url = home_url + 'category/full-movie/'
        scenes_url = home_url + 'category/clips/'
        search_url = home_url + '/?s='
        false_positives = ['http://www.freeomovie.com/category/full-movie/',
                           'http://www.freeomovie.com/category/clips/']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': home_url, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30001), 'content': '',
                          'url': movies_url, 'cover_url': a.image('movies.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30002), 'content': '',
                          'url': scenes_url, 'cover_url': a.image('scenes.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                          'url': home_url, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                          'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'categories':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'multi-column-taxonomy-list'}))
            item_list = []
            if soup:
                for item in soup.findAll('a'):
                    if item:
                        if item.get('href') not in false_positives:
                            item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href'),
                                               'content': '', 'title': item.string.encode('UTF-8'),
                                               'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])

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
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'content'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                for item in soup.findAll('div', {'class': 'postbox'}):
                    if item:
                        if item.h2.a.get('href') not in false_positives:
                            _dict = xbmcdict.copy()
                            if scenes_url in params['url']:
                                _dict['duration'] = '1500'
                                _dict['content'] = 'episodes'
                            _dict['url'] = item.h2.a.get('href')
                            _dict['title'] = item.h2.a.get('title').encode('UTF-8')
                            _dict['tvshowtitle'] = _dict['title']
                            _dict['originaltitle'] = _dict['title']
                            _dict['cover_url'] = a.image(item.img.get('src'))
                            _dict['thumb_url'] = _dict['cover_url']
                            _dict['poster'] = _dict['cover_url']
                            _dict['sub_site'] = site
                            item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'wp-pagenavi'}))
            last_item = False
            if soup:
                for item in soup.findAll('a', href=True):
                    if item:
                        if item.get('class') == 'previouspostslink':
                            item_list.extend(
                                [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                                  'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                  'backdrop_url': a.art(), 'type': 3}])
                        if item.get('class') == 'nextpostslink':
                            item_list.extend(
                                [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                                  'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                  'backdrop_url': a.art(), 'type': 3}])
                        if item.get('class') == 'last':
                            last_item = item.get('href')
                if not last_item:
                    try:
                        if not soup.find('a', {'class': 'nextpostslink'}):
                            last_item = soup.findAll('a', href=True)[-1].get('href')
                        else:
                            last_item = soup.findAll('a', href=True)[-2].get('href')
                    except:
                        pass
                if last_item:
                    item_list.extend([{'site': site, 'mode': 'list', 'url': last_item, 'content': 'goto',
                                       'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])

            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            item_list = []
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'videosection'}))
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                pages = soup.findAll('li', {'class': re.compile('pg.')})
                if pages:
                    old_li = pages[0].get('class')
                    _dict = xbmcdict.copy()
                    _dict['multi-part'] = True
                    parts = []
                    for li in pages:
                        if old_li != li.get('class'):
                            _dict['parts'] = parts
                            item_list.extend([_dict])
                            _dict = xbmcdict.copy()
                            _dict['multi-part'] = True
                            old_li = li.get('class')
                            parts = []
                        url = re.search('.+myurl=(.+)', li.a.get('href'), re.IGNORECASE)
                        if url:
                            url = url.group(1)
                            parts.extend([url])
                    if parts:
                        _dict['parts'] = parts
                        item_list.extend([_dict])
                alink = soup.find('a', {'target': '_blank'})
                if alink:
                    alink = alink.get('href')
                    if 'main.exoclick.com' not in alink:
                        _dict = xbmcdict.copy()
                        _dict['url'] = alink
                        item_list.extend([_dict])
                iframes = soup.findAll('iframe', {'src': True})
                if iframes:
                    for iframe in iframes:
                        iframe = iframe.get('src')
                        if 'main.exoclick.com' not in iframe:
                            _dict = xbmcdict.copy()
                            _dict['url'] = iframe
                            item_list.extend([_dict])
                if not item_list:
                    soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'id': 'countrytabs'}))
                    if soup:
                        xbmcdict = XBMCDict(0).update(params)
                        for index, items in enumerate(soup.findAll('a', href=True)):
                            item = ''
                            if not items.get('id') == 'jpg':
                                item = items.get('href')
                                item = re.search('.*myURL\[\]=(.+)$', item, re.DOTALL)
                                if item:
                                    item = re.sub('&tab=[0-9]+', '', item.group(1))
                                if item:
                                    _dict = xbmcdict.copy()
                                    _dict['url'] = item
                                    _dict['count'] = index
                                    item_list.extend([_dict])
            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
