# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, INTEGER, Index, LargeBinary, String, Text, text
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Avoir(Base):
    __tablename__ = 'avoir'

    id_avoir = Column(INTEGER(10), primary_key=True)
    avoir = Column(String(15), nullable=False, server_default=text("''"))
    id_facture = Column(INTEGER(10))
    facture = Column(String(20))
    date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    id_dossier = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_client = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    raison_soc = Column(String(255))
    adresse = Column(String(255))
    cp = Column(String(15))
    ville = Column(String(100))
    id_voyage = Column(INTEGER(10))
    voyage = Column(String(30))
    bateau = Column(String(100))
    port_emb = Column(String(100))
    port_deb = Column(String(100))
    fact_march = Column(String(255))
    mt_march = Column(DECIMAL(10, 2))
    cond_trans = Column(String(100))
    tot_colis = Column(DECIMAL(10, 2))
    tot_poids = Column(DECIMAL(10, 2))
    tot_volume = Column(DECIMAL(10, 3))
    col_nb = Column(String(100))
    col_type = Column(String(100))
    col_nature = Column(LargeBinary)
    col_poids = Column(String(100))
    col_volume = Column(String(100))
    lib_fac = Column(String(100))
    mt_fac = Column(String(100))
    tht = Column(DECIMAL(10, 2))
    tva = Column(DECIMAL(10, 2))
    ttc = Column(DECIMAL(10, 2))
    cond_regl = Column(TINYINT(3))
    reglement = Column(String(255))
    stat_avoir = Column(CHAR(1))


class Bonlivraison(Base):
    __tablename__ = 'bonlivraison'

    id_bl = Column(INTEGER(10), primary_key=True)
    bl = Column(String(20), index=True)
    id_dossier = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_voyage = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_client = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    desti_bl = Column(LargeBinary)
    tel = Column(String(50))
    mod_trans = Column(TINYINT(3))
    fact_march = Column(String(255))
    instruc1 = Column(String(255))
    instruc2 = Column(String(255))
    instruc3 = Column(String(255))
    col_nb = Column(String(100))
    col_type = Column(String(100))
    col_nature = Column(LargeBinary)
    col_poids = Column(String(100))
    col_volume = Column(String(100))
    obs_manifeste = Column(LargeBinary)
    stat_bl = Column(CHAR(1))


class Client(Base):
    __tablename__ = 'client'

    id_client = Column(INTEGER(10), primary_key=True)
    client = Column(String(20), nullable=False, index=True, server_default=text("''"))
    siret = Column(String(30))
    raison_soc = Column(String(255))
    adresse = Column(String(255))
    cp = Column(String(15))
    ville = Column(String(100))
    tel = Column(String(25))
    fax = Column(String(25))
    email = Column(String(100))
    contact_titre = Column(String(100))
    contact_nom = Column(LargeBinary)
    contact_fonction = Column(LargeBinary)
    contact_tel = Column(LargeBinary)
    contact_port = Column(LargeBinary)
    contact_fax = Column(LargeBinary)
    contact_email = Column(LargeBinary)
    police_flot = Column(CHAR(1))
    cond_regl = Column(TINYINT(3))
    obs = Column(LargeBinary)
    stat_cli = Column(CHAR(1))


class Document(Base):
    __tablename__ = 'documents'

    id_doc = Column(INTEGER(10), primary_key=True)
    nom = Column(String(50), nullable=False, server_default=text("''"))
    ddoc = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    titre = Column(String(255), nullable=False, server_default=text("''"))
    entete = Column(CHAR(1), nullable=False, server_default=text("''"))
    pied = Column(CHAR(1), nullable=False, server_default=text("''"))
    client = Column(CHAR(1), nullable=False, server_default=text("''"))
    date = Column(String(255), nullable=False, server_default=text("''"))
    attention = Column(String(255), nullable=False, server_default=text("''"))
    signature = Column(Text, nullable=False)
    objet = Column(Text, nullable=False)
    contenu = Column(Text, nullable=False)
    type = Column(CHAR(1), nullable=False, server_default=text("''"))
    droits = Column(String(20), nullable=False, server_default=text("''"))


class Dossier(Base):
    __tablename__ = 'dossier'

    id_dossier = Column(INTEGER(10), primary_key=True)
    dossier = Column(String(15), nullable=False, unique=True, server_default=text("''"))
    id_voyage = Column(String(15))
    id_client = Column(String(15))
    desti = Column(LargeBinary)
    expe = Column(LargeBinary)
    assur = Column(CHAR(1))
    cond_trans = Column(TINYINT(3))
    fact_march = Column(String(255))
    mt_march = Column(DECIMAL(10, 2))
    cond_regl = Column(TINYINT(3))
    tot_colis = Column(DECIMAL(10, 2))
    tot_poids = Column(DECIMAL(10, 2))
    tot_volume = Column(DECIMAL(10, 3))
    col_nb = Column(String(100))
    col_type = Column(String(100))
    col_nature = Column(LargeBinary)
    col_poids = Column(String(100))
    col_volume = Column(String(100))
    rem = Column(LargeBinary)
    type = Column(CHAR(1))
    stat_dos = Column(CHAR(1))


