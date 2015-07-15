from xml_utils import clean_tag
import gml

class B_Field(object):
    """general attribute object, fields are created for target collection"""

    GEOMETRY_TYPES = ("POINT","LINESTRING","POLYGON","MULTIPOLYGON")
    ALL_TYPES = GEOMETRY_TYPES + ("TEXT", "INTEGER", "REAL")


    def __init__(self, field_name, field_type, is_mandatory=True,
                 is_key_field=False, tag2object=()):
        """create field object

        name: is name used in target table or CSV header
        type: is type used in sql table, and used by sql_value to deliver
              correct value to insert in table.
        is_key_field: is key field that should contain a unique value
        tag_to_object: to convert geometry from GML to WKT, an xml element
                       is passed to GML-object which returns correct WKT-value
        value: holds the raw tekst value which can be used to create csv-files
               to create a value to store in SQL db use sql_value.
        """
        self.__name = field_name
        self.__type = None
        self.__is_mandatory = is_mandatory
        self.__is_key_field = is_key_field
        # set field type using object.. i.e. gml polygon -> wkt geometry
        self.__tag2object = tag2object
        self.__sql_template = None
        # set type using property set function, will also set __sql_template!
        self.type = field_type
        self.__value = None

    def _name(self):
        return self.__name

    name = property(fget=_name, doc="name is attribute name in database")

    def _type(self):
        return self.__type

    def _set_type(self, field_type):
        self.__type = field_type
        self._set_sql_template()

    type = property(fget=_type, fset=_set_type,
                    doc="type is one of database type")

    def _value(self):
        return self.__value

    def _set_value(self, value):
        self.__value = value

    value = property(fget=_value, fset=_set_value,
                    doc="value is the raw textvalue")
    
    def _is_key_field(self):
        return self.__is_key_field

    is_key_field = property(fget=_is_key_field,
                    doc="Is this a key field --> boolean")

    def _is_mandatory(self):
        return self.__is_mandatory

    is_mandatory = property(fget=_is_mandatory,
                    doc="Is this a mandatory field --> boolean")

    def _tag2object(self):
        return self.__tag2object

    tag2object = property(fget=_tag2object,
                          doc="tag2object is object that needs to be created \
to get value frome")

    def _set_sql_template(self):
        sql_template = "%s"
        if self.type == 'TEXT':
            sql_template = "'%s'"
        elif self.type in B_Field.GEOMETRY_TYPES:
            sql_template = "GeomFromText('%s', 28992)"
        self.__sql_template = sql_template        
        
    def set_value_from_xml(self, xml_element):
        """Convert contents of xml_element into field value."""
        if self.tag2object[0] == clean_tag(xml_element.tag):
            an_object = self.tag2object(1)
            self.value = an_object(xml_element).as_wkt()
        else:
            self.value = xml_element.text
            
    def sql_value(self):
        value = self.value
        if self.type == 'TEXT':
            value = value.replace("'", "''")
        return self.__sql_template % value
        
    def is_geometry(self):
        '''Depending on type returns true or false

        Purpose, for creation of datamodel from object.
        '''
        return self.type in B_Field.GEOMETRY_TYPES

    def sql_definition(self):
        """Returns definition for field in sql."""
        definition = self.name + " " + self.type
        if self.is_mandatory == True:
            definition += " NOT NULL"
        if self.is_key_field == True:
            definition += " PRIMARY KEY"
        return definition                        
     
class B_Object(object):
    """Parent class for all Basis Classes i.e. defined in bag.py."""

    def __init__(self, name):
        # attributes
        self.name = name
        self.fields = []
        self.tag2fields = {}
        # for caching variable
        self.tag = None
        self.tag2process = {}
        self.tag2field = {}

    def add_field(self, tag, field):
        self.fields.append(field)
        self.tag2field[tag] = field

    def process(self, xml_element):
        """Process an incoming xml_element describing a basis object
        """
        for i_elem in xml_element:
            self.tag = clean_tag(i_elem.tag)
            if self.tag2process.has_key(self.tag):
                a_process = self.tag2process[self.tag]
                a_process(i_elem)
            
    def _process_field(self, xml_element):
        """Convert contents of xml_element into field_value."""
        a_field = self.tag2field[self.tag]
        a_field.set_value_from_xml(xml_element)

    def geometry_field(self):
        """Returns the geometry field.
        """
        geometry_field = None
        for i_field in self.fields:
            if i_field.is_geometry():
                geometry_field = i_field
        return geometry_field

    def attribute_fields(self):
        attribute_fields = []
        for i_field in self.fields:
            if not i_field.is_geometry():
                attribute_fields.append(i_field)
        return attribute_fields

    def field_names(self):
        '''Gives a list of fieldnames.'''
        return [i_field.name for i_field in self.fields]

    def field_values(self):
        '''Gives a list of field values.'''
        return [i_field.value for i_field in self.fields]

    def field_types(self):
        '''Gives a list of field types.'''
        return [i_field.type for i_field in self.fields]

    def field_names_and_sql_values(self):
        '''Gives field names and field values to include in sql_statement
        for insert --> field_names, sql_values
        '''
        field_names = []
        sql_values = []
        for i_field in self.fields:
            field_names.append(i_field.name)
            field_names.append(i_field.sql_value())
        return names, sql_values            

    def csv_header(self):
        """Return the csv_header."""
        return ";".join(self.field_names())

    def as_csv(self):
        '''Returns CSV line to write a record for current object.'''
        return ";".join(self.field_values())

    def as_sql(self):
        '''Gives SQL insert statement to insert record for current object'''
        field_names, sql_values = self.field_names_and_sql_values()        
        sql = "INSERT INTO %s (" % self.name
        sql += ", ".join(field_names)
        sql += ") VALUES ("
        sql += ", ".join(sql_values)
        sql += ")"
        return sql

    def sql_create_table_statements(self):
        """Returns a list of SQL statements to create table
        with geometry fields and spatial index"""
        sql_statements = [self.sql_drop_table_statement(),
                          self.sql_create_table_statement()]
        if self.geometry_field() is not None:
            sql_statements.append(self.sql_add_geometry_statement())
            sql_statements.append(self.sql_create_index_statement())
        return sql_statements

    def sql_drop_table_statement(self):
        return "DROP TABLE if exists " + self.name

    def sql_create_table_statement(self):
        """Returns sql statement to create table in sql database."""
        sql = "CREATE TABLE %s (" % self.naam
        field_definitions = []
        for i_field in self.attribute_fields():
            field_definitions.append(i_field.sql_definition())
        sql += ",".join(field_definitions) + ")"
        return sql

    def sql_add_geometry_statement(self):
        """Returns sql statement to add a geometry column to sql table."""
        geom_field = self.geometry_field()
        sql = "SELECT AddGeometryColumn('%swoonplaats', " % self.naam
        sql += "'geometry', 28992, '%s', 'XY')" % geom_field.type
        return sql

    def sql_create_index_statement(self):
        """Returns sql statement to create spatial index."""
        return "SELECT CreateSpatialIndex('%s', 'geometry')" % self.naam
        
        

    
        
            
            
            
        
