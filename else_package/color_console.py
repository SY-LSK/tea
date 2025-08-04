#small_package/color_console.py

color_config = {
    'red': '\033[31m',
    'yellow': '\033[33m',
    'end': '\033[0m'
}

def color_print(text,color):
    print(f"{color_config[color]}{text}{color_config['end']}")