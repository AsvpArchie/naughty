import xbmc,xbmcplugin,os,urlparse,re
import log_utils
import kodi
import cache
import client
import dom_parser2
import scraper_updater
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://justporno.tv'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 202
content_mode = 203
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'search?query=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
    scraper_updater.check(filename)
    
    try:
        url = base_domain
        c = client.request(url)
        r = dom_parser2.parse_dom(c, 'li')
        r = dom_parser2.parse_dom(r, 'a', req='title')
        r = [(urlparse.urljoin(base_domain,i.attrs['href']),i.content) for i in r if '/tag' in i.attrs['href']]
        if ( not r ):
            log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
            kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
            quit()
    except Exception as e:
        log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
        kodi.notify(msg='Fatal Error', duration=4000, sound=True)
        quit()
        
    dirlst = []

    if r:
        for i in r:
            try:
                iconimage = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % filename))
                fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
                name = kodi.sortX(i[1].encode('utf-8'))
                dirlst.append({'name': name, 'url': i[0], 'mode': content_mode, 'icon': iconimage, 'fanart': fanarts, 'folder': True})
            except Exception as e:
                log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)
    
        if dirlst: buildDirectory(dirlst)
        else:
            kodi.notify(msg='No Menu Items Found')
            quit()
            
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=None):

    pattern = r'''%s\=['"]+([^'"]+)'''

    try:
        c = client.request(url)
        r = dom_parser2.parse_dom(c, 'li')
        r = [i.content for i in r if 'thumb-item-desc' in i.content]
        if ( not r ):
            log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
            kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
    except Exception as e:
        log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
        kodi.notify(msg='Fatal Error', duration=4000, sound=True)
        quit()
        
    dirlst = []
    
    for i in r:
        try:
            name = re.findall(pattern % 'title', i)[0]
            name = kodi.sortX(name.encode('utf-8'))
            if searched: description = 'Result provided by %s' % base_name.title()
            else: description = name
            url  = re.findall(pattern % 'href', i)[0]
            iconimg = re.findall(pattern % 'src', i)[0]
            iconimg = 'http:%s' % iconimg if iconimg.startswith('//') else iconimg
            fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
            dirlst.append({'name': name, 'url': urlparse.urljoin(base_domain,url + '|SPLIT|%s' % base_name), 'mode': player_mode, 'icon': iconimg, 'fanart': fanarts, 'description': description, 'folder': False})
        except Exception as e:
            log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)
    
    if searched: 
        if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
        return str(len(r))
    else: 
        if dirlst: buildDirectory(dirlst, isVideo = True, isDownloadable = True)
        else:
            kodi.notify(msg='No Content Found')
            quit()