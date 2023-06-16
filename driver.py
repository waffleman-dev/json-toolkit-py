from util import json_util
from resources import paths

if __name__ == '__main__':
    data = json_util.get_load(paths.PATH_DK_FUTURES)
    print(data)