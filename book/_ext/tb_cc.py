import os
from sphinx.application import Sphinx
import numpy as np

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def calc_mid_and_min(rgb):

    # convert to hex
    hex = rgb_to_hex(rgb)
    hex_mid = hex+'20'
    hex_min = hex+'05'

    return hex_mid, hex_min

def hue_rotate(rgb,angle):
    # angle must be in degrees

    rgb = np.array(rgb)

    A1 = np.array([[0.213,0.715,0.072],[0.213,0.715,0.072],[0.213,0.715,0.072]])
    A2 = np.array([[0.787,-0.715,-0.072],[-0.213,0.285,-0.072],[-0.213,-0.715,0.928]])
    A3 = np.array([[-0.213,-0.715,0.928],[0.143,0.140,-0.283],[-0.787,0.715,0.072]])

    A = A1 + np.cos(np.deg2rad(angle))*A2+np.sin(np.deg2rad(angle))*A3

    rgb = A@rgb
    rgb = np.round(rgb).astype(int)
    rgb[rgb>255] = 255
    rgb[rgb<0] = 0

    return list(rgb)

def saturate(rgb,sat):
    # sat must be scalar

    rgb = np.array(rgb)

    A1 = np.array([[0.213,0.715,0.072],[0.213,0.715,0.072],[0.213,0.715,0.072]])
    A2 = np.array([[0.787,-0.715,-0.072],[-0.213,0.285,-0.072],[-0.213,-0.715,0.928]])
    
    A = A1 + sat*A2

    rgb = A@rgb
    rgb = np.round(rgb).astype(int)
    rgb[rgb>255] = 255
    rgb[rgb<0] = 0
    
    return list(rgb)

def write_css(app,exc):

    list_of_colors = app.config.tb_cc_list
    # generate list of names
    names = list(list_of_colors.keys())
    # get rgb code for light colors
    light_colors = {}
    for name in names:
        rgb = list_of_colors[name][0:3]
        light_colors[name] = rgb_to_hex(rgb)
        hex_mid, hex_min = calc_mid_and_min(rgb)
        light_colors[name+'-mid'] = hex_mid
        light_colors[name+'-min'] = hex_min
    # if dark colors are required, get/generate them
    if app.config.tb_cc_dark_and_light:
        # assumption: get overrules generate
        dark_colors = {}
        for name in names:
            if len(list_of_colors[name])>3:
                # get
                rgb = list_of_colors[name][3:]
            else:
                # generate
                # 1) invert
                rgb = [255-c for c in list_of_colors[name][0:3]]
                # 2) rotate hue
                rgb = hue_rotate(rgb,180)
                # 3) saturate
                rgb = saturate(rgb,1.5)
            dark_colors[name] = rgb_to_hex(rgb)
            hex_mid, hex_min = calc_mid_and_min(rgb)
            dark_colors[name+'-mid'] = hex_mid
            dark_colors[name+'-min'] = hex_min

    # now set the CSS
    CSS_content = ''
    # light color string
    CSS_light = '/* (light/default mode) colors */\n:root {'
    for name in light_colors:
        CSS_light += '\n\t--%s: %s;'%(name,light_colors[name])
    CSS_light += '\n}'
    CSS_content += CSS_light+'\n\n'
    # dark color string
    if app.config.tb_cc_dark_and_light:
        CSS_dark = '/* dark mode colors */\nhtml[data-theme="dark"] {'
        for name in dark_colors:
            CSS_dark += '\n\t--%s: %s;'%(name,dark_colors[name])
        CSS_dark += '\n}'
        CSS_content += CSS_dark+'\n\n'
    # class strings
    CSS_class = '/* LaTeX classes */\n'
    for name in names:
        CSS_class += '.%s {color: var(--%s);}\n'%(name,name)
    CSS_content += CSS_class+'\n\n'
    # admonitions
    base = '/* <color> admonition */\ndiv.admonition.<color> {\n\tborder-color: var(--<color>);\n\tbackground-color: var(--<color>-min);\n}\n'
    base += 'div.admonition.<color> > .admonition-title {\n\tcolor: var(--pst-color-text-base);\n\tbackground-color: var(--<color>-mid);\n}\n'
    base += 'div.admonition.<color> > .admonition-title::after {\n\tcolor: var(--<color>);\n}\n'
    CSS_admonitions = '/* Admonitions */\n'
    for name in names:
        CSS_admonitions += base.replace('<color>',name)
    CSS_content += CSS_admonitions
    # write the css file
    staticdir = os.path.join(app.builder.outdir, '_static')
    filename = os.path.join(staticdir,'tb_cc.css')
    with open(filename,"w") as css:
        css.write(CSS_content)

    return

def set_latex(app,conf):

    old =  app.config

    for name in old.tb_cc_list:
        newcommand_name = name
        newcommand_content = ['\class{%s}{#1}'%(name),1]
        
        if 'mathjax3_config' in old:
            old_mj = old.mathjax3_config
            if old_mj is None:
                old['mathjax3_config'] = {'tex': {'macros': {newcommand_name: newcommand_content}}}
            elif 'tex' in old_mj:
                old_mj_tex = old.mathjax3_config['tex']
                if 'macros' in old_mj_tex:
                    old_mj_tex['macros'] = old_mj_tex['macros'] | {newcommand_name: newcommand_content}
                    old.mathjax3_config['tex'] = old_mj_tex
                else:
                    old.mathjax3_config['tex'] = old.mathjax3_config['tex'] | {'macros': {newcommand_name: newcommand_content}}
            else:
                old.mathjax3_config['tex'] = {'macros': {newcommand_name: newcommand_content}}
        else:
            old['mathjax3_config'] = {'tex': {'macros': {newcommand_name: newcommand_content}}}
        
    app.config = old

    print(app.config.mathjax3_config['tex']['macros'])

    return

def setup(app: Sphinx):
    app.add_config_value('tb_cc_list', None, 'env')
    app.add_config_value('tb_cc_dark_and_light', True, 'env')
    app.add_css_file('tb_cc.css')

    app.connect('config-inited',set_latex)
    app.connect("build-finished",write_css)

    return