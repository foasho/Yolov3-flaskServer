import xml.etree.ElementTree as ET
from os import getcwd
import sys

basepath = getcwd().replace("\\", "/")
voc_class_path = basepath + '/model_data/voc_classes.txt'

if len(sys.argv) > 1:
    classes = sys.argv[1:]

with open(voc_class_path, 'w') as f:
    f.write('\n'.join(classes))