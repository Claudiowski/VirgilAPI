-- Table: reader

-- DROP TABLE reader;

CREATE TABLE reader
(
  id serial NOT NULL,
  pseudo character varying(255) NOT NULL,
  password character varying(255) NOT NULL,
  secret character varying(255),
  is_admin boolean NOT NULL,
  CONSTRAINT prk_constraint_reader PRIMARY KEY (id),
  CONSTRAINT reader_pseudo_key UNIQUE (pseudo)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE reader
  OWNER TO virgil;


-- Table: theme

-- DROP TABLE theme;

CREATE TABLE theme
(
  id serial NOT NULL,
  name character varying(255) NOT NULL,
  id_reader integer NOT NULL,
  CONSTRAINT prk_constraint_theme PRIMARY KEY (id),
  CONSTRAINT fk_theme_id_reader FOREIGN KEY (id_reader)
      REFERENCES reader (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT theme_name_id_reader_key UNIQUE (name, id_reader)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE theme
  OWNER TO virgil;


-- Table: category

-- DROP TABLE category;

CREATE TABLE category
(
  name character varying(255) NOT NULL,
  id serial NOT NULL,
  id_theme integer NOT NULL,
  CONSTRAINT prk_constraint_category PRIMARY KEY (id),
  CONSTRAINT fk_category_id_theme FOREIGN KEY (id_theme)
      REFERENCES theme (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT category_name_id_theme_key UNIQUE (name, id_theme)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE category
  OWNER TO virgil;


-- Table: stream

-- DROP TABLE stream;

CREATE TABLE stream
(
  url character varying(255) NOT NULL,
  name character varying(255) NOT NULL,
  id serial NOT NULL,
  id_category integer NOT NULL,
  CONSTRAINT prk_constraint_stream PRIMARY KEY (id),
  CONSTRAINT fk_stream_id_category FOREIGN KEY (id_category)
      REFERENCES category (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT stream_name_id_category_key UNIQUE (name, id_category),
  CONSTRAINT stream_url_id_category_key UNIQUE (url, id_category)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE stream
  OWNER TO virgil;


-- Table: favorite

-- DROP TABLE favorite;

CREATE TABLE favorite
(
  url character varying(255) NOT NULL,
  annotation character varying(2000),
  id serial NOT NULL,
  id_stream integer,
  title varchar(255) NOT NULL,
  description TEXT NOT NULL,
  date_hour DATE NOT NULL,
  CONSTRAINT prk_constraint_favorites PRIMARY KEY (id),
  CONSTRAINT fk_favorites_id_stream FOREIGN KEY (id_stream)
      REFERENCES stream (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT favorites_url_id_stream_key UNIQUE (url, id_stream)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE favorite
  OWNER TO virgil;

INSERT INTO reader(pseudo, password, is_admin)
VALUES ('reader', 'passwd', 'true');



