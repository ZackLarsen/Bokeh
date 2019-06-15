

# Dataviz project for plotting snowmobile registrations by county in Illinois using Bokeh
# Zack Larsen 10/27/2018

# Snowmobile data downloaded from:
#https://data.illinois.gov/dataset/1fab1c10-5230-4e75-8c4c-96ae08a1bd56/resource/6c7c1f88-4748-4691-9df8-04a3067c5eab/download/hodnrtempboatssnowmastercurrentexcelfiles20181001snowactiveregistrations.xlsx

import pandas as pd
pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",20)
import os

from bokeh.io import show
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.plotting import figure, output_file, save

palette.reverse()



os.getcwd()
os.chdir('/Users/zacklarsen/Desktop/Projects/Dataviz/Python')
os.listdir()

snowmobiles = pd.read_excel('hodnrtempboatssnowmastercurrentexcelfiles20181001snowactiveregistrations.xlsx')
snowmobiles.head()

# Get the snowmobile counts by counties in a dictionary:
df = snowmobiles.groupby('COUNTY').Registration_Number.nunique().reset_index(name='counts')
county_snowmobiles = pd.Series(df['counts'].values,index=df['COUNTY']).to_dict()
# county_snowmobiles
# len(county_snowmobiles) # 91


# Save shape longitude and latitude values for all Illinois counties:
counties = {
    code: county for code, county in counties.items() if county["state"] == "il"
}

# counties

county_names = [county['name'].upper() for county in counties.values()]
# len(county_names) # 102
# county_names
county_xs = [county["lons"] for county in counties.values()]
# len(county_xs) # 102
# county_xs
county_ys = [county["lats"] for county in counties.values()]
# len(county_ys) # 102
# county_ys



# Get the counties that appear in the Bokeh county data for Illinois but not the
# snowmobile spreadsheet from Illinois.gov:
# for key in county_names:
#     if key not in county_snowmobiles.keys():
#         print(key)

# Get the counties from the snowmobile spreadsheet that do not appear in the Bokeh
# county data:
# for key in county_snowmobiles.keys():
#     if key not in county_names:
#         print(key)

# We need to rename the counties from the snowmobile spreadsheet that were
# misspelled:
county_snowmobiles['DE WITT'] = county_snowmobiles.pop('DEWITT')
county_snowmobiles['GREENE'] = county_snowmobiles.pop('GREEENE')
county_snowmobiles['JO DAVIESS'] = county_snowmobiles.pop('JODAVIS')
county_snowmobiles['ROCK ISLAND'] = county_snowmobiles.pop('ROCKISLAND')
county_snowmobiles['ST. CLAIR'] = county_snowmobiles.pop('STCLAIR')

# Look at this again to see which counties are still missing from county_snowmobiles:
# for key in county_names:
#     if key not in county_snowmobiles.keys():
#         print(key)

# We need to fill in values of zero for any
# counties in Illinois that don't have a snowmobile registered:
for key in county_names:
    if key not in county_snowmobiles.keys():
        county_snowmobiles[key] = 0

# len(county_snowmobiles) # 108; there should be 102, so these 6 need to be removed:
extras = []
for key in county_snowmobiles.keys():
    if key not in county_names:
        extras.append(key)
# extras

for state in extras:
    del county_snowmobiles[state]

# len(county_snowmobiles) # 102. Success!











# county_snowmobiles
# counties
# counties.values()

# Get the county name from counties
# for county_id in counties.values():
#     print(county_id['name'])

# [county_snowmobiles[county['name'].upper()] for county in counties.values()]

# We need to have a county_id and corresponing rate so that we can have the
# number of vehicles for each county county_vehicles) in the same order as the
# counties themselves (from Bokeh data):

county_vehicles = [county_snowmobiles[county['name'].upper()] for county in counties.values()]
# county_vehicles # List of values

# len(county_vehicles) # 102. Booyah!!










# Constructing the plot:

color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    count=county_vehicles
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Illinois snowmobile registrations", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Snowmobile count", "@count"), ("(Long, Lat)", "($x, $y)")
    ])

p.grid.grid_line_color = None

p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'count', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)


show(p)




# Save plot as HTML file:
from bokeh.plotting import figure, output_file, save
output_file("Illinois snowmobiles.html")
save(p)


# Delete the plot when finished or rendering a second time:
del p







dir()
globals()
locals()
