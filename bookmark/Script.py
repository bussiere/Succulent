from models import Bookmark,Url,Title,Description,Tag,Private

def savebookmark(TitleF,UrlF,DescriptionF,TagF,PrivateF):
    UrlB = Url.objects.filter(url=Url)

    UrlB = Url(url=UrlF)
    UrlB.save()
    print UrlB
    q = Bookmark.objects.filter(url__url__contains=UrlB)
    print q
    TitleB = Title(title=TitleF)
    TitleB.save();
    DescriptionB = Description(description=DescriptionF)
    DescriptionB.save()
    print PrivateF
    PrivateB = Private(private= (PrivateF == 'True'))
    PrivateB.save()
    
    b2 = Bookmark(title=TitleB,url=UrlB,description=DescriptionB,private=PrivateB)
    b2.save()

    tags = TagF.split(" ")
    for t in tags :
        TagB= Tag(tag=t)
        TagB.save()
        b2.tag.add(TagB)
        b2.save()
        

def getbookmark(Url):
    q = Bookmark.objects.filter(url__url__contains=Url)