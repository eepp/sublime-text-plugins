import sublime
import sublime_plugin
import re
import os


class BtOpenOtherHeaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()

        if filename.endswith('-internal.h'):
            filename = re.sub(r'^(.*)-internal\.h$', r'\1.h', filename)
        elif filename.endswith('.h'):
            filename = filename[:-2] + '-internal.h'
        else:
            return

        if os.path.isfile(filename):
            self.window.open_file(filename)
