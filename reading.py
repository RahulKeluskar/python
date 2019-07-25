from xml.dom import minidom

mydoc = minidom.parse("data.xml")
items = mydoc.getElementsByTagName('item')

for elem in items:
	print(elem.attributes['name'].value,"\t\t",elem.firstChild.data)