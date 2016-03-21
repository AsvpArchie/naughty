import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.aob'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'aob.db')
net = Net()
addon = Addon('plugin.video.aob', sys.argv)

BASE_URL1 = 'http://adultbay.org/'
BASE_URL2 = 'http://www.hornywhores.net/'
BASE_URL3 = 'http://www.naughtyblog.org/'
BASE_URL4 = 'http://pornorips.com/'
BASE_URL5 = 'http://scnlog.eu/'
BASE_URL6 = 'http://pornreleasez.com/'
BASE_URL7 = 'http://xxxstreams.org/'
BASE_URL8 = 'http://webwarez.it/'
BASE_URL35 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'
BASE_URL9 = 'http://anyporn.com/'
BASE_URL10 = 'http://www.rabbittube.xxx/'
BASE_URL11 = 'http://www.discovery360.net/'
BASE_URL12 = 'http://pornve.com/'
BASE_URL14 = 'http://extbb.com/'

######PATHS########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)

#################################################################################### Get Movie Titles #####################################################################################

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): # adult-bay
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################################################################################################################################

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): # hornywhores
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="post">\s*?<h2 id="post-.+?"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks2', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #naughtyblog
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################################################################################################################

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): # pornorips
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content 
                match = re.compile('entry.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): #scenelog
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('title="" /><a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h1>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'sl2.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################################

def GetTitles6(section, url, startPage= '1', numOfPages= '1'): # pornreleasez
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content  
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles6', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################################

def GetTitles7(section, url, startPage= '1', numOfPages= '1'): # naked
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<img src="(.+?)"/>  </a><a href="(.+?)"  class="more-link">.+?<span class="screen-reader-text">(.+?)</span> <span class="meta-nav">.+?</span></a></p>', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles7', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################################

def GetTitles8(section, url, startPage= '1', numOfPages= '1'): # webwarez
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="quadrato">\s*?<a href="(.+?)" title="(.+?)"><p style=".+?"><img src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles8', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################################################################################

def GetTitles9(section, url, startPage= '1', numOfPages= '1'): #anyporn
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="th">\s*?<a href="(.+?)"  data-rt=".+?" title="(.+?)">\s*?<img src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetTitles9a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles9', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles9a(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("video_url: '(.+?)'").findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo2', 'url': url, 'listitem': listitem}, {'title':  'load stream'}, img= '', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): #rabbittube
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<span class="title">(.+?)</span>\s*?</a>\s*?<a href="(.+?)" class="thumb">\s*?<span class="img">\s*?<img src="(.+?)"', re.DOTALL).findall(html)
                for name, movieUrl, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetTitles9a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################

