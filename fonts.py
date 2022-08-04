from weasyprint import CSS
from weasyprint.fonts import FontConfiguration

def css_for_extra_fonts(add_bootstrap_style=False):
    font_config = FontConfiguration()

    bootstrap_style = ''
    if add_bootstrap_style:
        bootstrap_style = open('bootstrap/bootstrap.css').read()    

    font_string = bootstrap_style+'''
        @font-face {
            font-family: 'BC Sans Regular';
            src: local('BCSans-Regular');
        }
        @font-face {
            font-family: 'BC Sans Bold';
            src: local('BCSans-Bold');
        }
        @font-face {
            font-family: 'BC Sans Bold Italic';
            src: local('BCSans-BoldItalic');
        }
        @font-face {
            font-family: 'BC Sans Italic';
            src: local('BCSans-Italic');
        }
        @font-face {
            font-family: 'Noto Sans Light';
            src: local('NotoSans-Light');
        }
        @font-face {
            font-family: 'Noto Sans Light Italic';
            src: local('NotoSans-LightItalic');
        }        
        '''
    # print(font_string)
    return CSS(string=font_string, font_config=font_config), font_config
    
