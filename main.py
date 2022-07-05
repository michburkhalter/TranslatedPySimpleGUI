import gettext

import PySimpleGUI as sg


def main_window(my_window=None):
    menu_def = [_('&About'), [_('Close::close')]], [_('&Language'), ['&de', 'en']],
    layout_mainwindow = [
        [
            [sg.Menu(menu_def, pad=(10, 10))],
            [sg.Text(_('Select direction: '), key='txt_direction')], [sg.Combo([_('Left'), _('Right')], key='cmb_direction')],
            [sg.Button(_('Close'), key='btn_close')],
        ]
    ]

    new_window = sg.Window("Demo TranslatedPySimpleGui", layout_mainwindow, finalize=True)

    if my_window is not None:
        my_window.close()
    return new_window


if __name__ == '__main__':

    # Setup translations
    localedir = 'locale'
    translate = gettext.translation('messages', localedir=localedir, languages=['de'])
    _ = translate.gettext

    # Create window
    window = main_window()

    # Create event loop
    while True:
        event, values = window.read()

        # End program if user closes window or presses the Close button
        if event == sg.WIN_CLOSED or event == 'btn_close' or event.endswith("::close"):
            break

        elif event == 'de':
            translate = gettext.translation('messages', localedir=localedir, languages=['de'])
            _ = translate.gettext
            print(_("Language changed to DE"))
            window = main_window(window)

        elif event == 'en':
            translate = gettext.translation('messages', localedir=localedir, languages=['en'])
            _ = translate.gettext
            print(_("Language changed to EN"))
            window = main_window(window)

    window.close()
