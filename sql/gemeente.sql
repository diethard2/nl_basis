DROP TABLE if exists gemeente;
--
CREATE TABLE gemeente 
    (gemeentecode TEXT NOT NULL,
     naam TEXT NOT NULL);
--
CREATE INDEX i_gemeentecode ON woonplaats_gemeente (id_gemeente, id_woonplaats);
