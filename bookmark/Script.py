from models import Bookmark,Url

def savebookmark(TitleF,UrlF,DescriptionF,TagF,PrivateF):
    UrlB = Url.objects.filter(url=Url)
    print UrlB
    UrlB = Url(url=UrlF)
    UrlB.save()
    q = Bookmark.objects.filter(url=UrlB)
    print q
    b2 = Bookmark(title=Titleb,url=Urlb,description=Description,tag=Tag,private=Private)
    b2.save()

def getbookmark(Url):
    pass