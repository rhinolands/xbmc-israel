# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc
__settings__ = xbmcaddon.Addon(id='plugin.video.KIDSIL')
ADDON = xbmcaddon.Addon(id='plugin.video.KIDSIL')
def CATEGORIES():
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.10qtv'):
                addDir('10Q סרטי אנימציה ','plugin://plugin.video.10qtv/?mode=6&name=אנימציה&url=http://www.10q.tv/board/filmy/animciha/5',8,'http://www.helicon.co.il/wp-content/uploads/2011/10/LionKing_920.jpg','')
                addDir('10Q  ומשפחה סרטי אנימציה ','plugin://plugin.video.10qtv/?mode=6&name=אנימציה&url=http://www.10q.tv/board/filmy/mshfhha/17',8,'http://2.bp.blogspot.com/-tkAp5l6dAJA/TyJw_RHiuzI/AAAAAAAACEs/jTFqK7ocFqg/s1600/dumbo+ears.jpg','')
        else:
                addDir('[COLOR red]10QTV לא מותקן[/COLOR]','','','','')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.seretil'):
                addDir('מדובבים seretil','plugin://plugin.video.seretil/?mode=4&name=סרטים מדובבים&url=http://seretil.me/category/סרטים-מדובבים/page/1/',8,'http://www.printime.co.il/image/users/16584/ftp/my_files/ariel.jpg','')
        else:
                addDir('[COLOR red]seretil לא מותקן[/COLOR]','','','','')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.movie25'):
                
                addDir('ללא דיבוב','plugin://plugin.video.movie25/?fanart=https%3a%2f%2fgithub.com%2fmash2k3%2fMashupArtwork%2fraw%2fmaster%2fart%2ffanart2.jpg&iconimage=https%3a%2f%2fencrypted-tbn3.gstatic.com%2fimages%3fq%3dtbn%3aANd9GcTR26WavA0VthRpyIneD6ERay2rnWOA5gxoWnfTDCfAWCfHcXg6&mode=236&name=Animated%20Movies%20%5bCOLOR%20red%5d%20Updated%2009%2f09%2f13%5b%2fCOLOR%5d&plot&url=https%3a%2f%2fgithub.com%2fmash2k3%2fStaael1982%2fraw%2fmaster%2fanimated_movies.xml',8,'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTR26WavA0VthRpyIneD6ERay2rnWOA5gxoWnfTDCfAWCfHcXg6','')
                addDir('ללא דיבוב 2','plugin://plugin.video.movie25/?fanart=http%3a%2f%2fs20.postimg.org%2ff1ov06599%2ffanart2.png&amp;iconimage=http%3a%2f%2fs20.postimg.org%2fsx4lyuvbx%2fkidzone.png&amp;mode=236&amp;name=KidZonE%20%5bCOLOR%20red%5d%20Updated%2017%2f09%2f13%5b%2fCOLOR%5d&amp;plot&amp;url=https%3a%2f%2fgithub.com%2fmash2k3%2fMashUpTNPB%2fraw%2fmaster%2fkidszone.xml',8,'http://s20.postimg.org/sx4lyuvbx/kidzone.png','')
        else:
               addDir('[COLOR red]MASHUP לא מותקן[/COLOR]','','','','')
               
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.wallaNew.video'):
                addDir('קלסיקלטת','plugin://plugin.video.wallaNew.video/?mode=1&module=338&name=קלסיקלטת&url=http://vod.walla.co.il/channel/338/clasicaletet',8,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTYE2VT8CR2O31MsqAhdaydYrqrCD--HCCdGcs7blBn3Zh92Kwq','')
                addDir('גוניור','plugin://plugin.video.wallaNew.video/?mode=1&module=junior&name=גוניור&url=http://junior.walla.co.il/',8,'http://upload.wikimedia.org/wikipedia/he/1/19/%D7%A2%D7%A8%D7%95%D7%A5_%D7%92%27%D7%95%D7%A0%D7%99%D7%95%D7%A8.jpg','')
                addDir('ניק גוניור ','plugin://plugin.video.wallaNew.video/?mode=1&module=nickjr&name=ניקלאודיון גוניור&url=http://nickjr.walla.co.il/',8,'http://www.imanoga.co.il/wp-content/uploads/2012/06/646457567.jpg','')
                addDir('וואלה ילדים','plugin://plugin.video.wallaNew.video/?mode=1&module=000003&name=ילדים&url=http://vod.walla.co.il/kids/',8,'https://lh6.ggpht.com/V8v_FzkTMqeLRg_oY7G00zf0bcxubsm659cLrbf9nEKMLHQG-5LSZdbbJGQgkV6j1PQ=w300','')
        else:
                addDir('[COLOR red]וואלה לא מותקן[/COLOR]','','','','')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.hotVOD.video'):
                addDir('HOT VOD YOUNG','plugin://plugin.video.hotVOD.video/?mode=5&name=%20HOT%20VOD%20YOUNG&url=http%3a%2f%2fhot.ynet.co.il%2fhome%2f0%2c7340%2cL-7449%2c00.html',8,'http://i28.tinypic.com/20o8lt.jpg','')
        else:
               addDir('[COLOR red]HOT VOD לא מותקן[/COLOR]','','','','')

        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.gozlan.me'):        
                addDir('אנימציה גוזלן','plugin://plugin.video.gozlan.me/?mode=1&name=%d7%a1%d7%a8%d7%98%d7%99%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&url=http%3a%2f%2fanonymouse.org%2fcgi-bin%2fanon-www.cgi%2fhttp%3a%2f%2fgozlan.co%2f%2fsearch.html%3fg%3d%25D7%2590%25D7%25A0%25D7%2599%25D7%259E%25D7%25A6%25D7%2599%25D7%2594',8,'http://thelazyandi.files.wordpress.com/2012/07/d790d79ed799d7a6d794-d79ed7a8d799d793d794.jpg','')
                addDir('משפחה גוזלן','plugin://plugin.video.gozlan.me/?mode=1&name=%d7%a1%d7%a8%d7%98%d7%99%20%d7%9e%d7%a9%d7%a4%d7%97%d7%94&url=http%3a%2f%2fanonymouse.org%2fcgi-bin%2fanon-www.cgi%2fhttp%3a%2f%2fgozlan.co%2f%2fsearch.html%3fg%3d%25D7%259E%25D7%25A9%25D7%25A4%25D7%2597%25D7%2594',8,'http://www.israjung.co.il/chochma/chochma6/sarig/narnia.files/image002.jpg','')
        else:
                 addDir('[COLOR red]GOZLAN לא מותקן[/COLOR]','','','','')
        addDir(' KIDS LIVE TV (benny 123)','https://dl.dropboxusercontent.com/u/94071174/Online/wow/Kids.plx',7,'http://www.livestream.com/filestore/logos/6a941358-6c7f-2ebf-e8ac-b05f4f338270-banner.png','')
        addDir('Baby Einstein','TerrapinStation5',9,'http://d202m5krfqbpi5.cloudfront.net/books/1170326163l/46377.jpg','1')
        YOUsubs('UC5RJ8so5jivihrnHB5qrV_Q')
        setView('movies', 'default')       

def update_view(url):

    ok=True        
    xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
    return ok
    
    
    


def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
#reads data from Benny123 Kids section 
def ListLive(url):
        link=OPEN_URL(url)
        matches=re.compile('name=(.*?)\\n.*?URL=(.*?)#',re.I+re.M+re.U+re.S).findall(link)

        for match in matches:
                url=match[1][:-2]
                addLink(match[0],url,'','')
        setView('tvshows', 'default')   


def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        if mode==8:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        else:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,iconimage,description):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok 


