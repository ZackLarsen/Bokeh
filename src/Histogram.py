


import scipy.special
from bokeh.layouts import gridplot
from bokeh.models import HoverTool



def make_plot(title, hist, x, pdf, cdf):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend="PDF")
    p.line(x, cdf, line_color="orange", line_width=2, alpha=0.7, legend="CDF")

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'Pr(x)'
    p.grid.grid_line_color="white"
    return p





# Delete before trying again:
del p1, p2
# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm histogram.html
ls





# Normal Distribution
mu, sigma = 0, 0.5
measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=50)

x = np.linspace(-2, 2, 1000)
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2

p1 = make_plot("Normal Distribution (μ=0, σ=0.5)", hist, x, pdf, cdf)


# Log-Normal Distribution
mu, sigma = 0, 0.5
measured = np.random.lognormal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=50)

x = np.linspace(0.0001, 8.0, 1000)
pdf = 1/(x* sigma * np.sqrt(2*np.pi)) * np.exp(-(np.log(x)-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((np.log(x)-mu)/(np.sqrt(2)*sigma)))/2

p2 = make_plot("Log Normal Distribution (μ=0, σ=0.5)", hist, x, pdf, cdf)



output_file('histogram.html', title="histogram.py example")

show(gridplot([p1,p2], ncols=2, plot_width=400, plot_height=400, toolbar_location=None))





















# Reset the output so we only see one plot in the browser:
reset_output()
# Delete the previous HTML file:
rm histogram_no_cdf.html





def make_plot_no_cdf(title, hist, x, pdf):
    TOOLS = "hover,pan,reset,save"
    p = figure(title=title, tools=TOOLS, background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5, hover_fill_color="firebrick")
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend="PDF")

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'Pr(x)'
    p.grid.grid_line_color="white"
    return p


# Normal Distribution
mu, sigma = 0, 0.5
measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=50)

x = np.linspace(-2, 2, 1000)
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))


edges
pdf




p3 = make_plot_no_cdf("Normal Distribution (μ=0, σ=0.5)", hist, x, pdf)



hover = p3.select(dict(type=HoverTool))
hover.tooltips = [('X value:',' $x')]




# Set autohide to true to only show the toolbar when mouse is over plot
#p3.toolbar.autohide = True

output_file('histogram_no_cdf.html', title="histogram.py example")

show(p3)




