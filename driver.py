from util import json_util, file_util
from resources import paths

if __name__ == '__main__':
    data = json_util.serialize(paths.PATH_DK_FUTURES)
    key_value_pairs = [("label", "Defensive Rookie of the Year"), ("label", "Offensive Rookie of the Year")]

    targetted_nodes = json_util.get_nodes(data, key_value_pairs)
    stripped_json = json_util.strip_by_keys(targetted_nodes, ["id", "label", "oddsAmerican", "outcomes"])

    file_util.write_to_file(json_util.deserliaze(stripped_json), paths.PATH_JSON_TEST_OUTPUT)