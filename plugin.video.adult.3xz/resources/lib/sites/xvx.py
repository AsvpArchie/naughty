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
title = 'XVX'
image = ''
art = ''
order = 7


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        base_url = 'http://yespornplease.com'
        home_url = base_url + '/index.php'
        popular_url = base_url + '/index.php?p=1&m=today'
        search_url = base_url + '/search.php?q='
        false_positives = ['']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': home_url, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30016), 'content': '',
                          'url': popular_url, 'cover_url': a.image('popular.png', image), 'backdrop_url': a.art(),
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
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'categories'}))
            item_list = []
            if soup:
                for item in soup.findAll('a'):
                    if item: item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href').replace(' ', '+'),
                                                'content': '', 'title': item.string.encode('UTF-8'),
                                                'cover_url': a.image(image, image), 'backdrop_url': a.art(),
                                                'type': 3}])
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'list':
            if params.get('content', '') == 'search':
                item = a.search_input()
                if item:
                    params['url'] = search_url + item.replace(' ', '+')
                else:
                    exit(1)
            elif params.get('content', '') == 'goto':
                last_item = re.search('p=([0-9]+)', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    params['url'] = re.sub('p=[0-9]+', 'p=' + str(item), params['url']).replace(' ', '+')
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'videos'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                for item in soup.findAll('div', {'class': 'video-preview'}):
                    if item:
                        _dict = xbmcdict.copy()
                        temp = item.find('div', {'class': 'jcarousel'}).a
                        if temp:
                            temp = temp.get('href')
                            if not temp.startswith('http://'): temp = base_url + temp
                            _dict['url'] = temp
                            _dict['title'] = item.find('div', {'class': 'preview-title'}).get('title').encode('UTF-8')
                            _dict['tvshowtitle'] = _dict['title']
                            _dict['originaltitle'] = _dict['title']
                            temp = item.find('div', {'class': 'jcarousel'}).img.get('src')
                            if temp.startswith('//'): temp = 'http:' + temp
                            _dict['cover_url'] = a.image(temp)
                            _dict['thumb_url'] = _dict['cover_url']
                            _dict['poster'] = _dict['cover_url']
                            temp = item.find('div', {'class': 'preview-info-box length'}).b.string
                            if temp:
                                temp = re.search('([0-9]+):([0-9]+):([0-9]+)', temp)
                                _dict['duration'] = str(
                                    (int(temp.group(1)) * 60 * 60) + (int(temp.group(2)) * 60) + int(temp.group(3)))
                            _dict['sub_site'] = site

                            item_list.extend([_dict])

                soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('body'))
                if soup.find('a', {'id': 'prev-page'}):
                    item = soup.find('a', {'id': 'prev-page'}).get('href').replace(' ', '+')
                    if not item.startswith('http://'): item = base_url + item
                    if 'index.php' in params['url']: item = item.replace('search.php', 'index.php')
                    item_list.extend([{'site': site, 'mode': 'list', 'url': item, 'content': params['content'],
                                       'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])
                if soup.find('a', {'id': 'next-page'}):
                    item = soup.find('a', {'id': 'next-page'}).get('href').replace(' ', '+')
                    if 'index.php' in params['url']: item = item.replace('search.php', 'index.php')
                    if not item.startswith('http://'): item = base_url + item
                    item_list.extend([{'site': site, 'mode': 'list', 'url': item, 'content': params['content'],
                                       'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])

                soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'pagination'}))
                last_item = False
                if soup:
                    for item in reversed(soup.findAll('a')):
                        last_item = item.get('href')
                        if not last_item.startswith('http://'): last_item = base_url + last_item
                        break
                if last_item:
                    item_list.extend([{'site': site, 'mode': 'list', 'url': last_item, 'content': 'goto',
                                       'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])

            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('object', {'id': 'videoContainer'}))
            item_list = []
            if soup:
                item = soup.find('param', {'name': 'flashvars'})
                item = re.search('.*?video_url=(.+?)&.*?', str(item))
                if item: item = item.group(1)
                xbmcdict = XBMCDict(0).update(params)
                if item:
                    _dict = xbmcdict.copy()
                    _dict['url'] = item
                    item_list.extend([_dict])
                else:
                    a.alert(a.language(30904, True), sound=False)
            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
