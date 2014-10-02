import namere


def analyze_file(filename):
    names_dict = {}
    with open(filename) as f:
        for line in f:
            increment_count_dict(names_dict, namere.find_names(line))

    return names_dict


def increment_count_dict(orig_dict, name_list):
    for name in name_list:
        if name in orig_dict:
            orig_dict[name] = orig_dict[name] + 1
        else:
            orig_dict[name] = 1
