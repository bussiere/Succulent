from models import Bookmark,Url,Title,Description,Tag,Private

def savebookmark(TitleF,UrlF,DescriptionF,TagF,PrivateF):
    UrlB = Url.objects.filter(url=Url)
    print UrlB
    UrlB = Url(url=UrlF)
    UrlB.save()
    q = Bookmark.objects.filter(url=UrlB)
    print q
    TitleB = Title(title=TitleF)
    TitleB.save();
    DescriptionB = Description(description=DescriptionF)
    DescriptionB.save()
    TagB= Tag(tag=TagF)
    TagB.save()
    PrivateB = Private(private=PrivateF)
    PrivateB.save()
    
    b2 = Bookmark(title=TitleB,url=UrlB,description=DescriptionB,tag=TagB,private=PrivateB)
    b2.save()

def getbookmark(Url):
    pass