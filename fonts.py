from weasyprint import CSS
from weasyprint.fonts import FontConfiguration

def css_for_extra_fonts(add_bootstrap_style=False, add_vuetify_style=False):
    font_config = FontConfiguration()

    additional_style = ''
    if add_bootstrap_style:
        additional_style = open('bootstrap/bootstrap.css').read()
    elif add_vuetify_style:
        additional_style = open('bootstrap/vuetify.css').read()

    font_string = additional_style+'''
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
        
        @font-face {
            font-family: 'barcode';
            src: local(LibreBarcode39-Regular);
        }

        @font-face {
            font-family: 'Montserrat Regular';
            src: local('Montserrat-Regular');
        }
        @font-face {
            font-family: 'Montserrat Bold';
            src: local('Montserrat-Bold');
        }
        @font-face {
            font-family: 'Montserrat Bold Italic';
            src: local('Montserrat-BoldItalic');
        }
        @font-face {
            font-family: 'Montserrat Italic';
            src: local('Montserrat-Italic');
        }
        
        @font-face {
            font-family: 'Aleo Regular';
            src: local('Aleo-Regular');
        }
        @font-face {
            font-family: 'Aleo Bold';
            src: local('Aleo-Bold');
        }
        @font-face {
            font-family: 'Aleo Bold Italic';
            src: local('Aleo-BoldItalic');
        }
        @font-face {
            font-family: 'Aleo Italic';
            src: local('Aleo-Italic');
        }        

        @font-face {
            font-family: 'Roboto Regular';
            src: local('Roboto-Regular');
        }
        @font-face {
            font-family: 'Roboto Bold';
            src: local('Roboto-Bold');
        }
        @font-face {
            font-family: 'Roboto Bold Italic';
            src: local('Roboto-BoldItalic');
        }
        @font-face {
            font-family: 'Roboto Italic';
            src: local('Roboto-Italic');
        }

        @font-face {
            font-family: 'Arimo Regular';
            src: local('Arimo-Regular');
        }
        @font-face {
            font-family: 'Arimo Bold';
            src: local('Arimo-Bold');
        }
        @font-face {
            font-family: 'Arimo Bold Italic';
            src: local('Arimo-BoldItalic');
        }
        @font-face {
            font-family: 'Arimo Italic';
            src: local('Arimo-Italic');
        }
        
        @font-face {
            font-family: 'DM Sans Regular';
            src: local('DMSans-Regular');
        }
        @font-face {
            font-family: 'DM Sans Bold';
            src: local('DMSans-Bold');
        }
        @font-face {
            font-family: 'DM Sans Bold Italic';
            src: local('DMSans-BoldItalic');
        }
        @font-face {
            font-family: 'DM Sans Italic';
            src: local('DMSans-Italic');
        }    
        '''
    # print(font_string)
    return CSS(string=font_string, font_config=font_config), font_config
    
