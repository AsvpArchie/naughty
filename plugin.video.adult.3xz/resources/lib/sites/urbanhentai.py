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
title = 'Urbanhentai'
image = 'urbanhentai-icon.png'
art = 'urbanhentai-fanart.png'
order = 9


class Site:
    def __init__(self, params):
        import re
        import urllib2
        from addon import Addon
        from addondict import AddonDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        base_url = 'http://urbanhentai.com'
        home_url = base_url
        index_url = base_url + '/index/'
        latest_url = base_url + '/?orderby=date'
        search_url = base_url + '/?s='
        false_positives = ['#']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30012), 'content': '',
                          'url': latest_url, 'cover_url': a.image('latest.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                          'url': index_url, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(),
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
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'id': 'tag_cloud-2'}))
            item_list = []
            if soup:
                genre_list = soup.find('div', {'class': 'tagcloud'})
                if genre_list:
                    for item in soup.findAll('a'):
                        if item.get('href') not in false_positives:
                            cat_title = item.string.encode('UTF-8')
                            try:
                                cat_count = item.get('title').replace(' topics', '')
                                cat_title += ' (' + cat_count + ')'
                            except:
                                cat_count = None
                            item_list.extend([{'site': site, 'mode': 'list', 'url': item.get('href').replace(' ', '+'),
                                               'content': '', 'title': cat_title,
                                               'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
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
                last_item = re.search('/page/([0-9]+)/', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    params['url'] = re.sub('/page/[0-9]+/', '/page/' + str(item) + '/', params['url']).replace(' ', '+')
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': re.compile('loop-content.*')}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'episodes'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = '1500'
            params['sub_site'] = site
            if soup:
                addondict = AddonDict(0).update(params)
                for item in soup.findAll('div', {'id': re.compile('post-[0-9]+')}):
                    _dict = addondict.copy()
                    clip_link = item.find('a', {'class': 'clip-link'})
                    if clip_link:
                        url = clip_link.get('href')
                        if not url.startswith('http://'):
                            url = base_url + url
                        _dict['url'] = url
                        try:
                            _dict['title'] = clip_link.get('title').encode('UTF-8')
                        except:
                            data = item.find('h2', {'class': 'entry-title'})
                            if data:
                                _dict['title'] = str(data.a.contents[0])
                        _dict['tvshowtitle'] = _dict['title']
                        _dict['originaltitle'] = _dict['title']
                        img = item.find('img')
                        if img:
                            img = img.get('src')
                            if img.startswith('//'):
                                img = 'http:' + img
                        else:
                            img = ''
                        _dict['cover_url'] = a.image(img)
                        _dict['thumb_url'] = _dict['cover_url']
                        _dict['poster'] = _dict['cover_url']
                        item_list.extend([_dict])
                pages = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'wp-pagenavi'}))
                if pages:
                    previouspage = pages.find('a', {'class': 'previouspostslink'})
                    nextpage = pages.find('a', {'class': 'nextpostslink'})
                    lastpage = pages.find('a', {'class': 'last'})

                    if previouspage:
                        previouspage = previouspage.get('href').replace(' ', '+')
                        item_list.extend([{'site': site, 'mode': 'list', 'url': previouspage, 'content': params['content'],
                                           'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])
                    if nextpage:
                        nextpage = nextpage.get('href').replace(' ', '+')
                        item_list.extend([{'site': site, 'mode': 'list', 'url': nextpage, 'content': params['content'],
                                           'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])
                    if lastpage:
                        lastpage = lastpage.get('href').replace(' ', '+')
                        item_list.extend([{'site': site, 'mode': 'list', 'url': lastpage, 'content': 'goto',
                                           'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                           'backdrop_url': a.art(), 'type': 3}])

            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('video', {'id': 'video'}))
            item_list = []
            if soup:
                item = soup.find('source')
                try:
                    item = item.get('src')
                except:
                    item = None
                if item:
                    if base_url in item:
                        try:
                            opener = urllib2.build_opener()
                            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                                                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                'Chrome/45.0.2454.101 Safari/537.36')]
                            opener.addheaders = [('Referer', params['url'])]
                            opener.addheaders = [('Accept', 'text/html,application/xhtml+xml,'
                                                            'application/xml;q=0.9,image/webp,*/*;q=0.8')]
                            urllib2.install_opener(opener)
                            item = urllib2.urlopen(item).geturl()
                        except urllib2.HTTPError as e:
                            if item != e.geturl():
                                item = e.geturl()
                            else:
                                item = None
                    if item:
                        addondict = AddonDict(0).update(params)
                        _dict = addondict.copy()
                        _dict['url'] = item
                        item_list.extend([_dict])
            if item_list:
                from playback import Playback
                Playback().choose_sources(item_list)
            else:
                a.alert(a.language(30904, True), sound=False)
