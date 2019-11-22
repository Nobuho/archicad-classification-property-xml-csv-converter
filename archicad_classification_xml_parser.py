from lxml import etree
import csv
import codecs
import re


tree = etree.parse("archicad_classification_xml/archicad_classification_xml.xml")

# ##################################################
# making classification list
# ##################################################

classification_list = []

search_xpath1 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/ID"
search_xpath2 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/ID"
search_xpath3 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"
search_xpath4 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"
search_xpath5 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"

for tag in tree.iter():

    path = tree.getpath(tag)
    text = tree.xpath(path)[0].text

    if re.match(search_xpath1, path):
        cls1 = text
        classification_list.append([cls1, cls1, cls1, cls1, cls1])

    elif re.match(search_xpath2, path):
        cls2 = text
        classification_list.append([cls1, cls2, cls2, cls2, cls2])

    elif re.match(search_xpath3, path):
        cls3 = text
        classification_list.append([cls1, cls2, cls3, cls3, cls3])

    elif re.match(search_xpath4, path):
        cls4 = text
        classification_list.append([cls1, cls2, cls3, cls4, cls4])

    elif re.match(search_xpath5, path):
        cls5 = test
        classification_list.append([cls1, cls2, cls3, cls4, cls5])
        
with codecs.open('classification.csv', 'w', 'cp932', 'ignore') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(classification_list)

# ##################################################
# making classification property mapping list
# ##################################################

mapping_list = []

search_xpath_property = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Name"
search_xpath_classification = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup.*ItemID"

for tag in tree.iter():

    path = tree.getpath(tag)
    text = tree.xpath(path)[0].text

    if re.match(search_xpath_property, path):
        classification = text

    elif re.match(search_xpath_classification, path):
        mapping_list.append([classification, text])
        
with codecs.open('classification_property_mapping.csv', 'w', 'cp932', 'ignore') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(mapping_list)


# /BuildingInformation/Classification/System/Items/Item\[\d\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID

# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup[7]/PropertyDefinitions/PropertyDefinition[4]/ClassificationIDs/ClassificationID/ItemID
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup[7]/PropertyDefinitions/PropertyDefinition[2]/Name

# search_xpath = r"/BuildingInformation/Classification/System/Items/Item.*"
# search_tag = r".*ID"

# for tag in tree.iter():
#     path = tree.getpath(tag)
#     if re.match(search_xpath, path) and re.match(search_tag, path):
#         level = path.count("Children")
#         print(","*level,tree.xpath(path)[0].text)