# coding: utf-8
from datetime import date

import boundaries

boundaries.register('Sherbrooke districts',
    domain='Sherbrooke, QC',
    last_updated=date(2014, 2, 19),
    name_func=boundaries.clean_attr('NOM'),
    id_func=boundaries.attr('NUMERO'),
    source_url='http://donnees.ville.sherbrooke.qc.ca/dataset/districts-electoraux',
    data_url='http://donnees.ville.sherbrooke.qc.ca/storage/f/2014-02-19T19%3A28%3A50.620Z/districtelectoral-shp.zip',
    licence_url='http://donnees.ville.sherbrooke.qc.ca/licence',
    authority='Ville de Sherbrooke',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2443027'},
)
