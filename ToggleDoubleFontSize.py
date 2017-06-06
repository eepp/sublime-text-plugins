import sublime
import sublime_plugin


class ToggleDoubleFontSizeCommand(sublime_plugin.WindowCommand):
    def run(self):
        preferences = sublime.load_settings('Preferences.sublime-settings')
        font_size = preferences.get('font_size')

        if font_size <= 15:
            font_size *= 2
        else:
            font_size /= 2

        preferences.set('font_size', font_size)
