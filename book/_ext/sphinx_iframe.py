from __future__ import annotations

import os

from docutils.parsers.rst import Directive, directives

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.util.typing import ExtensionMetadata

from typing import Optional

def generate_style(width: Optional[str], height: Optional[str],aspectratio: Optional[str]):

     styles = ''

     if width:
          styles += f'width: {width};'

     if height:
          styles += f'height: {height};'
     
     if aspectratio:
          styles += f'aspect-ratio: {aspectratio};'

     return styles

class IframeDirective(SphinxDirective):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'class': directives.class_option,
        "height": directives.unchanged,
        "width": directives.unchanged,
        "aspectratio": directives.unchanged
    }

    def run(self) -> list[nodes.Node]:

        assert self.arguments[0] is not None

        iframe_class = self.options.get("class")

        if self.name == "h5p":
             base_class = "sphinx h5p blend"
             if iframe_class is not None:
                  if "no-blend" in iframe_class:
                    base_class = "sphinx h5p"        
        elif self.name == "video":
             base_class = "sphinx video no-blend"
             if iframe_class is not None:
                  if "blend" in iframe_class and "not-blend" not in iframe_class:
                    base_class = "sphinx video"
        else:
             base_class = "sphinx"

        if iframe_class is None:
            iframe_class = base_class
        elif isinstance(iframe_class, list):
            iframe_class = base_class+" "+" ".join(iframe_class)
        else:
            iframe_class = base_class+""+str(iframe_class)
        
            
        style = generate_style(
            self.options.get("width", None), self.options.get("height", None),self.options.get("aspectratio",None)
        )
        if style != '':
            style = 'style="%s"'%(style)

        iframe_html = f"""
            <iframe class="{iframe_class}" {style} src="{self.arguments[0]}" allow="fullscreen *;autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" frameborder="0"></iframe>
		"""

        if self.name == "video":
             iframe_html = '<div class="video-container" %s>\n'%(style)
             iframe_html += f"""
                 <iframe class="{iframe_class}" src="{self.arguments[0]}" allow="fullscreen *;autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" frameborder="0"></iframe>
		     """
             iframe_html += '\n</div>'
        elif self.name == 'h5p':
             iframe_html = f"""
                 <iframe class="{iframe_class}" {style} src="{self.arguments[0]}" allow="fullscreen *;autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" frameborder="0"></iframe>
		     """
        else:
             iframe_html = '<div class="iframe-container" %s>\n'%(style)
             iframe_html += f"""
                 <iframe class="{iframe_class}" src="{self.arguments[0]}" allow="fullscreen *;autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" frameborder="0"></iframe>
		     """
             iframe_html += '\n</div>'

        iframe_node = nodes.raw(None, iframe_html, format="html")
        # paragraph_node = nodes.paragraph()
        # paragraph_node.insert(0, iframe_node)

        return [iframe_node]
    
def include_js(app: Sphinx):
     
     if app.config.iframe_h5p_autoresize:
          app.add_js_file("https://tudelft.h5p.com/js/h5p-resizer.js") # to support auto-width for h5p

     return

def setup(app: Sphinx):

    app.add_directive("iframe", IframeDirective)
    app.add_directive("h5p", IframeDirective)
    app.add_directive("video", IframeDirective)

    app.add_config_value("iframe_h5p_autoresize",True,'env')
    app.connect('builder-inited',include_js)

    app.add_config_value("iframe_blend_all",True,'env')
    app.add_config_value("iframe_saturation",1.5,'env')
    app.add_config_value("iframe_background","#ffffff",'env')
    
    app.add_css_file('sphinx_iframe.css')

    app.connect("build-finished",write_css)

    return

def write_css(app: Sphinx,exc):
    # now set the CSS
    CSS_content = ''
    
    # add blend or no-blend option if required
    if app.config.iframe_blend_all:
        CSS_content += "iframe.sphinx:not(.no-blend) {\n\tbackground: transparent;\n\tmix-blend-mode: darken;\n}\n\n" # blend all except no-blend
        CSS_content += "html[data-theme=dark] iframe.sphinx:not(.no-blend) {\n\tfilter: invert(1) hue-rotate(180deg) saturate(%s);\n\tbackground: transparent;\n\tmix-blend-mode: lighten;\n}\n\n"%(app.config.iframe_saturation) # blend all except no-blend
        CSS_content += "iframe.sphinx.no-blend {\n\tbackground: %s;\n\tborder-radius: .25rem;\n}\n"%(app.config.iframe_background)
    else:
        CSS_content += "iframe.sphinx.blend {\n\tbackground: transparent;\n\tmix-blend-mode: darken;\n}\n\n" # blend none except blend
        CSS_content += "html[data-theme=dark] iframe.sphinx.blend {\n\tfilter: invert(1) hue-rotate(180deg) saturate(%s);\n\tbackground: transparent;\n\tmix-blend-mode: lighten;\n}\n\n"%(app.config.iframe_saturation) # blend none except blend
        CSS_content += "iframe.sphinx:not(.blend) {\n\tbackground: %s;\n\tborder-radius: .25rem;\n}\n"%(app.config.iframe_background)
    
    # write the css file
    staticdir = os.path.join(app.builder.outdir, '_static')
    filename = os.path.join(staticdir,'sphinx_iframe.css')
    with open(filename,"w") as css:
        css.write(CSS_content)

    return