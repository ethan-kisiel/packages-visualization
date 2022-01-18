class Color:
    '''
    Takes an array[r,g,b,a] (r,g,b=(0-255) a=(0.0-1.0))
    Converts to :  #AARRGGBB Hex,
    '''
    def __init__(self, rgba):
        self.rgba = rgba
        
        # conversion table for dec to hex
        global HEX_CONVERSION
        HEX_CONVERSION = ['0', '1', '2', '3', '4', '5', '6', '7',
                          '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    def convert_to_ARGB(self, rgba=None):
        '''
        Takes self or an optional array[r,g,b,a] (r,g,b=(0-255) a=(0.0-1.0))
        Returns String 'AARRGGBB'
        '''
        
        #TODO: add catch/throws(?) for wrong size array 
        if rgba is None:
            ov = self.rgba
        else:
            ov = rgba
        
        # conversion to hex:
        nv = [HEX_CONVERSION[int((ov[3] * 255) / 16)], HEX_CONVERSION[int((ov[3] * 255) % 16)],
              HEX_CONVERSION[int(ov[0] / 16)], HEX_CONVERSION[int(ov[0] % 16)],
              HEX_CONVERSION[int(ov[1] / 16)], HEX_CONVERSION[int(ov[1] % 16)],
              HEX_CONVERSION[int(ov[2] / 16)], HEX_CONVERSION[int(ov[2] % 16)]]
 
        # conversion to string:
        return f'{nv[0]}{nv[1]}{nv[2]}{nv[3]}{nv[4]}{nv[5]}{nv[6]}{nv[7]}'
        