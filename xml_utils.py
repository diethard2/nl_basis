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