# reads  user names from my subscriptions 
def YOUsubs(user):
      murl='http://gdata.youtube.com/feeds/api/users/'+user+'/subscriptions?start-index=1&max-results=50'
      link=OPEN_URL(murl)
      print link
      match=re.compile('>Activity of:(.*?)</title>.*?http://gdata.youtube.com/feeds/api/users/(.*?).?/>').findall(link)
      print """""" + str ( match)
        
      for name ,user in match:
              addDir(name.strip(),user.strip(),9,'http://img-ipad.lisisoft.com/imgmic/1/2/1253-1-youtube-kids.jpg','1')
      setView('tvshows', 'default')
#list the links from  usernames based on mash23 + improvment
def YOUList(name,url,description):
        murl='http://gdata.youtube.com/feeds/api/users/'+url+'/uploads?&max-results=50&start-index='+description

        print "murl is :::::::::::::" + str (murl)
        link=OPEN_URL(murl)
        match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
        for nurl,desc,thumb,rname in match:
                rname=rname.replace('<','')
                YOULink(rname,nurl,thumb)
        description=int(description)+50
        addDir(' עוד תוצאות',url,9,'',str(description))

def YOULink(mname,url,thumb):
        ok=True
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url+"&hd=1"
        liz=xbmcgui.ListItem(mname, iconImage="DefaultVideo.png", thumbnailImage=thumb)
        liz.setInfo( type="Video", infoLabels={ "Title": mname, "Plot": description } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
 
        
#below tells plugin about the views                
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        Choose_series(url)
elif mode==2:
        series_land(url)
elif mode==3:
        play_episode(url)
elif mode==8:
           update_view(url)
elif mode==7:
           ListLive(url)
elif mode==9:
        YOUList(name,url,description)
elif mode==10:
        YOUsubs(url)
       
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
