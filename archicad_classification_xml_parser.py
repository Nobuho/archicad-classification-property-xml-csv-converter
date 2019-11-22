from lxml import etree
import csv
from glob import glob
import codecs
import re, collections
from collections import Counter


tree = etree.parse("archicad_classification_xml/archicad_classification_xml.xml")
root = tree.getroot().tag
base_path = tree.xpath("/BuildingInformation/Classification/System/Items/Item/Children/Item/ID/chomechome")

if len(p) == 0:
    print("none!")


for elem in base_path:
    tree.getpath(elem)        



# /BuildingInformation/Classification/System/Items/Item[1]/ID
# /BuildingInformation/Classification/System/Items/Item[1]/Children/Item[1]/ID
# /BuildingInformation/Classification/System/Items/Item[1]/Children/Item[3]/Children/Item[1]/ID