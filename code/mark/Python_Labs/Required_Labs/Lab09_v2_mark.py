
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def draw_graph(data):
    top_of_graph = max(data)
    for i in range(top_of_graph,0, -1):
        row_list = []
        for item in data:
            if item >= i:
                row_list.append(" X ")
            else:
                row_list.append("   ")
        row_string = "".join(row_list)
        print(row_string)

draw_graph(data)


