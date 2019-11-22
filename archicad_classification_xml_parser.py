from lxml import etree
import csv
from glob import glob
import codecs
import re
from collections import Counter


tree = etree.parse("archicad_classification_xml/archicad_classification_xml.xml")
root = tree.getroot().tag
base_path = tree.xpath("/BuildingInformation/Classification/System/Items/Item")

# if len(p) == 0:
    # print("none!")

search_xpath = r"/BuildingInformation/Classification/System/Items/Item.*"
search_tag = r".*ID"

for tag in tree.iter():
    path = tree.getpath(tag)
    if re.match(search_xpath, path) and re.match(search_tag, path):
        level = path.count("Children")
        print(","*level,tree.xpath(path)[0].text)



# for elem in base_path:
#     path = tree.getpath(elem)
#     elem_name = tree.xpath(path + "/ID")[0].text
#     print(elem_name)
#     while True:
#         child_path = path + "/Children/Item"
#         child_elem = tree.xpath(child_path + "/ID")
#         if len(child_elem) == 0:
#             break
#         else:
#             child_elem_name = tree.xpath(child_path + "/ID")[0].text
#             print(elem_name)
#             path = path + "/Children/Item"



# /BuildingInformation/Classification/System/Items/Item[1]/ID
# /BuildingInformation/Classification/System/Items/Item[1]/Children/Item[1]/ID
# /BuildingInformation/Classification/System/Items/Item[1]/Children/Item[3]/Children/Item[1]/ID