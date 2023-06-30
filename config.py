# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles


from libqtile import hook
from libqtile import bar
from libqtile import widget

from subprocess import Popen

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults, bar
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'

def set_window_rounded_corners(win_id):
    # Configura el radio de las esquinas circulares (ajusta el valor según tus preferencias)
    radius = 10

    # Obtén la geometría actual de la ventana
    cmd = f"xdotool getwindowgeometry --shell {win_id}"
    output = Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode("utf-8")
    geometry = dict(line.strip().split('=') for line in output.splitlines())

    # Calcula las nuevas dimensiones de la ventana con esquinas circulares
    new_width = int(geometry['WIDTH']) - 2 * radius
    new_height = int(geometry['HEIGHT']) - 2 * radius
    new_x = int(geometry['X']) + radius
    new_y = int(geometry['Y']) + radius

    # Ejecuta el comando para redimensionar y mover la ventana
    cmd = f"xdotool windowsize {win_id} {new_width} {new_height}; xdotool windowmove {win_id} {new_x} {new_y}; xdotool windowshape {win_id} radius {radius}"
    Popen(cmd, shell=True)

@hook.subscribe.client_new
def set_rounded_corners(client):
    # Verifica si la ventana recién creada es una ventana normal
    if client.window.wm_type == 'NORMAL':
        # Llama a la función para aplicar las esquinas circulares
        set_window_rounded_corners(client.window.wid)
