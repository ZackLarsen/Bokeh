
# Boxplot example with Bokeh

from bokeh.plotting import figure, show, output_file, reset_output


os.getcwd()
os.chdir('/Users/zacklarsen/Desktop/Projects/Dataviz/Python')
os.listdir()

snowmobiles = pd.read_excel('hodnrtempboatssnowmastercurrentexcelfiles20181001snowactiveregistrations.xlsx')
snowmobiles.head()
snowmobiles.columns

# Just pull the three biggest counties for this:
snowmobiles = snowmobiles[snowmobiles['COUNTY'].isin(["COOK","DUPAGE","WILL"])]
snowmobiles.head()


df = snowmobiles[['COUNTY','Horsepower']]
df.head()



# find the quartiles and IQR for each category
groups = df.groupby('COUNTY')
q1 = groups.quantile(q=0.25)
q2 = groups.quantile(q=0.5)
q3 = groups.quantile(q=0.75)
iqr = q3 - q1
upper = q3 + 1.5*iqr
lower = q1 - 1.5*iqr





cats = df['COUNTY'].unique()

# find the outliers for each category
def outliers(group):
    cat = group.name
    return group[(group.Horsepower > upper.loc[cat]['Horsepower']) | (group.Horsepower < lower.loc[cat]['Horsepower'])]['Horsepower']
out = groups.apply(outliers).dropna()

# prepare outlier data for plotting, we need coordinates for every outlier.
if not out.empty:
    outx = []
    outy = []
    for keys in out.index:
        outx.append(keys[0])
        outy.append(out.loc[keys[0]].loc[keys[1]])

p = figure(tools="", background_fill_color="#efefef", x_range=cats, toolbar_location=None)

# if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
qmin = groups.quantile(q=0.00)
qmax = groups.quantile(q=1.00)
upper.Horsepower = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,'Horsepower']),upper.Horsepower)]
lower.Horsepower = [max([x,y]) for (x,y) in zip(list(qmin.loc[:,'Horsepower']),lower.Horsepower)]

# stems
p.segment(cats, upper.Horsepower, cats, q3.Horsepower, line_color="black")
p.segment(cats, lower.Horsepower, cats, q1.Horsepower, line_color="black")

# boxes
p.vbar(cats, 0.7, q2.Horsepower, q3.Horsepower, fill_color="#E08E79", line_color="black")
p.vbar(cats, 0.7, q1.Horsepower, q2.Horsepower, fill_color="#3B8686", line_color="black")

# whiskers (almost-0 height rects simpler than segments)
p.rect(cats, lower.Horsepower, 0.2, 0.01, line_color="black")
p.rect(cats, upper.Horsepower, 0.2, 0.01, line_color="black")

# outliers
if not out.empty:
    p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "white"
p.grid.grid_line_width = 2
p.xaxis.major_label_text_font_size="12pt"

output_file("boxplot.html", title="Boxplot.py example")

show(p)









# Delete before trying again:
del p
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm boxplot.html
ls