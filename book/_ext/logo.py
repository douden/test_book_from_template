def logo_def(app,conf):
    if conf.tud_change_logo:
        print('Changing logo to TU Delft logo')
        old =  app.config.html_theme_options
        old['logo'] = {'image_light':'_static\TUDelft_logo_descriptor_rgb.png','image_dark': '_static\TUDelft_logo_descriptor_white.png'}
        app.config.html_theme_options = old
    else:
        print('Using user-defined logo')

def setup(app):
    app.add_config_value('tud_change_logo', True, 'env')

    app.connect('config-inited',logo_def)