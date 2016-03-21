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
title = 'StreamGloud'
image = ''
art = ''
order = 5


class Site():
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        home_url = 'http://qwertty.net'
        search_url = home_url + '/index.php?do=search&subaction=search&full_search=0&search_start=0&result_from=1&story='
        false_positives = ['']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': home_url, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                          'url': home_url, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                          'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'categories':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'navi-wrap'}))
            item_list = []
            if soup:
                for item in soup.findAll('a'):
                    if item: item_list.extend([{'site': site, 'mode': 'list', 'url': home_url + item.get('href'),
                                                'content': '', 'title': item.string.encode('UTF-8'),
                                                'cover_url': a.image(image, image), 'backdrop_url': a.art(),
                                                'type': 3}])
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
                if 'do=search' in params['url']:
                    last_item = re.search('search_start=([0-9]+)', params['url'])
                else:
                    last_item = re.search('/page/([0-9]+)/', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    if 'do=search' in params['url']:
                        page = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + str(item), params['url'])
                        params['url'] = re.sub(r'(result_from=)([0-9]+)', '\g<01>' + str(int(str(item)) * 10 + 1), page)
                    else:
                        params['url'] = re.sub('/page/[0-9]+/', '/page/' + str(item) + '/', params['url'])
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'dle-content'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                for item in soup.findAll('div', {'class': 'short-item'}):
                    if item:
                        _dict = xbmcdict.copy()
                        _dict['url'] = item.a.get('href')
                        _dict['title'] = item.a.img.get('alt').encode('UTF-8')
                        _dict['tvshowtitle'] = _dict['title']
                        _dict['originaltitle'] = _dict['title']
                        item = home_url + item.a.img.get('src').replace('/thumbs', '')
                        _dict['cover_url'] = a.image(item)
                        _dict['thumb_url'] = _dict['cover_url']
                        _dict['poster'] = _dict['cover_url']
                        _dict['sub_site'] = site

                        item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'bottom-nav'}))
            if soup:
                last_item = len(soup.findAll('a', href=True)) - 1
                for index, item in enumerate(soup.findAll('a', href=True)):
                    page = ''
                    if item:
                        if index == 0 and item.string.encode('UTF-8') != 'Back': last_item -= 1
                        if item.string.encode('UTF-8') == 'Back':
                            if item.get('href') == '#':
                                temp = re.search('.*list_submit\(([0-9]+)\).*', item.get('onclick'))
                                if temp:
                                    page = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + temp.group(1), params['url'])
                                    page = re.sub(r'(result_from=)([0-9]+)',
                                                  '\g<01>' + str(int(temp.group(1)) * 10 + 1), page)
                            else:
                                page = item.get('href')
                            if page:
                                item_list.extend(
                                    [{'site': site, 'mode': 'list', 'url': page, 'content': params['content'],
                                      'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                      'backdrop_url': a.art(), 'type': 3}])
                        if item.string.encode('UTF-8') == 'Next':
                            if item.get('href') == '#':
                                temp = re.search('.*list_submit\(([0-9]+)\).*', item.get('onclick'))
                                if temp:
                                    page = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + temp.group(1), params['url'])
                                    page = re.sub(r'(result_from=)([0-9]+)',
                                                  '\g<01>' + str(int(temp.group(1)) * 10 + 1), page)
                            else:
                                page = item.get('href')
                            if page:
                                item_list.extend(
                                    [{'site': site, 'mode': 'list', 'url': page, 'content': params['content'],
                                      'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                      'backdrop_url': a.art(), 'type': 3}])
                        if index == last_item:
                            if item.get('href') == '#':
                                temp = re.search('.*list_submit\(([0-9]+)\).*', item.get('onclick'))
                                if temp:
                                    page = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + temp.group(1), params['url'])
                                    page = re.sub(r'(result_from=)([0-9]+)',
                                                  '\g<01>' + str(int(temp.group(1)) * 10 + 1), page)
                            else:
                                page = item.get('href')
                            if page:
                                item_list.extend([{'site': site, 'mode': 'list', 'url': page, 'content': 'goto',
                                                   'title': a.language(30019, True),
                                                   'cover_url': a.image('goto.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'full-text clearfix desc-text'}))
            item = soup.find('a')
            item_list = []
            xbmcdict = XBMCDict(0).update(params)
            if item:
                _dict = xbmcdict.copy()
                _dict['url'] = item.get('href')
                item_list.extend([_dict])
            else:
                a.alert(a.language(30904, True), sound=False)
            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
