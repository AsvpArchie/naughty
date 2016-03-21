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
title = 'Filmikz XXX'
image = 'filmikz-icon.png'
art = 'filmikz-fanart.png'
order = 8


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        base_url = 'http://filmikz.ch'
        home_url = base_url + '/index.php?genre=14'
        search_url = home_url + '&search='
        false_positives = ['#']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30006), 'content': '',
                          'url': home_url, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                          'url': search_url, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(),
                          'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
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
                last_item = re.search('pg=([0-9]+)', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                last_item = int(last_item / 10)
                item = a.page_input(last_item)
                if item:
                    item = str(int(item) * 10)
                    params['url'] = re.sub('pg=[0-9]+', 'pg=' + str(item), params['url']).replace(' ', '+')
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('td', {'width': '490'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'movies'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '7200'
            params['sub_site'] = site
            if soup:
                addondict = AddonDict(0).update(params)
                for item in soup.findAll('table', {'width': '100%', 'height': '155'}):
                    _dict = addondict.copy()
                    ahref = item.find('a', {'href': True})
                    if ahref:
                        url = ahref.get('href')
                        if not url.startswith('http://'):
                            url = base_url + url
                        _dict['url'] = url
                        data = item.find('strong')
                        _dict['title'] = str(data.contents[0]).rstrip(' XXX :')
                        _dict['tvshowtitle'] = _dict['title']
                        _dict['originaltitle'] = _dict['title']
                        img = item.find('img')
                        if img:
                            img = img.get('src')
                            if not img.startswith('http://'):
                                img = base_url + '/' + img
                        else:
                            img = ''
                        _dict['cover_url'] = a.image(img)
                        _dict['thumb_url'] = _dict['cover_url']
                        _dict['poster'] = _dict['cover_url']
                        cast = item.find('p', text=re.compile('[Ss]tarring:.+'))
                        if cast:
                            _dict['plot'] = str(cast)
                            _dict['plotoutline'] = _dict['plot']
                            cast = re.search('[Ss]tarring:\s*(.+?)\s*\.+', str(cast))
                            if cast:
                                cast = cast.group(1)
                                _dict['cast'] = cast.split(', ')
                        item_list.extend([_dict])
                pages = BeautifulSoup(html, parseOnlyThese=SoupStrainer('table', {'width': '250'}))
                if pages:
                    previouspage = None
                    nextpage = None
                    lastpage = None
                    for ahref in pages.findAll('a', {'href': True}):
                        astr = ahref.string.encode('utf-8')
                        if astr == '‹‹ ':
                            previouspage = base_url + '/' + ahref.get('href')
                        elif astr == '››':
                            nextpage = base_url + '/' + ahref.get('href')
                        elif astr == ' Last ':
                            lastpage = base_url + '/' + ahref.get('href')
                            last_item = re.search('pg=(-*[0-9]+)', str(lastpage))
                            if last_item:
                                last_item = int(last_item.group(1))
                                if last_item < 10:
                                    lastpage = None
                    if previouspage:
                        item_list.extend([{'site': site, 'mode': 'list', 'url': previouspage, 'content': params['content'],
                                           'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])
                    if nextpage:
                        item_list.extend([{'site': site, 'mode': 'list', 'url': nextpage, 'content': params['content'],
                                           'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])
                    if lastpage:
                        item_list.extend([{'site': site, 'mode': 'list', 'url': lastpage, 'content': 'goto',
                                           'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('body'))
            item_list = []
            _bad_hosts = ['NowDownload', 'ePornik']
            if soup:
                buttons = soup.findAll('input', {'type': 'button', 'onclick': True})
                if buttons:
                    addondict = AddonDict(0).update(params)
                    for button in buttons:
                        value = button.get('value')
                        newhost = re.search('.+?-([a-zA-Z]+)', value)
                        if newhost:
                            newhost = newhost.group(1)
                        else:
                            newhost = ''
                        if newhost not in _bad_hosts:
                            item = button.get('onclick')
                            item = re.sub('javascript:popUp\([\'"](.+?)[\'"]\);*', '\g<01>', item)
                            item = base_url + item
                            value = button.get('value')
                            if not re.search('[Pp]art ', value):
                                try:
                                    thtml = a.get_page(item)
                                    tsoup = BeautifulSoup(thtml)
                                    source = tsoup.find('frame')
                                    if source:
                                        source = source.get('src')
                                        if 'ads.php' not in source:
                                            _dict = addondict.copy()
                                            _dict['url'] = source
                                            item_list.extend([_dict])
                                except:
                                    continue
                    parts = []
                    oldhost = ''
                    _dict = addondict.copy()
                    _dict['multi-part'] = True
                    for button in buttons:
                        value = button.get('value')
                        newhost = re.search('.+?-([a-zA-Z]+)', value)
                        if newhost:
                            newhost = newhost.group(1)
                        else:
                            newhost = ''
                        if newhost not in _bad_hosts:
                            item = button.get('onclick')
                            item = re.sub('javascript:popUp\([\'"](.+?)[\'"]\);*', '\g<01>', item)
                            item = base_url + item
                            if re.search('[Pp]art ', value):
                                if oldhost != newhost:
                                    if oldhost != '':
                                        _dict['parts'] = parts
                                        item_list.extend([_dict])
                                        _dict = addondict.copy()
                                        _dict['multi-part'] = True
                                        parts = []
                                    oldhost = newhost

                                try:
                                    thtml = a.get_page(item)
                                    tsoup = BeautifulSoup(thtml)
                                    source = tsoup.find('frame')
                                    if source:
                                        source = source.get('src')
                                        if 'ads.php' not in source:
                                            parts.extend([source])
                                except:
                                    continue
                    if parts:
                        _dict['parts'] = parts
                        item_list.extend([_dict])
            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
