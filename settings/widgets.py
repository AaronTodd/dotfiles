from libqtile import widget
from .theme import colors
import psutil
from libqtile import bar
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
bateria = ""
battery = psutil.sensors_battery()
percent = int(battery.percent)
def baterias():
    global bateria
    if(percent >= 95):
        bateria = " 󰁹"
    elif(percent >= 90):
        bateria = " 󰂂"
    elif(percent <= 90 and percent >= 80 ):
        bateria = " 󰂁"
    elif(percent <= 80 and percent >= 70 ):
        bateria = " 󰂀"
    elif(percent <= 70 and percent >= 60 ):
        bateria = " 󰁿"
    elif(percent <= 60 and percent >= 50 ):
        bateria = " 󰁾"
    elif(percent <= 50 and percent >= 40 ):
        bateria = " 󰁽"
    elif(percent <= 40 and percent >= 30 ):
        bateria = " 󰁼"
    elif(percent <= 30 and percent >= 20 ):
        bateria = " 󰁻"
    elif(percent <= 20 and percent >= 10 ):
        bateria = " 󰁺"
    elif(percent <= 10 and percent >= 5 ):
        bateria = " 󰁺"
    elif(percent <= 5 and percent >= 0 ):
        bateria = " 󰂃"


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='SpaceMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

baterias()
primary_widgets = [
    *workspaces(),
    separator(),
    

    powerline('color4', 'dark'),

    widget.TextBox(
        **base(bg='color4'),
       text = bateria  # Icono: nf-fa-battery-three-quarters
    ),

    widget.Battery(
        **base(bg='color4'),
        format='{percent:2.0%}',
        charge_char='',
        discharge_char='',
        full_char='',
        empty_char='',
        update_interval=5,
        low_percentage=0.2
    ),


    powerline('color3', 'color4'),

    icon(bg="color3", text=' todd '),  # Icon: nf-fa-feed
    

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'SpaceMono Nerd Font',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

bar.Bar(
    [

    ],
    100,  # Ajusta la altura según tus preferencias
    orientation='vertical',
),
