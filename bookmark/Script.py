from models import Bookmark,Url,Title,Description,Tag,Private

def savebookmark(TitleF,UrlF,DescriptionF,TagF,PrivateF):

    try :
        UrlB = Url.objects.get(url=UrlF)
    except :
        UrlB = Url(url=UrlF)
    UrlB.save()

    try :
        TitleB = Title.objects.get(title=TitleF)
    except :
        TitleB = Title(title=TitleF)
    TitleB.save();
    try :
        DescriptionB = Description.objects.get(description=DescriptionF)
    except :
        DescriptionB = Description(description=DescriptionF)
    DescriptionB.save()
    try :
        PrivateB = Private.objects.get(private= (PrivateF == 'True'))
    except :
        PrivateB = Private(private= (PrivateF == 'True'))
    PrivateB.save()
    try :
        b2 = Bookmark.objects.get(url=UrlB)
        b2.title=TitleB
        b2.description=DescriptionB
        b2.private=PrivateB
    except :
        b2 = Bookmark(title=TitleB,url=UrlB,description=DescriptionB,private=PrivateB)
    b2.save()

    tags = TagF.split(" ")
    for t in tags :
        try :
            TagB = Tag.objects.get(tag=t)
        except :
            TagB= Tag(tag=t)
        TagB.save()
        b2.tag.add(TagB)
    b2.save()
        

def getbookmark(Url):
    tag = ""
    q = Bookmark.objects.filter(url__url__contains=Url)
    if q :
        print "q"
        print q
        tags = q[0].tag.all()
        for t in tags :
            tag += t.tag + " "
        tag =  tag[0:-1]
    return tag