#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_row(row):
        return (row if row != search else replace)
    return list(map(s_r_row, my_list))
