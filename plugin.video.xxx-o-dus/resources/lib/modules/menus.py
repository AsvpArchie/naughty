"""
    Copyright (C) 2016 ECHO Coder

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
import xbmc,xbmcplugin,os,urllib
import kodi
import log_utils
import helper
import utils
import search
import downloader
import parental
import history
import favorites
from resources.lib.pyxbmct_.github import xxxgit
from scrapers import __all__
from scrapers import *

buildDirectory = utils.buildDir
specific_icon       = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork/resources/art/', '%s/icon.png'))
specific_fanart     = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork/resources/art/', '%s/fanart.jpg'))

@utils.url_dispatcher.register('0')
def mainMenu():

    art = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork/resources/art/', 'main/%s.png'))

    dirlst = []
    c = []
    
    if kodi.get_setting('mobile_mode') == 'true':
        c += [(kodi.giveColor('Mobile Mode ON','deeppink',True),None,19,None,'Mobile Mode auto selects low bandwidth files to limit mobile data usage.',False)]
    c += [
         (kodi.giveColor('Welcome to XXX-O-DUS Version %s' % kodi.get_version() ,'dodgerblue',True),xbmc.translatePath(os.path.join(kodi.addonfolder, 'resources/files/information.txt')),17,'icon','All issues must be reported at https://github.com/xibalba10/plugin.video.xxx-o-dus/issues or I will not know the issues exist. I will not provide support at any other location as one central place for everyone to see and discuss issues benefits everyone.',False), \
         (kodi.giveColor(kodi.countGitHubIssues('https://github.com/xibalba10/plugin.video.xxx-o-dus/issues'),'dodgerblue',True) + kodi.giveColor(' | Click To View Issues','white',True),None,34,'report','All issues must be reported at https://github.com/xibalba10/plugin.video.xxx-o-dus/issues or I will not know the issues exist. I will not provide support at any other location as one central place for everyone to see and discuss issues benefits everyone.',False), \
         ('Search...',None,29,'search','Search XXX-O-DUS',True), \
         ('Chaturbate',None,300,'chaturbate','Chaturbate',True), \
         ('Tubes',None,4,'tubes','Videos',True), \
         ('Parental Controls',None,5,'parental_controls','View/Change Parental Control Settings.',True), \
         ('Your History',None,20,'history','View Your History.',True), \
         ('Your Favourites',None,23,'favourites','View Your Favourites.',True), \
         ('Your Downloads',None,27,'downloads','View Your Downloads.',True), \
         ('Your Settings',None,19,'settings','View/Change Addon Settings.',False), \
         #('View Disclaimer',xbmc.translatePath(os.path.join(kodi.addonfolder, 'resources/files/disclaimer.txt')),17,'disclaimer','View XXX-O-DUS Disclaimer.',False), \
         ('View Addon Information',xbmc.translatePath(os.path.join(kodi.addonfolder, 'resources/files/information.txt')),17,'addon_info','View XXX-O-DUS Information.',False), \
         ('RESET XXX-O-DUS',None,18,'reset','Reset XXX-O-DUS to Factory Settings.',False), \
         (kodi.giveColor('Report Issues @ https://github.com/xibalba10/plugin.video.xxx-o-dus/issues','white',True),xbmc.translatePath(os.path.join(kodi.addonfolder, 'resources/files/information.txt')),17,'report','All issues must be reported at https://github.com/xibalba10/plugin.video.xxx-o-dus/issues or I will not know the issues exist. I will not provide support at any other location as one central place for everyone to see and discuss issues benefits everyone.',False), \
         ]
    
    for i in c:
        icon    = art % i[3]
        fanart  = kodi.addonfanart
        dirlst.append({'name': kodi.giveColor(i[0],'white'), 'url': i[1], 'mode': i[2], 'icon': icon, 'fanart': fanart, 'description': i[4], 'folder': i[5]})

    buildDirectory(dirlst, cache=False)
    
@utils.url_dispatcher.register('4')
def VIDEOS():

    sources = __all__ ; video_sources = []; base_name = []; menu_mode = []; art_dir = []
    sources = [i for i in sources if i != 'chaturbate']
    for i in sources:
        try:
            if eval(i + ".type") == 'video': 
                base_name.append(eval(i + ".base_name"))
                menu_mode.append(eval(i + ".menu_mode"))
                art_dir.append(i)
                video_sources = zip(base_name,menu_mode,art_dir)
        except: pass

    if video_sources:
        dirlst = []
        for i in sorted(video_sources):
            dirlst.append({'name': kodi.giveColor(i[0],'white'), 'url': None, 'mode': i[1], 'icon': specific_icon % i[2], 'fanart': specific_fanart % i[2], 'folder': True})

    buildDirectory(dirlst)