import sublime
import sublime_plugin
import re
import os
import os.path


def _find_bt_dir(path):
    bt_dir = path

    while True:
        if os.path.isfile(os.path.join(bt_dir, 'configure.ac')):
            break

        bt_dir = os.path.dirname(bt_dir)

        if bt_dir == '/':
            return

    return bt_dir


class BtOpenOtherSourceCommand(sublime_plugin.WindowCommand):
    def run(self):
        active_view = self.window.active_view()
        path = active_view.file_name()
        bt_dir = _find_bt_dir(path)

        if bt_dir is None:
            return

        filename = os.path.basename(path)

        if filename.endswith('.h'):
            search_filenames = (filename[:-2] + '.c',)
            search_dir = os.path.join(bt_dir, 'lib')
        elif filename.endswith('.c'):
            search_filenames = (
                filename[:-2] + '.h',
                filename[:-2] + '-internal.h',
            )
            search_dir = os.path.join(bt_dir, 'include')

        for root, dirs, files in os.walk(search_dir):
            if 'ctf-writer' in root:
                continue

            for search_filename in search_filenames:
                if search_filename in files:
                    src = os.path.join(root, search_filename)

                    if os.path.isfile(src):
                        self.window.open_file(src)
                        return
