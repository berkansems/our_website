from django import template
register = template.Library()

@register.simple_tag()
def getAllTypes(obj):
    list=str(obj).split(', ')
    result = ""
    for i in list:
        result += (i + " ")
    return result


@register.simple_tag(takes_context=True)
def getCoverPhoto(context,images):
    print(len(images))
    try:
        covers = images.objects.filter(status=True)
        print('2')
        if len(covers)>1:
            cover = covers[0]
            print('3')
        else:
            cover = covers
            print('4')
    except:
        print('5')
        try:
            cover = images.objects.first()
        except:
            return ''
    return cover

