
# Scatter plot example in Bokeh

from bokeh.plotting import figure, show, output_file, reset_output
import numpy as np
import pandas as pd
import os

os.getcwd()
os.chdir('/Users/zacklarsen/Desktop/Projects/Dataviz/Python')
os.listdir()

snowmobiles = pd.read_excel('hodnrtempboatssnowmastercurrentexcelfiles20181001snowactiveregistrations.xlsx')
snowmobiles.head()
snowmobiles.columns

# Just pull the three biggest counties for this:
snowmobiles = snowmobiles[snowmobiles['COUNTY'].isin(["COOK","DUPAGE","WILL"])]
snowmobiles.head()

# Remove rows with zero values:
snowmobiles = snowmobiles[snowmobiles['Model_Year'] != 0]
snowmobiles = snowmobiles[snowmobiles['Horsepower'] != 0]
snowmobiles[['Model_Year','Horsepower']].head()

# Outliers:
snowmobiles = snowmobiles[~snowmobiles['Model_Year'] <= 1950]

# For the scatterplot, we need to pull out two numeric variables and a class variable.
x = snowmobiles['Model_Year'].astype(int)
y = snowmobiles['Horsepower']
# The class might be county:
snowClass = snowmobiles['COUNTY']

# Map the colors so we can group color by class
colormap = {'COOK': 'blue', 'DUPAGE': 'red', 'WILL': 'green'}
colors = [colormap[x] for x in snowmobiles['COUNTY']]
colors






# Delete before trying again:
del p
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm Scatter.html
ls






p = figure(title = "Snowmobile Scatterplot")
p.xaxis.axis_label = 'Model Year'
p.yaxis.axis_label = 'Horsepower'
p.circle(x, y, color=colors, fill_alpha=0.2, size=10)

p.legend.location = "top_left"
p.legend.click_policy="hide"

output_file("Scatter.html", title="Scatter.py example")

show(p)
















# MPG

from bokeh.sampledata.autompg import autompg_clean as df
df = df.copy()

# data cleanup
df.cyl = df.cyl.astype(str)
df.yr = df.yr.astype(str)
del df['name']
df.head()

columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
discrete
continuous = [x for x in columns if x not in discrete]
continuous



# Delete before trying again:
del p
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm mpg_scatter.html
ls



x = df['hp']
y = df['mpg']
radii = df['weight']
colors = df['mfr']

TOOLS="hover,pan,wheel_zoom,box_zoom,reset,save"
p = figure(tools=TOOLS)

#radius=radii,
p.scatter(x,
          y,
          fill_color=colors,
          fill_alpha=0.6,
          line_color=None)

output_file("mpg_scatter.html", title="mpg_scatter.py example")
show(p)




















from bokeh.layouts import row, column
from bokeh.models import BoxSelectTool, LassoSelectTool, Spacer
from bokeh.plotting import figure, curdoc

N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)]
TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"


# Delete before trying again:
del p
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm color_scatter.html
ls


p = figure(tools=TOOLS)
p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.6,
          line_color=None)

output_file("color_scatter.html", title="color_scatter.py example")
show(p)









#
#
# import bokeh.plotting as bpl
# import bokeh.models as bmo
# from bokeh.palettes import d3
# #bpl.output_notebook()
#
#
# df = pd.DataFrame(
#     {
#         "journey": ['ch1', 'ch2', 'ch2', 'ch1'],
#         "cat": ['a', 'b', 'a', 'c'],
#         "kpi1": [1,2,3,4],
#         "kpi2": [4,3,2,1]
#     }
# )
# source = bpl.ColumnDataSource(df)
#
# # use whatever palette you want...
# palette = d3['Category10'][len(df['cat'].unique())]
# color_map = bmo.CategoricalColorMapper(factors=df['cat'].unique(),
#                                    palette=palette)
#
# # create figure and plot
# p = bpl.figure()
# p.scatter(x='kpi1', y='kpi2',
#           color={'field': 'cat', 'transform': color_map},
#           legend='cat', source=source)
#
# #bpl.show(p)
# show(p)



