from scripts.load import load_data
from scripts.export import export_data
import cmd
import os

DEFAULT_ROOMS_FILEPATH = os.path.join('source', 'rooms.json')
DEFAULT_STUDENTS_FILEPATH = os.path.join('source', 'students.json')

class MyCLI(cmd.Cmd):
    prompt = 'MyCLI>>'
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_load(self, arg):
        try:
            load_data(DEFAULT_ROOMS_FILEPATH, DEFAULT_STUDENTS_FILEPATH)
        except Exception as e:
            print(f'Error occured during data load: {e}')

    
    def do_export(self, arg):
        if arg not in ['json', 'xml']:
            print('Error. Format must be json or xml.')
            return
        try:
            export_data(arg)
            print(f'Data successfully exported to {arg} format.')
        except Exception as e:
            print(f'Error occured during data export {e}')

        
    def do_exit(self, arg):
        print('Bye')
        return True
