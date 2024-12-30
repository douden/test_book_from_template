import os

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file

def set_mtext(app,conf):
    if conf.tud_change_mtext:
        print('Changing mtext font to inherited from html')
        old =  app.config
        
        if 'mathjax3_config' in old:
            old_mj = old.mathjax3_config
            print(old_mj)
            if old_mj is None:
                old['mathjax3_config'] = {'chtml': {'mtextInheritFont': True}}
            elif 'chtml' in old_mj:
                old.mathjax3_config['chtml'] = old.mathjax3_config['chtml'] | {'mtextInheritFont': True}
            else:
                old.mathjax3_config['chtml'] = {'mtextInheritFont': True}         
        else:
            old['mathjax3_config'] = {'chtml': {'mtextInheritFont': True}}
            
        app.config = old
    else:
        print('Using default/user defined mtext font')

def setup(app: Sphinx):
    app.add_config_value('tud_change_mtext', True, 'env')
    app.connect('config-inited',set_mtext)