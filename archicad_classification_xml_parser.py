from lxml import etree
import csv
import codecs
import re


xml_filepath = "archicad_xml/ArchiCAD23テンプレート_1_プロパティ.xml"

tree = etree.parse(xml_filepath)
root = tree.getroot()

# ##################################################
# making property list
# ##################################################

# This csv is just mapping list between classification and property.
# You need to combine these two list based on this mapping table.

property_list = [["group", "name", "discription", "data type", "defaultvalue", "opt1", "opt2", "opt3", "opt4", "opt5", "opt6", "opt7", "opt8", "opt9", "opt10", "opt11"]]

pg = [i for i in root.iterfind('PropertyDefinitionGroups/PropertyDefinitionGroup')]

for n in pg:
    pg_name = n.find("Name").text
    pg_p = n.findall("PropertyDefinitions/PropertyDefinition")
    p_list = []

    for i in pg_p:
        p = []
        pg_p_opts_val = []
        pg_p_name = i.find("Name").text 
        pg_p_des = i.find("Description").text

        if i.find("ValueDescriptor/EnumerationValueDescriptorWithStoredValues/ValueType") != None:
            pg_p_typ = "Optset"
            pg_p_opts_key = [n.text for n in i.findall("ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Key")]
            pg_p_opts_val = [n.text for n in i.findall("ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Value/Variant/Value")]
            pg_p_opts_dict = {key: value for key, value in zip(pg_p_opts_key, pg_p_opts_val)}
            pg_p_def_key = i.find("DefaultValue/Variant/Value").text
            pg_p_def = pg_p_opts_dict[pg_p_def_key]
            
        elif i.find("DefaultValue/DefaultValueType") != None:
            if i.find("DefaultValue/DefaultValueType").text == "Expression":
                pg_p_typ = "Expression"
                pg_p_def = i.find("DefaultValue/ExpressionDefaultValue/Expression").text
            else:
                pg_p_typ = i.find("ValueDescriptor/ValueType").text
                pg_p_def = i.find("DefaultValue/Variant/Value").text

        p += [pg_name, pg_p_name, pg_p_des, pg_p_typ, pg_p_def]
        p += pg_p_opts_val

        property_list.append(p)

with codecs.open('Property.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(property_list)

# ##################################################
# making classification list
# ##################################################

# The level is limitted under 4th. Meybe it will not be deeper than that...

classification_list = [["Level 1", "Level 2", "Level 3", "Level 4", "Merged"]]

xpath1 = r"/BuildingInformation/Classification/System/Items/Item\[\d*\]/ID"
xpath2 = r"/BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/ID"
xpath3 = r"/BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID"
xpath4 = r"/BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID"
xpath5 = r"/BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID"

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
