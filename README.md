# archicad-classification-xml-parser

Main purpose of this script is extract the data from Archicad22 property and classification setting xml file.

# Target

Archicad 22

#  Not support

Culuculation field

# Extraction list

1. Property list

Columns : "group", "name", "discription", "data type", "defaultvalue", "opts"

2. Classification list 

Columns : "Level 1", "Level 2", "Level 3", "Level 4", "Merged"

3. Classification property mapping (kind of intermidiate table)

Columns : "classification", "property"

# xml xpath reference

```
# property

# group
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/Name
# name
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Name
# discription
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Description
# datatype
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/ValueType
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/ValueType
# default value
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/DefaultValue/Variant/Value
# key of default value in OptionSet
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Key\[\d*\]
# option set
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ValueDescriptor/EnumerationValueDescriptorWithStoredValues/Values/Value\[\d*\]/Variant/Value

# classification

# /BuildingInformation/Classification/System/Items/Item\[\d*\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID
# /BuildingInformation/Classification/System/Items/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/Children/Item\[\d*\]/ID

# mapping

# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/ClassificationIDs/ClassificationID/ItemID
# /BuildingInformation/PropertyDefinitionGroups/PropertyDefinitionGroup\[\d*\]/PropertyDefinitions/PropertyDefinition\[\d*\]/Name

```
