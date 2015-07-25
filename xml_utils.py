def clean_tag(tag):
    """Remove namespace from tag"""
    if '}' in tag:
        index = tag.rindex('}')
        tag = tag[index+1:]
    return tag
        
def find_xml_with_tag(xml_element, search_tag, found_elem):
    """Find in xml_element the element with given search_tag --> xml_element"""
    if found_elem is not None:
        return found_elem
    for i_elem in xml_element:
        # print i_elem.tag
        tag = clean_tag(i_elem.tag)
        # print tag
        if search_tag == tag:
            found_elem = i_elem
            break
        else:
            # search deeper in xml-tree
            found_elem = find_xml_with_tag(i_elem, search_tag, found_elem)
    return found_elem

class B_XmlProcessor(object):
    """superclass for all objects that need to process and interprete xml"""
    def __init__(self):
        self.__tag2process = {}

    def _tag2process(self):
        return self.__tag2process

    tag2process = property(fget=_tag2process, doc="tag2process is a dictionary, \
the key is the tag from xml the value the process method")

    def add_tag_method_to_process(self, a_tag, a_method):
        self.__tag2process[a_tag] = a_method

    def process(self, xml_element):
        """Process an incoming xml_element
        """
        for i_elem in xml_element:
            self.tag = clean_tag(i_elem.tag)
            if self.tag2process.has_key(self.tag):
                a_process = self.tag2process[self.tag]
                a_process(i_elem)
            