def GetTitles14(section, url, startPage= '1', numOfPages= '1'):  #extbb.com
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h2 class="postTitle"><span></span><a href="(.+?)">(.+?)</a></h2>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.aob/?mode=Search3&query=%s)' %(name.strip())
        		cm.append(('[COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, contextmenu_items= cm, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################################################################################################################

def GetTitles12(section, url, startPage= '1', numOfPages= '1'):  #pornve
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="vid_bloczk">\s*?<a href="(.+?)" class=".+?" style="background-image:ur.+?http://(.+?).jpg.+?;"><span>.+?</span></a>\s*?<div colspan=2 class="vb_title"><a href=".+?" class="link"><b>(.+?)</b></a></div>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetTitles12a', 'section': section, 'url': movieUrl}, {'title':  name.strip().replace('.', ' ')}, img= 'http://' + img + '.jpg', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')  
        setView('tvshows', 'tvshows-view')       
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles12a(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<IFRAME SRC="(.+?)"').findall(content)
        for url in match:
                addon.add_directory({'mode': 'GetTitles12b', 'url': url, 'listitem': listitem}, {'title':  'get stream'}, img= 'http://pornve.com/images/logo.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles12b(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('file:"(.+?)"').findall(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo2', 'url': url, 'listitem': listitem}, {'title':  'load stream'}, img= 'http://pornve.com/images/logo.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- github iptv -------------------------------------------------------------------------------------#

def GetTitles35(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo2', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- github help -----------------------------------------------------------------------------------#

def GetTitles37(url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo1(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")



##.replace('/', ' ')## \s*? ##
######################################################################## Get Links ####################################################################################################

def GetLinks(section, url): # Get Links
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        match1 = re.compile("href='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## Get Links2 ####################################################################################################

def GetLinks2(section, url): # Get Links2
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><a href="(.+?)"').findall(content)
        match2 = re.compile('<a href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match2:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## Get Links3 ####################################################################################################

def GetLinks3(section, url): # Get Links3
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        match2 = re.compile('src="(.+?)"').findall(content)
        match3 = re.compile('<p><a href=".+?">(.+?)</a></p>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match2 + match3:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                        
                # ignore .rar files
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                        title = title.replace('x264','')
                        title = title.replace('XXX','[COLOR red][B][I]XXX[/B][/I][/COLOR]')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        host = host.replace('k2s.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('keep2share.cc','[COLOR red]Unsupported Link[/COLOR]')
                        host = host.replace('ryushare.com','[COLOR red]Unsupported Link[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' [COLOR pink][B]:-[/B][/COLOR] ' + title}, img=IconPath + 'play1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks8a(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('streamer: "(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo2', 'url': url, 'listitem': listitem}, {'title': url}, img=IconPath + 'play.png', fanart= 'http://hatterkep.eu/wallpapers/16/img-4606.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################################################################################

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")



def PlayVideo2(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='https://lh5.googleusercontent.com/-p2h0tx7Trgs/Uzu-3kxzKuI/AAAAAAAAOsU/sVJKqxSMY-4/s319/watch2.jpg', thumbnailImage= 'http://s29.postimg.org/8z8jd5x5j/logo1.png')
        li.setProperty('fanart_image', '')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

############################################################################################################################################

def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] : [COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'msearch.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu1'}, {'title':  '[COLOR hotpink][B]Adult bay >[/B][/COLOR] >'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu2'}, {'title':  '[COLOR hotpink][B]Horny Whores >[/B][/COLOR] >'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu3'}, {'title':  '[COLOR hotpink][B]Naughty Blog >[/B][/COLOR] >'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu5'}, {'title':  '[COLOR hotpink][B]SceneLog XXX >[/B][/COLOR] >'}, img=IconPath + 'sl2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu6'}, {'title':  '[COLOR hotpink][B]PornReleasez >[/B][/COLOR] >'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu4'}, {'title':  '[COLOR hotpink][B]PornoRips >[/B][/COLOR] >'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu7'}, {'title':  '[COLOR hotpink][B]Naked XXX >[/B][/COLOR] >'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Menu8'}, {'title':  '[COLOR hotpink][B]webwarez >[/B][/COLOR] >'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'Menu9'}, {'title':  '[COLOR hotpink][B]Free porn >[/B][/COLOR] >'}, img=IconPath + 'fp.png', fanart=FanartPath + 'fanart.png')

        #addon.add_directory({'mode': 'GetTitles35', 'url': BASE_URL35 + '/black.txt'}, {'title':  '[COLOR hotpink][B]FREE Streams & V.O.D >[/COLOR][/B] >'}, img=IconPath + 'lsv.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR] - [COLOR pink]real-debird & alldebird login[/COLOR]'}, img=IconPath + 'rset.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR red]FOR HELP PLEASE GOTO...[/COLOR] [COLOR blue][B][I]www.xbmchub.com[/B][/I][/COLOR]'}, img=IconPath + 'help2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR hotpink][B]News & Help  >[/B][/COLOR] >'}, img=IconPath + 'hn.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[B][COLOR yellow]www.entertainmentrepo.com  [/B][/COLOR]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Adult's Only [COLOR deeppink][B]HUB[/B][/COLOR]","                         [COLOR red]XXX[/COLOR] [COLOR pink][B]OVER 18's/ 21's ONLY !!![/B][/COLOR] [COLOR red]XXX[/COLOR]" , "       [COLOR pink]Works better with a debrid premium account[/COLOR]" , '        [COLOR lime][B]              !!! ARE YOU OVER 18/21 !!![/COLOR][/B]','[COLOR red]NO & EXIT[/COLOR]','[COLOR lime]YES[/COLOR]'):
                exit
        else:
                exit()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------help---------------------------------------help-----------------------------help--------------------------help-------------------------------help-------#

def HelpMenu(): 
        addon.add_directory({'mode': 'Help'}, {'title':  'Adults Only [COLOR deeppink][B]HUB[/B][/COLOR] : [COLOR lime]News >[/COLOR] >'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        addon.add_directory({'mode': 'GetTitles37', 'url': BASE_URL35 + '/help.txt'}, {'title':  '[COLOR deeppink]How to videos >[/COLOR] >'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg') 
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]If you like this addon[/COLOR][/B]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]& you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR blue]System/Add-ons/Get Add-ons/entertainmentrepo[/COLOR][/B]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR aqua]@MrEntertainRepo & www.entertainmentrepo.com[/COLOR][/B] - [B][COLOR gold]Add me on twitter for all the latest news & updates..[/COLOR][/B]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu1():    #adult bay
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/hdtv/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/hdtv/1080p/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX 1080p>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ab1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]Adult Bay[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################

def Menu2():    #hornywhores
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/category/movies/dvd-r/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies DVD-R>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'hw1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]Horny Whores[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#############################################################################################################

def Menu3():    #NaughtyBlog
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/siterips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies SiteRips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Latest>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/paysites/brazzers/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Brazzers Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/paysites/bangbros/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Bangbros Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/paysites/teamskeet/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Teamskeet Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/clips/casting/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Casting Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'nb1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR green]Search[/COLOR] [COLOR pink]NaughtyBlog[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################################################

def Menu4():    #PornoRips
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/hd-porn/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/no-english-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies None english>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/adult-sites-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies SiteRips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu5():    #SceneLog
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD 1080p 720p SceneLog >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'sl2.png', fanart=FanartPath + 'fanart.png')

        #addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/nsfw/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies ExtBB.com Porn Content >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'sl2.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu6():    #pornreleasez
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/clips-hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/dvdr/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Dvdr>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/movies-hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/site-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Site Rips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/movies/vintage/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Vintage>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/category/clips/celebrity/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Celebrity>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pr2.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu7():    #naked
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/new-porn-streaming/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/tag/hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX HD>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles7', 'section': 'ALL', 'url': BASE_URL7 + '/full-movies-streaming/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Movies >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ns.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu8():  #webwarez
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest added>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/straight/clips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/movies-xxx/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/straight/movies-xxx/international-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest international movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/film-porno-italian/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest italian movies>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/?s=played.to',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX FREE played.to links>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/clips/?s=Brazzers',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest Brazzers Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/clips/?s=BangBros',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX Latest BangBros Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/category/clips/?s=NaughtyAmerica',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX NaughtyAmerica Clips>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###########################################################################################################

def Menu9():  #free
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + 'newest/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<< Anyporn >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ap.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/videos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<< Rabbittube >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'rab.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<< Pornve >>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'pv.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/xxx/?s=played.to',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR pink]<<XXX FREE played.to links>>[/COLOR] [COLOR red]<<OVER 18s ONLY...>>[/COLOR]'}, img=IconPath + 'ww1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################### viewType  ##########################################################################

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

######################################################################## searches #################################################################################################

#hw
def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]Horny Whores[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return  
def Search(query):
        url = 'http://www.hornywhores.net/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################

#ab
def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]Adult Bay[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return  
def Search1(query):
        url = 'http://adultbay.org/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################

#nb
def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR] [COLOR pink]NaughtyBlog[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return  
def Search2(query):
        url = 'http://www.naughtyblog.org/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------mega search---------------------------------------------------------------------------------------#

def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] : [COLOR hotpink][B]A[/B][/COLOR]dult [COLOR hotpink][B]HUB[/B][/COLOR] [COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return  
def Search3(query):
    try:
        url = 'http://www.hornywhores.net/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="post">\s*?<h2 id="post-.+?"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]hornywhores[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry hornywhores search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://adultbay.org/search/ ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('post_headerr.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]adultbay[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry adultbay search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.naughtyblog.org/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]NaughtyBlog[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry naughtyblog search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://pornreleasez.com/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]pornreleasez[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry pornreleasez search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://scnlog.eu/?s= ' + query + '&cat=9'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('title="" /><a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h1>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]scnlog[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry scnlog search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://pornorips.com/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<center><h2><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2></center>\s*?</div>\s*?<div class="post-content" style="padding-top:7px;">\s*?<div class="thumb">\s*?<a href=".+?" rel="bookmark" title= ".+?"><img src="(.+?)" ', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]pornorips[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry pornorips search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://webwarez.it/xxx/?s= ' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="quadrato">\s*?<a href="(.+?)" title="(.+?)"><p style=".+?"><img src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks3', 'url': url}, {'title':  title + ' - ' + '[COLOR pink]webwarez[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry webwarez search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://xxxstreams.org/?s=' + query +'&cat=0'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<img src="(.+?)"/>  </a><a href="(.+?)"  class="more-link">.+?<span class="screen-reader-text">(.+?)</span> <span class="meta-nav">.+?</span></a></p>', re.DOTALL).findall(html)
        for img, title, url in match:
                addon.add_directory({'mode': 'GetLinks3', 'url': url}, {'title': title + ' - ' + '[COLOR pink]xxxstreams (new)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry xxxstreams search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##.replace('/', ' ')## \s*? ##
##########################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(section, url, startPage, numOfPages)
elif mode == 'GetTitles5': 
	GetTitles5(section, url, startPage, numOfPages)	
elif mode == 'GetTitles6': 
	GetTitles6(section, url, startPage, numOfPages)	
elif mode == 'GetTitles7': 
	GetTitles7(section, url, startPage, numOfPages)
elif mode == 'GetTitles8': 
	GetTitles8(section, url, startPage, numOfPages)
elif mode == 'GetLinks8a':
	GetLinks8a(section, url)
elif mode == 'GetTitles9': 
	GetTitles9(section, url, startPage, numOfPages)
elif mode == 'GetTitles9a': 
	GetTitles9a(url)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles11': 
	GetTitles11(section, url, startPage, numOfPages)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles12a': 
	GetTitles12a(url)
elif mode == 'GetTitles12b': 
	GetTitles12b(url)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles35': 
	GetTitles35(url)
elif mode == 'GetTitles37': 
	GetTitles37(url)
elif mode == 'Categories':
        Categories(section)
elif mode == 'Categories1':
        Categories1(section)
elif mode == 'Menu0':
        Menu0()
elif mode == 'Menu1':
        Menu1()
elif mode == 'Menu2':
        Menu2()
elif mode == 'Menu3':
        Menu3()
elif mode == 'Menu4':
        Menu4()
elif mode == 'Menu5':
        Menu5()
elif mode == 'Menu6':
        Menu6()
elif mode == 'Menu7':
        Menu7()
elif mode == 'Menu8':
        Menu8()
elif mode == 'Menu9':
        Menu9()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks2':
	GetLinks2(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)
elif mode == 'PlayVideo2':
	PlayVideo2(url, listitem)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'Help':
    import helpbox
    helpbox.HelpBox()

xbmcplugin.endOfDirectory(int(sys.argv[1]))