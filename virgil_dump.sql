--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

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
-- Data for Name: article; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY article (id, title, publication_date, url, description, id_stream) FROM stdin;
112085	Des failles majeures confirmées pour les plateformes Ryzen et Epyc d'AMD	2018-03-19 14:08:42	https://www.lemondeinformatique.fr/actualites/lire-des-failles-majeures-confirmees-pour-les-plateformes-ryzen-et-epyc-d-amd-71196.html	Les chercheurs de l’entreprise de sécurité israélienne CTS-Labs disent avoir découvert de sérieuses vulnérabilités (...)	10
112086	Répondre à la gestion des secrets en environnement DevOps	2018-03-19 11:16:51	https://www.lemondeinformatique.fr/actualites/lire-repondre-a-la-gestion-des-secrets-en-environnement-devops-71187.html	De prime abord, cela peut paraître impressionnant quand on pense à l’innombrable quantité d’utilisateurs non-humains à (...)	10
112087	Un hack de SAP CRM détaillé par ERPScan	2018-03-19 08:56:31	https://www.lemondeinformatique.fr/actualites/lire-un-hack-de-sap-crm-detaille-par-erpscan-71189.html	Le 13 février 2018, SAP a publié deux bulletins de sécurité (2547431 et 2565622) afin de corriger des vulnérabilités (...)	10
112088	L'avion hyper connecté : comment prévoir une sécurité maximale ?	2018-03-16 15:56:39	https://www.lemondeinformatique.fr/actualites/lire-l-avion-hyper-connecte-comment-prevoir-une-securite-maximale-71186.html	Jusqu’à aujourd’hui, les commandes mécaniques, les communications radios avec le sol et l’analogique étaient les (...)	10
112089	Linkedin revoit ses conditions d'utilisation et sa politique de confidentialité	2018-03-16 15:55:36	https://www.lemondeinformatique.fr/actualites/lire-linkedin-revoit-ses-conditions-d-utilisation-et-sa-politique-de-confidentialite-71184.html	« Nous mettons à jour nos conditions générales d’utilisation et souhaitons vous donner un aperçu de certaines des (...)	10
112090	Microsoft donne 250 000 $ aux découvreurs de failles semblables à Meltdown et Spectre	2018-03-16 11:51:29	https://www.lemondeinformatique.fr/actualites/lire-microsoft-donne-250-000-$-aux-decouvreurs-de-failles-semblables-a-meltdown-et-spectre-71179.html	Microsoft a été très actif depuis la découverte le 3 janvier dernier des vulnérabilités Meltdown et Spectre. (...)	10
112091	Les prochaines puces Xeon Cascade Lake d'Intel immunisées contre Spectre et Meltdown	2018-03-15 17:54:53	https://www.lemondeinformatique.fr/actualites/lire-les-prochaines-puces-xeon-cascade-lake-d-intel-immunisees-contre-spectre-et-meltdown-71172.html	Intel monte d'un cran sa stratégie de lutte contre Meltdown/Spectre. La société prévoit en effet de partitionner ses processeurs (...)	10
112092	Hub One lance une offre de conseil en cybersécurité	2018-03-15 15:04:01	https://www.lemondeinformatique.fr/actualites/lire-hub-one-lance-une-offre-de-conseil-en-cybersecurite-71168.html	Des services réseaux et télécoms à la cybersécurité il n'y a qu'un pas qu'Hub One a franchi. La filiale d'Aéroports (...)	10
112093	Microsoft corrige 75 vulnérabilités en mars	2018-03-15 12:19:48	https://www.lemondeinformatique.fr/actualites/lire-microsoft-corrige-75-vulnerabilites-en-mars-71164.html	Mardi, Microsoft a annoncé des correctifs de sécurité pour réparer 75 vulnérabilités dans plusieurs (...)	10
112094	McAfee dégaine une offre de sécurité pour Microsoft Azure	2018-03-14 13:01:27	https://www.lemondeinformatique.fr/actualites/lire-mcafee-degaine-une-offre-de-securite-pour-microsoft-azure-71155.html	McAfee a annoncé que sa plate-forme de sécurité cloud permet maintenant de protéger en permanence Microsoft Azure. « Le (...)	10
\.


--
-- Name: article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('article_id_seq', 112094, true);


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY category (id, name, id_theme) FROM stdin;
1	Sécurité	1
2	Afrique	2
3	dév	1
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('category_id_seq', 4, true);


--
-- Data for Name: favorite; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY favorite (id, annotation, url, title, description, publication_date, id_stream) FROM stdin;
17		https://www.lemondeinformatique.fr/actualites/lire-rgpd-microsoft-ajoute-une-app-pour-voir-les-donnees-collectees-depuis-windows-10-70753.html	RGPD : Microsoft ajoute une app pour voir les données collectées depuis Windows 10	Depuis la semaine dernière, les utilisateurs bêtas de Windows 10 peuvent tester l’aperçu d'une application qui permet de voir (...)	2018-02-02 14:15:31	10
18		https://www.lemondeinformatique.fr/actualites/lire-conference-cio-la-cybersecurite-a-l-heure-de-l-intelligence-artificielle-70746.html	Conférence CIO :  La cybersécurité à l'heure de l'intelligence artificielle	Si le RSSI doit sécuriser le système d'information de son entreprise face à des cybermenaces toujours plus complexes, il doit aussi (...)	2018-02-02 10:04:59	10
19		https://www.lemondeinformatique.fr/actualites/lire-bpifrance-1-3-mdeteuro-de-financement-a-l-innovation-en-2017-70743.html	Bpifrance : 1,3 Md&amp;euro; de financement à l'innovation en 2017	« Des résultats de grande qualité » obtenus à travers une « gamme de produits extrêmement profonde ». (...)	2018-02-01 18:29:52	10
20		https://www.lemondeinformatique.fr/actualites/lire-l-usage-detourne-des-big-data-de-strava-met-en-danger-les-militaires-70738.html	L'usage détourné des big data de Strava met en danger les militaires	Les big data sont aussi pratiques que dangereuses dans certains cas. Tel pourrait être l'enseignement tiré de l'usage détourné (...)	2018-02-01 18:13:46	10
\.


--
-- Name: favorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('favorite_id_seq', 20, true);


--
-- Data for Name: reader; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY reader (id, pseudo, password, secret) FROM stdin;
1	auguste	augusted	EvyPpjt3kgwZGJeMZkUnXdSSA9YHJiPkVFSwm4msCcYsdDwWNNhtmSyinxhYo8krnHCeR2xBdZmHBvLsmAiVGWPilwJVVprryUqRVQFC877gRGS1FIVK7C2tgLxCe5BcPaq2NVBZx6jBLipdy8g7L3VJl4uSHzVGfFPKu94t3v6loOgZ4I1mkCHSgyiCX3NkIP3RlFDzOSP5ROoknIe3946CImQvFRxkYVGgsPs7RQO1XA6YhoPiKkJQ7ZxqgRF
\.


--
-- Name: reader_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('reader_id_seq', 1, true);


--
-- Data for Name: stream; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY stream (id, url, name, id_category) FROM stdin;
10	https://www.lemondeinformatique.fr/flux-rss/thematique/securite/rss.xml	le monde info	1
\.


--
-- Name: stream_id_seq; Type: SEQUENCE SET; Schema: public; Owner: virgil
--

SELECT pg_catalog.setval('stream_id_seq', 13, true);


--
-- Data for Name: theme; Type: TABLE DATA; Schema: public; Owner: virgil
--

COPY theme (id, name, id_reader) FROM stdin;
1	Informatique	1
2	Politique	1
3	\N	\N
\.


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

