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
title = 'Xtheatre'
image = ''
art = ''
order = 3


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        home_url = 'http://xtheatre.net/'
        search_url = home_url + '?s='
        false_positives = ['http://watchxxxhd.net/watch-full-movies-hd/', 'http://watchxxxhd.net',
                           'http://watchxxxhd.net/category/movies/', 'http://watchxxxhd.net/category/ategorized222/',
                           'http://watchxxxhd.net/watch-full-movies-hd/']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': home_url + '?filtre=date&cat=0', 'cover_url': a.image('all.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                          'url': home_url + 'categories/', 'cover_url': a.image('categories.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                          'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'categories':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'class': 'listing-cat'}))
            item_list = []
            if soup:
                for item in soup.findAll('li'):
                    if item:
                        if item.a.get('href') not in false_positives:
                            try:
                                vidcount = item.findAll('span', {'class': 'nb_cat border-radius-5'})[0].string.encode(
                                    'UTF-8')
                                vidcount = re.sub('\svideo[s]*', '', vidcount)
                            except:
                                vidcount = '0'
                            if vidcount and vidcount != '0':
                                img = item.find('img')
                                if img:
                                    try:
                                        img = img.get('data-lazy-src')
                                    except:
                                        try:
                                            img = img.get('src')
                                        except:
                                            img = ''
                                if not img:
                                     img = ''
                                title = item.a.get('title').encode('UTF-8') + ' (%s)' % vidcount
                                item_list.extend([{'site': site, 'mode': 'list', 'url': item.a.get('href'),
                                                   'content': '', 'title': title,
                                                   'cover_url': a.image(img, image),
                                                   'backdrop_url': a.art(), 'type': 3}])

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
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'class': 'listing-videos listing-extract'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            if soup:
                xbmcdict = XBMCDict(0).update(params)
                for item in soup.findAll('li', {'class': 'border-radius-5 box-shadow'}):
                    if item:
                        if item.a.get('href') not in false_positives:
                            _dict = xbmcdict.copy()
                            _dict['url'] = item.a.get('href')
                            _dict['title'] = item.a.get('title').encode('UTF-8')
                            _dict['tvshowtitle'] = _dict['title']
                            _dict['originaltitle'] = _dict['title']
                            img = item.find('img')
                            if img:
                                try:
                                    img = img.get('data-lazy-src')
                                except:
                                    try:
                                        img = img.get('src')
                                    except:
                                        img = ''
                            if not img:
                                 img = ''
                            _dict['cover_url'] = a.image(img)
                            _dict['thumb_url'] = _dict['cover_url']
                            _dict['poster'] = _dict['cover_url']
                            _dict['sub_site'] = site
                            plot = item.find('div', {'class': 'right'})
                            if plot:
                                plot = plot.p.contents[0].encode('utf-8')
                                _dict['plot'] = plot
                                _dict['plotoutline'] = plot
                            item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'pagination'}))
            last_item = False
            if soup:
                for item in soup.findAll('a'):
                    if (item.string.encode('UTF-8') == 'Last »') or (item.get('class') == 'last'):
                        last_item = item.get('href')
                        break
                if last_item is False:
                    for last_item in soup.findAll('a', {'class': 'inactive'}): pass
                    if last_item: last_item = last_item.get('href')
                item = soup.find('span', {'class': 'current'})
                if item:
                    if item.parent:
                        item = item.parent
                        if item.previousSibling:
                            if item.previousSibling.find('a'):
                                item_list.extend([{'site': site, 'mode': 'list',
                                                   'url': item.previousSibling.a.get('href'),
                                                   'content': params['content'],
                                                   'title': a.language(30017, True),
                                                   'cover_url': a.image('previous.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])
                        if item.nextSibling:
                            if item.nextSibling.find('a'):
                                item_list.extend([{'site': site, 'mode': 'list', 'url': item.nextSibling.a.get('href'),
                                                   'content': params['content'],
                                                   'title': a.language(30018, True),
                                                   'cover_url': a.image('next.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])
            if last_item:
                item_list.extend([{'site': site, 'mode': 'list', 'url': last_item, 'content': 'goto',
                                   'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                   'backdrop_url': a.art(), 'type': 3}])

            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'video-embed'}))
            item_list = []
            if soup:
                for script in soup.findAll(re.compile('s_*c_*r_*i_*p_*t')):
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
                if soup.find('iframe', src=True):
                    item = ''
                    for iframe in soup.findAll('iframe', src=True):
                        if iframe.get('data-lazy-src'):
                            item = iframe.get('data-lazy-src')
                            r = re.search('.+old=(.+)$', item)
                            if r:
                                item = r.group(1)
                        else:
                            item = iframe.get('src').replace('\\', '')
                        xbmcdict = XBMCDict(0).update(params)
                        if item:
                            _dict = xbmcdict.copy()
                            _dict['url'] = item
                            item_list.extend([_dict])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'video-infos'}))
            if soup:
                item = ''
                for p in soup.findAll('p'):
                    if p.iframe:
                        item = p.iframe.get('src')
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
