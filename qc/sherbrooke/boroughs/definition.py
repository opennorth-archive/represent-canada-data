# coding: utf-8
from datetime import date

import boundaries

# @see http://www.toponymie.gouv.qc.ca/ct/toponymie-municipale/municipalites-arrondissements/arrondissement.aspx
# @see http://www.mamrot.gouv.qc.ca/repertoire-des-municipalites/fiche/arrondissement/?tx_mamrotrepertoire_pi1[order]=asc_nom_mun
boundaries.register('Sherbrooke boroughs',
    domain='Sherbrooke, QC',
    last_updated=date(2013, 12, 16),
    name_func=lambda f: re.sub(r'Arrondissement d[eu] ', '', f.get('NOM')).replace(u'', u'—'), # zero-width space, m-dash
    id_func=boundaries.attr('NUMERO'),
    source_url='http://donnees.ville.sherbrooke.qc.ca/dataset/arrondissements',
    data_url='http://donnees.ville.sherbrooke.qc.ca/storage/f/2014-02-19T15%3A46%3A25.089Z/arrondissement-shp.zip',
    licence_url='http://donnees.ville.sherbrooke.qc.ca/licence',
    authority='Ville de Sherbrooke',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2443027'},
)
