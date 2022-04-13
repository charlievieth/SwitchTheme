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
    def run(self, theme_name="Light", light=None, dark=None) -> None:
        # FIXME: going from Dark to Light sometimes fails to change the Theme
        # themes = sublime.load_settings("SwitchTheme.sublime-settings").get("themes")

        if theme_name not in THEMES:
            sublime.error_message(f"invalid theme: {theme_name}")
            return
        s = sublime.load_settings("Preferences.sublime-settings")
        s.update(THEMES[theme_name])
        sublime.save_settings("Preferences.sublime-settings")
