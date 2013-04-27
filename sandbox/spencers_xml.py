
from xml.etree.ElementTree import Element, SubElement, Comment,  tostring



#http://pymotw.com/2/xml/etree/ElementTree/create.html


# I need to make xml that looks like this
# <items>
#   <item uid="rdioartist" arg="r96664" valid="yes" autocomplete="Incubus">
#     <title>Incubus</title>
#     <subtitle>Artist</subtitle>
#     <icon>rdio-artist.png</icon>
#   </item>

meaningOfLife = 42

items = Element('items')

#comment = Comment('Generated by Spencer')
#items.append(comment)

item = SubElement(items, 'item')
item.set('uid', 'mtgoxprice')
item.set('arg', str(meaningOfLife))
item.set('valid', 'yes')


title = SubElement(item, 'title')
title.text = "Incubus"

subtitle = SubElement(item, 'subtitle')
subtitle.text = "Artist"

icon = SubElement(item, 'icon')
icon.text = "rdio-artist.png"

# child_with_tail = SubElement(items, "This child has a tail")
# child_with_tail.text = "This child has regular text"
# child_with_tail.tail = "And here is the tail"







from xml.etree import ElementTree
from xml.dom import minidom
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")





print tostring(items)

