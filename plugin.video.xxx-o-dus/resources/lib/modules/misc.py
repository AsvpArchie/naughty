import xbmc,xbmcgui,os,shutil
import kodi
import utils
import log_utils

@utils.url_dispatcher.register('17',['url'])
def VIEW_DIALOG(url):

    with open(url,mode='r')as f: msg = f.read()
    kodi.TextBoxes("%s" % msg)

    if url == xbmc.translatePath(os.path.join(kodi.addonfolder , 'resources/reset.txt')):
        return

@utils.url_dispatcher.register('18')
def RESET():

    VIEW_DIALOG(xbmc.translatePath(os.path.join(kodi.addonfolder , 'resources/reset.txt')))
    choice = xbmcgui.Dialog().yesno("[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]", '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]')
    if choice:
        download_location   = kodi.get_setting("download_location")
        download_folder     = xbmc.translatePath(download_location)

        extensions = ['.mp4']

        for file in os.listdir(download_folder):
            for extension in extensions:
                if file.endswith(extension):
                    try:
                        path = xbmc.translatePath(os.path.join(download_folder, file))
                        os.remove(path)
                    except:
                        kodi.dialog.ok(kodi.get_name(), "[COLOR white]There was an error deleting %s[/COLOR]" % file)
                        pass
        try:
            shutil.rmtree(kodi.datafolder)
        except:
            kodi.dialog.ok(kodi.get_name(), "[COLOR white]There was an error deleting deleting the data directory.[/COLOR]")
            quit()
        kodi.dialog.ok(kodi.get_name(), "[COLOR white]XXX-O-DUS has been reset to the factory state.[/COLOR]","[COLOR white]Press OK to continue.[/COLOR]")
        xbmc.executebuiltin("Container.Refresh")
