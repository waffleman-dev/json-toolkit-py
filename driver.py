from util import json_util, file_util
from resources import paths

if __name__ == '__main__':
    data = json_util.serialize(paths.PATH_DK_FUTURES)
    striped_json = json_util.strip_by_keys(data, ["name"])

    file_util.write_to_file(json_util.deserliaze(striped_json), paths.PATH_JSON_TEST_OUTPUT)