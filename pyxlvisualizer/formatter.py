from openpyxl import load_workbook
from openpyxl.styles import PatternFill

class Formatter():
    
    def __init__(self, keys=None, colors=None):
        if colors is None:
            colors = ['C0000000', 'C0FF0000', 'C000FF00', 'C00000FF']
        if keys is None:    
            keys = ['A', 'B', 'C', 'D']
            
        # TODO: add exception for mismatched array size
        self.colors = dict(zip(keys, colors))

    # Overwrites the color-code dictionary
    def overwrite_colors(self, new_dict: dict):
        self.colors = new_dict
    
    # Color must be ARGB hex value without '#'
    def set_color(self, key, color: str):
        try:
            self.colors[key] = color
        except KeyError:
            print('KeyError; invalid key')
    
    def set_key(self, key, new_key):
        try:
            self.colors[new_key] = self.colors.pop(key)
        except KeyError:
            print('KeyError; invalid key')

    # TODO: Adjust file_loc/file_name to make renaming of file smoother
    # TODO: Add functionality for changing fill type
    def format_spreadsheet(self, file_loc: str, new_sheet_name: str=None, cell_columns=None):
        if cell_columns is None:
            cell_columns = ['A', 'B', 'C']
        if new_sheet_name is None:
            new_sheet_name = 'New Sheet'

        wb = load_workbook(filename=file_loc)
        ws = wb.active
        counter = 2
        # while first column, row HAS data
        while ws[f'{cell_columns[0]}{counter}'].internal_value:
            # get the value of first column @ current row (counter)
            current_person = ws[f'A{counter}'].internal_value
            #print(color_codes[current_person])
            for i in range(len(cell_columns)):
                ws[f'{cell_columns[i]}{counter}'].fill = PatternFill(fill_type='lightUp', fgColor=self.colors[current_person])
            counter += 1
        ws.title = new_sheet_name
        wb.save(filename=f'NEW-{file_loc}')

