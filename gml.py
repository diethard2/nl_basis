from xml_utils import clean_tag

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

            
class MultiPolygon:
    
    def __init__(self, elem):
        self.polygons = []
        self._process(elem)

    def _process(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "MultiSurface":
                self._process_MultiSurface(i_elem)
            if tag == "Polygon":
                self.polygons.append(Polygon(i_elem))
                
    def _process_MultiSurface(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "surfaceMember":
                self._process_surfaceMember(i_elem)

    def _process_surfaceMember(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "Polygon":
                a_polygon = Polygon(i_elem)
                self.polygons.append(a_polygon)

    def as_wkt(self):
        wkt = "MultiPolygon("
        for a_polygon in self.polygons:
            wkt += a_polygon.wkt_rings()
        wkt += ")"
        return wkt
        

class Polygon:
    
    def __init__(self, elem):
        self.exterior_ring = ""
        self.interior_rings = []
        self._process(elem)

    def _process(self, elem):
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
                    self.exterior_ring = i_elem.text
                else:
                    self.interior_rings.append(i_elem.text)

    def as_wkt(self):
        """Return valid geom in WKT notation for polygon"""
        wkt = "Polygon" + self.wkt_rings()
        return wkt

    def wkt_rings(self):
        """Return only the external en internal rings in WKT \
        notation for polygon"""
        wkt = "((" + wkt_coords_from_gml(self.exterior_ring) + ")"
        for int_ring in self.interior_rings:
            wkt += "(" + wkt_coords_from_gml(int_ring) + ")"
        wkt += ")"
        return wkt
