#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_row(row):
	    return (row if row =! search else replace)
    return list(map(search_research_row, my_list))
