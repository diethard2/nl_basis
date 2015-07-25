from xml_utils import clean_tag
from basis import B_XmlProcessor

def wkt_coords_from_gml(gml_coords):
    wkt_coords = ""
    count = 0
    values = gml_coords.split(' ')
    for value in values:
        count += 1
        if count % 2 == 1:
            wkt_coords += value + ' '
        else:
            wkt_coords += value + ', '
    return wkt_coords[:-2]

            
class MultiPolygon(B_XmlProcessor):
    
    def __init__(self):
        B_XmlProcessor.__init__(self)
        self.polygons = []
        self._add_tags_to_process()

    def _add_tags_to_process(self):
        for i_tag in ("MultiSurface", "surfaceMember"):
            self.add_tag_method_to_process(i_tag, self.process)
        self.add_tag_method_to_process("Polygon", self._process_Polygon)

    def _process_Polygon(self, elem):
        a_polygon = Polygon()
        a_polygon.process(elem)
        self.polygons.append(a_polygon)

    def as_wkt(self):
        wkt = "MultiPolygon("
        count_polygon = 0
        for a_polygon in self.polygons:
            count_polygon += 1
            if count_polygon > 1:
                wkt += ","
            wkt += a_polygon.wkt_rings()
        wkt += ")"
        return wkt
        

class Polygon:
    
    def __init__(self):
        self.exterior_ring = ""
        self.interior_rings = []

    def process(self, elem):
        tag = clean_tag(elem.tag)
        if tag == "Polygon":
            # called from MultiPolygon, the incoming element is an xml
            # polygon item.
            self._process_polygon(elem)
        else:
            # called directly, incoming element is an xml geometry item
            for i_elem in elem:
                tag = clean_tag(i_elem.tag)
                if tag == "Polygon":
                    self._process_polygon(i_elem)
                
    def _process_polygon(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "exterior":
                    self._process_exterior(i_elem)
            elif tag == "interior":
                    self._process_interior(i_elem)

    def _process_exterior(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "LinearRing":
                self._process_LinearRing(i_elem, exterior=True)
                
    def _process_interior(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "LinearRing":
                self._process_LinearRing(i_elem, exterior=False)
                
    def _process_LinearRing(self, elem, exterior):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "posList":
                if exterior == True:
                    coords_text = self._text_poslist(i_elem)
                    self.exterior_ring = coords_text
                else:
                    coords_text = self._text_poslist(i_elem)
                    self.interior_rings.append(coords_text)
                    
    def _text_poslist(self, elem):
        if self._is_poslist_3d(elem):
            return self._2d_from_3d_poslist(elem.text)
        else:
            return elem.text
            
    def _is_poslist_3d(self, elem):
        is_3d = False
        xml_attributes = elem.attrib
        if xml_attributes.has_key('srsDimension'):
            if xml_attributes['srsDimension'] == '3':
                is_3d = True
        return is_3d
       
    def _2d_from_3d_poslist(self, text):
        xyz = text.split(' ')
        xy = []
        l_count = 0
        for i_coord in xyz:
            l_count += 1
            if l_count % 3 > 0:
                xy.append(i_coord)
        return ' '.join(xy)

    def as_wkt(self):
        """Return valid geom in WKT notation for polygon"""
        wkt = "Polygon" + self.wkt_rings()
        return wkt

    def wkt_rings(self):
        """Return only the external en internal rings in WKT \
        notation for polygon"""
        wkt = "((" + wkt_coords_from_gml(self.exterior_ring) + ")"
        for int_ring in self.interior_rings:
            wkt += ",(" + wkt_coords_from_gml(int_ring) + ")"
        wkt += ")"
        return wkt