class Facture(Base):
    __tablename__ = 'facture'

    id_facture = Column(INTEGER(10), primary_key=True)
    facture = Column(String(15), nullable=False, server_default=text("''"))
    date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    id_dossier = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_client = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    raison_soc = Column(String(255))
    adresse = Column(String(255))
    cp = Column(String(15))
    ville = Column(String(100))
    id_voyage = Column(INTEGER(10))
    voyage = Column(String(30))
    bateau = Column(String(100))
    port_emb = Column(String(100))
    port_deb = Column(String(100))
    fact_march = Column(String(255))
    mt_march = Column(DECIMAL(10, 2))
    cond_trans = Column(String(100))
    tot_colis = Column(DECIMAL(10, 2))
    tot_poids = Column(DECIMAL(10, 2))
    tot_volume = Column(DECIMAL(10, 3))
    col_nb = Column(String(100))
    col_type = Column(String(100))
    col_nature = Column(LargeBinary)
    col_poids = Column(String(100))
    col_volume = Column(String(100))
    lib_fac = Column(String(100))
    mt_fac = Column(String(100))
    tht = Column(DECIMAL(10, 2))
    tva = Column(DECIMAL(10, 2))
    ttc = Column(DECIMAL(10, 2))
    cond_regl = Column(TINYINT(3))
    reglement = Column(String(255))
    stat_fac = Column(CHAR(1))
    valide = Column(CHAR(1), nullable=False, server_default=text("'n'"))


class Historique(Base):
    __tablename__ = 'historiques'

    id_hist = Column(INTEGER(10), primary_key=True)
    nom_doc = Column(String(50), nullable=False, server_default=text("''"))
    id_doc = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    pdf = Column(String(30), nullable=False, server_default=text("''"))
    date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    id_voyage = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_dossier = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_client = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    id_facture = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    usr_nom = Column(String(50), nullable=False, server_default=text("''"))
    usr_prenom = Column(String(50), nullable=False, server_default=text("''"))
    usr_droits = Column(String(20), nullable=False, server_default=text("''"))


class Proforma(Base):
    __tablename__ = 'proforma'

    id_proforma = Column(INTEGER(10), primary_key=True)
    proforma = Column(String(15), nullable=False, server_default=text("''"))
    date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    raison_soc = Column(String(255))
    adresse = Column(String(255))
    cp = Column(String(15))
    ville = Column(String(100))
    id_voyage = Column(INTEGER(10))
    voyage = Column(String(30))
    bateau = Column(String(100))
    port_emb = Column(String(100))
    port_deb = Column(String(100))
    fact_march = Column(String(255))
    mt_march = Column(DECIMAL(10, 2))
    cond_trans = Column(String(100))
    tot_colis = Column(DECIMAL(10, 2))
    tot_poids = Column(DECIMAL(10, 2))
    tot_volume = Column(DECIMAL(10, 3))
    col_nb = Column(String(100))
    col_type = Column(String(100))
    col_nature = Column(LargeBinary)
    col_poids = Column(String(100))
    col_volume = Column(String(100))
    lib_fac = Column(String(100))
    mt_fac = Column(String(100))
    tht = Column(DECIMAL(10, 2))
    tva = Column(DECIMAL(10, 2))
    ttc = Column(DECIMAL(10, 2))
    cond_regl = Column(TINYINT(3))
    obs = Column(String(255))
    stat_pro = Column(CHAR(1))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('usr_id_2', 'usr_id', 'usr_log'),
    )

    usr_id = Column(INTEGER(10), primary_key=True, unique=True)
    usr_log = Column(String(30), nullable=False, server_default=text("''"))
    usr_pw = Column(String(64), nullable=False, server_default=text("''"))
    usr_droits = Column(String(20), nullable=False, server_default=text("''"))
    usr_nom = Column(String(50))
    usr_prenom = Column(String(50))
    usr_dcreation = Column(DateTime)


class Voyage(Base):
    __tablename__ = 'voyage'

    id_voyage = Column(INTEGER(10), primary_key=True)
    voyage = Column(String(30), nullable=False, unique=True, server_default=text("''"))
    d_dep = Column(DateTime)
    bateau = Column(String(100))
    mode_trans = Column(String(50))
    port_emb = Column(TINYINT(3))
    port_deb = Column(TINYINT(3))
    deb_lib = Column(String(100))
    deb_mt = Column(LargeBinary)
    deb_total = Column(DECIMAL(10, 2))