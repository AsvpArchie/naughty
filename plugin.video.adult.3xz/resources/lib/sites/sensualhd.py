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
title = 'PornHardX'
image = ''
art = ''
order = 1


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        home_url = 'http://pornhardx.com/'
        movies_url = home_url + 'category/full-movie/'
        scenes_url = home_url + 'video/'
        search_url = home_url + '?s='
        false_positives = ['http://pornhardx.com/video', 'http://pornhardx.com/video/?order=viewed',
                           'http://pornhardx.com/video/?order=liked', 'http://pornhardx.com/']

        if mode == 'main':
            item_list = []
            item_list.extend([{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                               'url': scenes_url, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(),
                               'type': 3}])
            item_list.extend([{'site': site, 'mode': 'list', 'title': a.language(30003), 'content': '',
                               'url': home_url, 'cover_url': a.image('recent.png', image), 'backdrop_url': a.art(),
                               'type': 3}])
            item_list.extend([{'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                               'url': scenes_url, 'cover_url': a.image('categories.png', image),
                               'backdrop_url': a.art(), 'type': 3}])
            item_list.extend([{'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                               'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                               'type': 3}])
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'categories':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'navigation-wrapper'}))
            item_list = []
            if soup:
                for item in soup.findAll('a', {'href': True}):
                    if item:
                        if item.get('href') not in false_positives:
                            if 'full-movie' in params['url']:
                                if movies_url != item.get('href') and 'full-movie' in item.get('href'):
                                    item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href'),
                                                       'content': '',
                                                       'title': item.contents[0].encode('UTF-8'),
                                                       'cover_url': a.image(image, image), 'backdrop_url': a.art(),
                                                       'type': 3}])
                            elif 'full-movie' not in item.get('href'):
                                item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href'),
                                                   'content': '',
                                                   'title': item.contents[0].encode('UTF-8'),
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
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {
                'class': re.compile('col-sm-8(?:\s*main-content)*')}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                for item in soup.findAll('div',
                                         {'class': re.compile('.*(?:col-xs-6 item|post type-post status-publish).*')}):
                    if item:
                        if item.a.get('href') not in false_positives:
                            _dict = xbmcdict.copy()
                            if 'full-movie' not in params['url']:
                                _dict['duration'] = '1500'
                                _dict['content'] = 'episodes'
                            if item.h3:
                                _dict['url'] = item.h3.a.get('href')
                                if item.h3.a.contents:
                                    _dict['title'] = item.h3.a.contents[0].encode('UTF-8')
                                else:
                                    _dict['title'] = 'Untitled'
                            elif item.h2:
                                _dict['url'] = item.h2.a.get('href')
                                if item.h2.a.contents:
                                    _dict['title'] = item.h2.a.contents[0].encode('UTF-8')
                                else:
                                    _dict['title'] = 'Untitled'
                            _dict['tvshowtitle'] = _dict['title']
                            _dict['originaltitle'] = _dict['title']
                            _dict['cover_url'] = a.image(item.img.get('src'))
                            _dict['thumb_url'] = _dict['cover_url']
                            _dict['poster'] = _dict['cover_url']
                            _dict['sub_site'] = site

                            item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'class': 'pagination'}))
            if soup.li:
                item = soup.find('a', {'class': 'prev page-numbers'})
                if item:
                    item_list.extend(
                        [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                          'title': a.language(30017, True), 'cover_url': a.image(image, image),
                          'backdrop_url': a.art(), 'type': 3}])
                item = soup.find('a', {'class': 'next page-numbers'})
                if item:
                    item_list.extend(
                        [{'site': site, 'mode': 'list', 'url': item.get('href'), 'content': params['content'],
                          'title': a.language(30018, True), 'cover_url': a.image(image, image),
                          'backdrop_url': a.art(), 'type': 3}])
                    if len(soup.findAll('a')) > 2:
                        last_item = soup.find('a', {'class': 'next page-numbers'}).parent.previousSibling.a.get('href')
                        item_list.extend([{'site': site, 'mode': 'list', 'url': last_item, 'content': 'goto',
                                           'title': a.language(30019, True), 'cover_url': a.image(image, image),
                                           'backdrop_url': a.art(), 'type': 3}])
                else:
                    item = soup.find('span', {'class': 'page-numbers current'})
                    if item:
                        if len(soup.findAll('a')) > 2:
                            last_item = soup.find('span',
                                                  {'class': 'page-numbers current'}).parent.previousSibling.a.get(
                                'href')
                            item_list.extend([{'site': site, 'mode': 'list', 'url': last_item, 'content': 'goto',
                                               'title': a.language(30019, True),
                                               'cover_url': a.image('goto.png', image),
                                               'backdrop_url': a.art(), 'type': 3}])
            else:
                soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'class': 'pager'}))
                item = soup.find('li', {'class': 'previous'})
                if item:
                    item_list.extend([{'site': site, 'mode': 'list', 'url': item.previousSibling.get('href'),
                                       'content': params['content'],
                                       'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])
                item = soup.find('li', {'class': 'next'})
                if item:
                    item_list.extend([{'site': site, 'mode': 'list', 'url': item.previousSibling.get('href'),
                                       'content': params['content'],
                                       'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                       'backdrop_url': a.art(), 'type': 3}])
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('body'))
            item = ''
            item_list = []
            first = True
            if soup:
                ul = soup.find('ul', {'class': 'pagination post-tape'})
                if ul:
                    lis = ul.findAll('li')
                else:
                    lis = ['none']
                for li in lis:
                    if first:
                        first = False
                    else:
                        try:
                            soup = None
                            li_url = li.a.get('href')
                            html = a.get_page(li_url)
                            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('body'))
                            item = ''
                        except:
                            pass
                    if soup:
                        for item in soup.findAll('param', {'name': 'FlashVars'}):
                            item = item.get('value')
                            item = re.search('.*?proxy\.link=(.+?)&(?:proxy|skin).*?', item)
                            if item:
                                if item not in item_list:
                                    item = item.group(1)
                                else:
                                    item = ''
                            else:
                                item = ''
                            xbmcdict = XBMCDict(0).update(params)
                            if item:
                                _dict = xbmcdict.copy()
                                _dict['url'] = item
                                item_list.extend([_dict])
                        item = ''
                        for item in soup.findAll('video'):
                            for source in soup.findAll('source'):
                                src = source.get('src')
                                if src:
                                    xbmcdict = XBMCDict(0).update(params)
                                    if item and ('..' not in src):
                                        _dict = xbmcdict.copy()
                                        try:
                                            _dict['src_title'] = source.get('data-res') + 'p'
                                        except:
                                            pass
                                        _dict['url'] = src
                                        item_list.extend([_dict])
                            try:
                                src = item.get('src')
                                if src:
                                    xbmcdict = XBMCDict(0).update(params)
                                    if item and ('..' not in src):
                                        _dict = xbmcdict.copy()
                                        try:
                                            _dict['src_title'] = source.get('data-res') + 'p'
                                        except:
                                            pass
                                        _dict['url'] = src
                                        item_list.extend([_dict])
                            except:
                                pass
                        for script in soup.findAll('script'):
                            item = ''
                            if script.get('src'):
                                if 'http://videomega.tv/validatehash.php' in script['src']:
                                    item = script['src']
                                elif 'ref=' in script.get('src'):
                                    temp = re.search('.*ref=[\'"](.+?)[\'"]', script.get('src'))
                                    if temp: item = 'http://videomega.tv/iframe.php?ref=' + temp.group(1)
                                xbmcdict = XBMCDict(0).update(params)
                                if item:
                                    _dict = xbmcdict.copy()
                                    _dict['url'] = item
                                    item_list.extend([_dict])
                        for iframe in soup.findAll('iframe'):
                            item = ''
                            if iframe.get('src'):
                                if 'http://videomega.tv/validatehash.php' in iframe['src']:
                                    item = iframe['src']
                                elif 'ref=' in iframe.get('src'):
                                    temp = re.search('.*ref=[\'"](.+?)[\'"]', iframe.get('src'))
                                    if temp: item = 'http://videomega.tv/iframe.php?ref=' + temp.group(1)
                                else:
                                    item = iframe.get('src')
                                xbmcdict = XBMCDict(0).update(params)
                                if item:
                                    _dict = xbmcdict.copy()
                                    _dict['url'] = item
                                    item_list.extend([_dict])

            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
