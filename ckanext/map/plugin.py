import pylons
import ckan.plugins as p
import ckan.model as model
from ckan.common import c
import ckanext.nhm.logic.action as action
from ckanext.nhm.model import setup as setup_model
import ckanext.nhm.lib.helpers as nhmhelpers
import sqlalchemy.exc

import ckan.logic as logic
get_action = logic.get_action

class MapPlugin(p.SingletonPlugin):
    """
    Theme for the NHM data portal
    """
    p.implements(p.IConfigurer)

    ## IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_resource('theme/public', 'map')
