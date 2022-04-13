import sublime
import sublime_plugin


THEMES = {
    "Light": {
        "theme": "Default.sublime-theme",
        "color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow.tmTheme",
    },
    "Dark": {
        "theme": "Default Dark.sublime-theme",
        "color_scheme": "Tomorrow Night.sublime-color-scheme",
    },
}


class SwitchThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, theme="Light") -> None:
        if theme not in THEMES:
            sublime.error_message(f"invalid theme: {theme}")
            return
        s = sublime.load_settings("Preferences.sublime-settings")
        for key, val in THEMES[theme].items():
            s.set(key, val)
        sublime.save_settings("Preferences.sublime-settings")
