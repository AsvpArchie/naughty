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
title = 'Beeg'
image = 'beeg-icon.png'
art = 'beeg-fanart.png'
order = 10


class Site:
    def __init__(self, params):
        import re
        import json
        import urllib
        from addon import Addon
        from addondict import AddonDict

        a = Addon()
        site = self.__module__
        mode = params['mode']

        api_version = 'v5'
        recent_url = 'http://beeg.com/api/%s/index/main/0/pc' % api_version
        long_url = 'http://beeg.com/api/%s/index/tag/0/pc?tag=long%svideos' % (api_version, '%20')
        search_url = 'http://beeg.com/api/%s/index/search/0/pc?query=' % api_version
        tag_url = 'http://beeg.com/api/%s/index/tag/0/pc?tag=' % api_version
        img_url = 'http://img.beeg.com/236x177/%s.jpg'

        data_markers = 'data=pc.US'

        if mode == 'main':
            item_list = [{'site': site, 'mode': 'list', 'title': a.language(30003), 'content': '',
                          'url': recent_url, 'cover_url': a.image('recent.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'categories', 'title': a.language(30005), 'content': '',
                          'url': recent_url, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(),
                          'type': 3},
                         {'site': site, 'mode': 'list', 'title': a.language(30039), 'content': '',
                          'url': long_url, 'cover_url': a.image('longvideos.png', image), 'backdrop_url': a.art(),
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
            data = json.loads(html)
            item_list = []
            tags = data.get('tags', None)
            if tags:
                popular = tags.get('popular', None)
                if popular:
                    for item in popular:
                        url_item = re.search('(.+?)-', str(item))
                        if url_item: url_item = url_item.group(1)
                        else: url_item = item
                        item_list.extend([{'site': site, 'mode': 'list', 'url': tag_url + url_item,
                                           'content': '', 'title': str(item).capitalize(),
                                           'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
                nonpopular = tags.get('nonpopular', None)
                if nonpopular:
                    for item in nonpopular:
                        url_item = re.search('(.+?)-', str(item))
                        if url_item: url_item = url_item.group(1)
                        else: url_item = item
                        item_list.extend([{'site': site, 'mode': 'list', 'url': tag_url + urllib.quote(url_item),
                                           'content': '', 'title': str(item).capitalize(),
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
                last_item = re.search('/([0-9]+)/pc', params['url'])
                if last_item:
                    last_item = int(last_item.group(1))
                else:
                    last_item = 10000
                item = a.page_input(last_item)
                if item:
                    params['url'] = re.sub('/[0-9]+/pc', '/' + str(item) + '/pc', params['url']).replace(' ', '+')
                else:
                    exit(1)
            html = a.get_page(params['url'])
            item_list = []
            data = json.loads(html)
            allvideos = []
            videos = data.get('videos', None)
            if videos:
                for video in videos:
                    nt_name = video.get('nt_name', '').encode('utf-8', 'ignore')
                    ps_name = video.get('ps_name', '').encode('utf-8', 'ignore')
                    atitle = video.get('title', '').encode('utf-8', 'ignore')
                    vid_id = video.get('id', '').encode('utf-8', 'ignore')
                    if nt_name.lower() == 'na': nt_name = ''
                    if ps_name.lower() == 'na': ps_name = ''
                    atitle = '%s - %s' % (atitle, ps_name)
                    if nt_name:
                        atitle += ' (%s)' % nt_name
                    if vid_id:
                        allvideos.append([vid_id, atitle, video])

                if allvideos:
                    params['mode'] = 'play'
                    params['content'] = 'episodes'
                    params['type'] = 0
                    params['context'] = 0
                    params['duration'] = '480'
                    params['sub_site'] = site
                    addondict = AddonDict(0).update(params)

                    for number, name, idata in allvideos:
                        _dict = addondict.copy()
                        _dict['title'] = name
                        _dict['tvshowtitle'] = _dict['title']
                        _dict['originaltitle'] = _dict['title']
                        _dict['cover_url'] = a.image(img_url % number)
                        _dict['thumb_url'] = _dict['cover_url']
                        _dict['poster'] = _dict['cover_url']
                        _dict['url'] = params['url']
                        _dict['count'] = number
                        item_list.extend([_dict])
                    pages = data.get('pages', 0)
                    if pages != 0:
                        pages -= 1
                    page = re.search('/([0-9]+)/pc', params['url'])
                    if page:
                        page = int(page.group(1))
                    else:
                        page = 0
                    previouspage = None
                    nextpage = None
                    lastpage = None
                    if page > 0:
                        previouspage = re.sub('/[0-9]+/pc', '/' + str(page - 1) + '/pc', params['url'])
                    if pages > 1:
                        lastpage = re.sub('/[0-9]+/pc', '/' + str(pages) + '/pc', params['url'])
                    if page < pages:
                        nextpage = re.sub('/[0-9]+/pc', '/' + str(page + 1) + '/pc', params['url'])

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
            data = json.loads(html)
            video = None
            videos = data.get('videos', None)
            if videos:
                for vid in videos:
                    if vid.get('id', None) == params['count']:
                        video = vid
                        break
                if video:
                    img = img_url % video.get('id')
                    name = params['title']
                    url = video.get('720p', None)
                    if not url:
                        url = video.get('480p', None)
                        if not url:
                            url = video.get('240p', None)
                    if url:
                        url = 'http:' + re.sub('\{DATA_MARKERS\}', data_markers, url)
                        from playback import Playback
                        Playback().play_this(url, name, img, a.common.usedirsources())
                    else:
                        a.alert(a.language(30904, True), sound=False)