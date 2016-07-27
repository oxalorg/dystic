import operator

def sort_list_dict(d):
    return sorted(d, key=operator.itemgetter('date'), reverse=True)
