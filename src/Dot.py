

from bokeh.layouts import row
from bokeh.plotting import figure, show, output_file, reset_output


os.getcwd()
os.chdir('/Users/zacklarsen/Desktop/Projects/Dataviz/Python')
os.listdir()

snowmobiles = pd.read_excel('hodnrtempboatssnowmastercurrentexcelfiles20181001snowactiveregistrations.xlsx')
snowmobiles.head()


df = snowmobiles.groupby('COUNTY').Registration_Number.nunique().reset_index(name='counts')

df.sort_values(by="counts",ascending=False,inplace=True)
# Take top 10 only:
df = df[:10]

# Have to reverse the order to get high values on top of plot
df.sort_values(by="counts",ascending=True,inplace=True)

factors = df['COUNTY']
factors

x = list(df['counts'])
x









# Delete before trying again:
del dot
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm Dot.html
ls



data=dict(
    x=factors,
    y=x
)
TOOLS = "reset,hover,save"
dot = figure(title="Snowmobiles by county in Illinois",
             tools=TOOLS,
             y_range=factors, x_range=[0,3000],
             tooltips=[("Registered snowmobiles", "$x{int}")])
dot.hover.point_policy = "follow_mouse"
dot.segment(0, factors, x, factors, line_width=2, line_color="blue", )
dot.circle(x, factors, size=15, fill_color="red", line_color="blue", line_width=3)
output_file("Dot.html", title="Dot.py example")

show(dot)






# dot = figure(title="Snowmobiles by county in Illinois",
#              toolbar_location=None,
#              y_range=factors, x_range=[0,3000])
#
# dot.segment(0, factors, x, factors, line_width=2, line_color="blue", )
# dot.circle(x, factors, size=15, fill_color="red", line_color="blue", line_width=3, )
#
# output_file("Dot.html", title="Dot.py example")
#
# show(dot)
