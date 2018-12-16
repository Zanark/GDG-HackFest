import xml.etree.ElementTree as ET
import yaml, re
import json

def parse_text_boxes(textboxes, pages):
    for page in pages:
        for textbox in page:
            if textbox.tag == "textbox":
                string = ""
                for textline in textbox:
                    for text in textline:
                        string += text.text
                    string += " "
                string.strip()
                string = re.sub('\\n', '', string)
                textboxes.append(string)

def read_text_box(textboxes, yml):
    data = {}
    for item in yml:
        lst = yml[item]
        for dct in lst:
            for (key, value) in dct.items():
                if (key == 'id'):
                    data[item] = textboxes[value]
    return data

def get_json(template_path, xml_file):
    textboxes = []
    data = (open(template_path)).read()
    yml = yaml.load(data)

    tree = ET.parse(xml_file)
    parse_text_boxes(textboxes, tree.getroot())

    data = read_text_box(textboxes, yml)
    json_val = json.dumps(data)

    return data