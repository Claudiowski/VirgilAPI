


--
-- Name: article; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE article (
    id integer NOT NULL,
    title character varying,
    publication_date timestamp without time zone,
    url character varying,
    description character varying(1000),
    id_stream integer
);


ALTER TABLE article OWNER TO virgil;

--
-- Name: article_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE article_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE article_id_seq OWNER TO virgil;

--
-- Name: article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE article_id_seq OWNED BY article.id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE category (
    id integer NOT NULL,
    name character varying,
    id_theme integer
);


ALTER TABLE category OWNER TO virgil;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_id_seq OWNER TO virgil;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE category_id_seq OWNED BY category.id;


--
-- Name: favorite; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE favorite (
    id integer NOT NULL,
    annotation character varying(511),
    url character varying,
    title character varying,
    description character varying(1000),
    publication_date timestamp without time zone,
    id_stream integer
);


ALTER TABLE favorite OWNER TO virgil;

--
-- Name: favorite_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE favorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE favorite_id_seq OWNER TO virgil;

--
-- Name: favorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE favorite_id_seq OWNED BY favorite.id;


--
-- Name: reader; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE reader (
    id integer NOT NULL,
    pseudo character varying,
    password character varying,
    secret character varying
);


ALTER TABLE reader OWNER TO virgil;

--
-- Name: reader_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE reader_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE reader_id_seq OWNER TO virgil;

--
-- Name: reader_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE reader_id_seq OWNED BY reader.id;


--
-- Name: stream; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE stream (
    id integer NOT NULL,
    url character varying,
    name character varying,
    id_category integer
);


ALTER TABLE stream OWNER TO virgil;

--
-- Name: stream_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE stream_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE stream_id_seq OWNER TO virgil;

--
-- Name: stream_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE stream_id_seq OWNED BY stream.id;


--
-- Name: theme; Type: TABLE; Schema: public; Owner: virgil
--

CREATE TABLE theme (
    id integer NOT NULL,
    name character varying,
    id_reader integer
);


ALTER TABLE theme OWNER TO virgil;

--
-- Name: theme_id_seq; Type: SEQUENCE; Schema: public; Owner: virgil
--

CREATE SEQUENCE theme_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE theme_id_seq OWNER TO virgil;

--
-- Name: theme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: virgil
--

ALTER SEQUENCE theme_id_seq OWNED BY theme.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY article ALTER COLUMN id SET DEFAULT nextval('article_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY category ALTER COLUMN id SET DEFAULT nextval('category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY favorite ALTER COLUMN id SET DEFAULT nextval('favorite_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY reader ALTER COLUMN id SET DEFAULT nextval('reader_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY stream ALTER COLUMN id SET DEFAULT nextval('stream_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY theme ALTER COLUMN id SET DEFAULT nextval('theme_id_seq'::regclass);



--
-- Name: article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('article_id_seq', 112094, true);



--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('category_id_seq', 4, true);


--
-- Name: favorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('favorite_id_seq', 20, true);



--
-- Name: reader_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('reader_id_seq', 1, true);




--
-- Name: stream_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('stream_id_seq', 13, true);




--
-- Name: theme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('theme_id_seq', 3, true);


--
-- Name: article_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY article
    ADD CONSTRAINT article_pkey PRIMARY KEY (id);


--
-- Name: category_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: favorite_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY favorite
    ADD CONSTRAINT favorite_pkey PRIMARY KEY (id);


--
-- Name: reader_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY reader
    ADD CONSTRAINT reader_pkey PRIMARY KEY (id);


--
-- Name: stream_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY stream
    ADD CONSTRAINT stream_pkey PRIMARY KEY (id);


--
-- Name: theme_pkey; Type: CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY theme
    ADD CONSTRAINT theme_pkey PRIMARY KEY (id);


--
-- Name: article_id_stream_fkey; Type: FK CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY article
    ADD CONSTRAINT article_id_stream_fkey FOREIGN KEY (id_stream) REFERENCES stream(id);


--
-- Name: category_id_theme_fkey; Type: FK CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_id_theme_fkey FOREIGN KEY (id_theme) REFERENCES theme(id);


--
-- Name: favorite_id_stream_fkey; Type: FK CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY favorite
    ADD CONSTRAINT favorite_id_stream_fkey FOREIGN KEY (id_stream) REFERENCES stream(id);


--
-- Name: stream_id_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY stream
    ADD CONSTRAINT stream_id_category_fkey FOREIGN KEY (id_category) REFERENCES category(id);


--
-- Name: theme_id_reader_fkey; Type: FK CONSTRAINT; Schema: public; Owner: virgil
--

ALTER TABLE ONLY theme
    ADD CONSTRAINT theme_id_reader_fkey FOREIGN KEY (id_reader) REFERENCES reader(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

