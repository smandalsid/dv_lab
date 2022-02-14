
import matplotlib.pyplot as plt
import pandas as pd
x=[ i for i in range(10)]
y=["{:02X}".format(i*2) for i in range(10)]
z=[[i for i in range(10)] for j in range(10)]
print(x)
print(y)
print(z)

fig, ax = plt.subplots()
ax.set_axis_off()
plt.table(cellText=z,rowLabels=y,colLabels=x,rowColours=["Palegreen"]*10,colColours=["Palegreen"]*10,cellLoc="center",loc="upper left")
plt.show()



# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# x=[ i for i in range(10)]
# y=["{:02X}".format(i*2) for i in range(3)]
# z=[[i for i in range(10)] for j in range(3)]
# print(x)
# print(y)
# print(z)

# fig, ax = plt.subplots()
# ax.set_axis_off()
# rcol=plt.cm.BuPu(np.full(len(y),0.1))
# ccolor=[["r","r","r","r","r","r","r","r","r","r"],["r","r","r","r","r","r","r","r","r","r"],["r","r","r","r","r","r","r","r","r","r"]]
# plt.table(cellText=z,cellColours=ccolor,rowLabels=y,colLabels=x,rowColours=rcol,colColours=["Palegreen"]*10,cellLoc="center",loc="upper left")
# plt.show()

# importing necessary packagess
# import numpy as np
# import matplotlib.pyplot as plt


# # input data values
# data = [[322862, 876296, 45261, 782372, 32451],
# 		[58230, 113139, 78045, 99308, 516044],
# 		[89135, 8552, 15258, 497981, 603535],
# 		[24415, 73858, 150656, 19323, 69638],
# 		[139361, 831509, 43164, 7380, 52269]]

# # preparing values for graph
# columns = ('Gokul', 'Kwality', 'Bakhri', 'Arun', 'Amul')
# rows = ['%d months' % x for x in (50, 35, 20, 10, 5)]
# values = np.arange(0, 2500, 500)
# value_increment = 1000

# # Adding pastel shades to graph
# colors = plt.cm.Oranges(np.linspace(22, 3, 12))
# n_rows = len(data)
# index = np.arange(len(columns)) + 0.3
# bar_width = 0.4

# # Initialing vertical-offset for the graph.
# y_offset = np.zeros(len(columns))

# # Plot bars and create text labels for the table
# cell_text = []
# for row in range(n_rows):
# 	plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
# 	y_offset = y_offset + data[row]
# 	cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])

# # Reverse colors and text labels to display table contents with
# # color.
# colors = colors[::-1]
# cell_text.reverse()

# # Add a table at the bottom
# the_table = plt.table(cellText=cell_text,
# 					rowLabels=rows,
# 					rowColours=colors,
# 					colLabels=columns,
# 					loc='bottom')

# # make space for the table:
# plt.subplots_adjust(left=0.2, bottom=0.2)
# plt.ylabel("Rise in Rs's".format(value_increment))
# plt.yticks(values * value_increment, ['%d' % val for val in values])
# plt.xticks([])
# plt.title('Cost of Milk od diff. brands')

# # plt.show()-display graph
# # Create image. plt.savefig ignores figure edge and face color.
# fig = plt.gcf()
# plt.savefig('pyplot-table-original.png',
# 			bbox_inches='tight',
# 			dpi=150)
