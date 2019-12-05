from lxml import etree
import csv
import codecs
import re


xml_filepath = "archicad_xml/archicad_classification_property.xml"
tree = etree.parse(xml_filepath)

# ##################################################
# making property list
# ##################################################

# This csv is just mapping list between classification and property.
# You need to combine these two list based on this mapping table.

property_list = [["group", "name", "discription", "data type", "defaultvalue", "opt1", "opt2", "opt3", "opt4", "opt5", "opt6", "opt7", "opt8", "opt9", "opt10", "opt11"]]
tmp = []
optset_dict = {}

xpath_property_group = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/Name"
xpath_property_name = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Name"
xpath_property_discription = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Description"
xpath_property_type1 = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/ValueType"
xpath_property_type2 = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/ValueType"
xpath_property_default = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/DefaultValue/Variant/Value"
xpath_property_optset = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Value\[\d+?\]/Variant/Value"
xpath_property_optset_key = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Key\[\d*\]"

for tag in tree.iter():
    path = tree.getpath(tag)
    text = tree.xpath(path)[0].text
    if text is None:
        text = "none"
    if re.match(xpath_property_group, path):
        property_group = text
    if re.match(xpath_property_name, path):
        property_list.append(tmp)
        tmp = []
        property_name = text
        tmp.extend([property_group, property_name])
    elif re.match(xpath_property_discription, path):
        property_discription = text
        tmp.append(property_discription)
    elif re.match(xpath_property_type1, path) or re.match(xpath_property_type2, path):
        if text == "3":
            text = "OptionSet"
        property_type = text
        tmp.append(property_type)
    elif re.match(xpath_property_default, path):
        if re.match("........-....-....-....-............", text):
            # If type is optset it's needed to add special default value based on the optset key
            tmp.insert(4, optset_dict[text])
            continue
        property_default = text
        tmp.append(property_default)
    elif re.match(xpath_property_optset_key, path):
        property_optset_key = text
    elif re.match(xpath_property_optset, path):
        property_optset = text
        optset_dict[property_optset_key] = property_optset
        tmp.append(property_optset)

property_list.pop(1)
property_list.append(tmp)

with codecs.open('property.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(property_list)

# ##################################################
# making classification list
# ##################################################

# The level is limitted under 4th. Meybe it will not be deeper than that...

classification_list = [["Level 1", "Level 2", "Level 3", "Level 4", "Merged"]]

xpath1 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/ID"
xpath2 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/ID"
xpath3 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"
xpath4 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"
xpath5 = r"/BuildingInformation/Classification/System/Items/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/Children/Item\[\d\]/ID"

for tag in tree.iter():
    path = tree.getpath(tag)
    text = tree.xpath(path)[0].text
    if re.match(xpath1, path):
        cls1 = text
        classification_list.append([cls1, "", "", "", cls1])
    elif re.match(xpath2, path):
        cls2 = text
        classification_list.append([cls1, cls2, "", "", cls2])
    elif re.match(xpath3, path):
        cls3 = text
        classification_list.append([cls1, cls2, cls3, "", cls3])
    elif re.match(xpath4, path):
        cls4 = text
        classification_list.append([cls1, cls2, cls3, cls4, cls4])
        
with codecs.open('classification.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(classification_list)

# ##################################################
# making classification property mapping list
# ##################################################

# This csv is just mapping list between classification and property.
# You need to combine these two list based on this mapping table.

mapping_list = [["property", "classification"]]

xpath_property_name = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Name"
xpath_classification = r"/BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup.*ItemID"

for tag in tree.iter():
    path = tree.getpath(tag)
    text = tree.xpath(path)[0].text
    if re.match(xpath_property_name, path):
        classification = text
    elif re.match(xpath_classification, path):
        mapping_list.append([classification, text])
with codecs.open('classification_property_mapping.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(mapping_list)
