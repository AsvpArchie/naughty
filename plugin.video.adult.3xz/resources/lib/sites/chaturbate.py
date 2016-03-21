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
title = 'Chaturbate'
image = 'chaturbate-icon.png'
art = 'chaturbate-fanart.png'
order = 11


class Site:
    def __init__(self, params):
        import re
        from addon import Addon
        from addondict import AddonDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        site = self.__module__
        mode = params['mode']

        base_url = 'https://chaturbate.com'
        home_url = base_url

        false_positives = ['#']

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30021), 'content': '',
                          'url': home_url, 'cover_url': a.image('featuredcams.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'bygender', 'title': a.language(30017), 'content': '',
                          'cover_url': a.image('bygender.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'byage', 'title': a.language(30018), 'content': '',
                          'cover_url': a.image('byage.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'byregion', 'title': a.language(30019), 'content': '',
                          'cover_url': a.image('byregion.png', image), 'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'bystatus', 'title': a.language(30020), 'content': '',
                          'cover_url': a.image('bystatus.png', image), 'backdrop_url': a.art(), 'type': 3}]
            item_list.extend(a.favs_hist_menu(site))
            item_list.extend(a.extended_menu())
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'bygender':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30022), 'content': '',
                          'url': base_url + '/female-cams/', 'cover_url': a.image('femalecams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30023), 'content': '',
                          'url': base_url + '/male-cams/', 'cover_url': a.image('malecams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30024), 'content': '',
                          'url': base_url + '/couple-cams/', 'cover_url': a.image('couplecams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30025), 'content': '',
                          'url': base_url + '/transsexual-cams/', 'cover_url': a.image('transcams.png', image),
                          'backdrop_url': a.art(), 'type': 3}]
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'byage':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30026), 'content': '',
                          'url': base_url + '/teen-cams/', 'cover_url': a.image('teencams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30027), 'content': '',
                          'url': base_url + '/18to21-cams/', 'cover_url': a.image('18to21cams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30028), 'content': '',
                          'url': base_url + '/20to30-cams/', 'cover_url': a.image('20to30cams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30029), 'content': '',
                          'url': base_url + '/30to50-cams/', 'cover_url': a.image('30to50cams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30030), 'content': '',
                          'url': base_url + '/mature-cams/', 'cover_url': a.image('maturecams.png', image),
                          'backdrop_url': a.art(), 'type': 3}]
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'byregion':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30031), 'content': '',
                          'url': base_url + '/north-american-cams/', 'cover_url': a.image('north-americancams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30032), 'content': '',
                          'url': base_url + '/other-region-cams/', 'cover_url': a.image('other-regioncams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30033), 'content': '',
                          'url': base_url + '/euro-russian-cams/', 'cover_url': a.image('euro-russiancams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30034), 'content': '',
                          'url': base_url + '/philippines-cams/', 'cover_url': a.image('philippinescams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30035), 'content': '',
                          'url': base_url + '/asian-cams/', 'cover_url': a.image('asiancams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30036), 'content': '',
                          'url': base_url + '/south-american-cams/', 'cover_url': a.image('south-americancams.png', image),
                          'backdrop_url': a.art(), 'type': 3}]
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'bystatus':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30037), 'content': '',
                          'url': base_url + '/exhibitionist-cams/', 'cover_url': a.image('exhibitionistcams.png', image),
                          'backdrop_url': a.art(), 'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30038), 'content': '',
                          'url': base_url + '/hd-cams/', 'cover_url': a.image('hdcams.png', image),
                          'backdrop_url': a.art(), 'type': 3}]
            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'list':
            if params.get('content', '') == 'goto':
                last_item = re.search('page=([0-9]+)', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    params['url'] = re.sub('page=[0-9]+', 'page=' + str(item), params['url']).replace(' ', '+')
                else:
                    exit(1)
            html = a.get_page(params['url'])
            soup = BeautifulSoup(html, parseOnlyThese=SoupStrainer('div', {'class': 'c-1 endless_page_template'}))
            item_list = []
            params['mode'] = 'play'
            params['content'] = 'episodes'
            params['type'] = 0
            params['context'] = 0
            params['duration'] = ''
            params['sub_site'] = site
            if soup:
                ul = soup.find('ul', {'class': 'list'})
                if ul:
                    addondict = AddonDict(0).update(params)
                    for item in ul.findAll('li'):
                        _dict = addondict.copy()
                        clip_link = item.find('a')
                        if clip_link:
                            url = clip_link.get('href')
                            if not url.startswith('http://'):
                                url = base_url + url
                            _dict['url'] = url
                            ctitle = ''
                            cage = ''
                            cname = ''
                            ccams = ''
                            details = item.find('div', {'class': 'details'})
                            if details:
                                temp = details.find('a')
                                if temp:
                                    cname = str(temp.contents[0])
                                temp = details.find('span', {'class': re.compile('age.*')})
                                if temp:
                                    cage = temp.string.encode('utf-8')
                                temp = details.find('li', {'class': 'cams'})
                                if temp:
                                    ccams = str(temp.contents[0])
                                temp = details.find('li', {'title': True})
                                if temp:
                                    ctitle = temp.get('title').encode('UTF-8')
                            if cname:
                                usetitle = '%s [%syr, %s] %s' % (cname, cage, ccams, ctitle)
                                _dict['title'] = usetitle
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

                    pages = BeautifulSoup(html, parseOnlyThese=SoupStrainer('ul', {'class': 'paging'}))
                    if pages:
                        previouspage = pages.find('a', {'class': re.compile('prev.*')})
                        nextpage = pages.find('a', {'class': re.compile('next.*')})
                        lastpage = pages.find('span', {'class': 'endless_separator'})
                        if lastpage:
                            lastpage = lastpage.findNext('a')

                        if previouspage:
                            previouspage = previouspage.get('href').replace(' ', '+')
                            if previouspage != '#':
                                if not previouspage.startswith('http://'):
                                    previouspage = base_url + previouspage
                                item_list.extend([{'site': site, 'mode': 'list', 'url': previouspage, 'content': params['content'],
                                                   'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])
                        if nextpage:
                            nextpage = nextpage.get('href').replace(' ', '+')
                            if nextpage != '#':
                                if not nextpage.startswith('http://'):
                                    nextpage = base_url + nextpage
                                item_list.extend([{'site': site, 'mode': 'list', 'url': nextpage, 'content': params['content'],
                                                   'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])
                        if lastpage:
                            lastpage = lastpage.get('href').replace(' ', '+')
                            if lastpage != '#':
                                if not lastpage.startswith('http://'):
                                    lastpage = base_url + lastpage
                                item_list.extend([{'site': site, 'mode': 'list', 'url': lastpage, 'content': 'goto',
                                                   'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                                   'backdrop_url': a.art(), 'type': 3}])

            a.add_items(item_list)
            a.end_of_directory()

        elif mode == 'play':
            html = a.get_page(params['url'])
            link = re.search('html \+= "src=\'(.+?)\'', html)
            if link:
                from playback import Playback
                Playback().play_this(link.group(1), params['title'], params['cover_url'], a.common.usedirsources())
            else:
                a.alert(a.language(30904, True), sound=False)
