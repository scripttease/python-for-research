# First, we import a tool to allow text to pop up on a plot when the cursor
# hovers over it.  Also, we import a data structure used to store arguments
# of what to plot in Bokeh.  Finally, we will use numpy for this section as well!

from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Let's plot a simple 5x5 grid of squares, alternating in color as red and blue.

plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# How do we tell Bokeh to plot each point in a grid?  Let's use a function that
# finds each combination of values from 1-5.
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)

# The first value is the x coordinate, and the second value is the y coordinate.
# Let's store these in separate lists.

xs, ys = zip(*grid)
print(xs)
print(ys)

# Now we will make a list of colors, alternating between red and blue.

colors = [plot_colors[i%2] for i in range(len(grid))]
print(colors)

# Finally, let's determine the strength of transparency (alpha) for each point,
# where 0 is completely transparent.

alphas = np.linspace(0, 1, len(grid))

# Bokeh likes each of these to be stored in a special dataframe, called
# ColumnDataSource.  Let's store our coordinates, colors, and alpha values.

source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)
# We are ready to make our interactive Bokeh plot!

output_file("Basic_Example.html", title="Basic Example")
fig = figure(tools="resize, hover, save")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }
show(fig)

### my answer ###
# first pip install bokeh
from bokeh.models import HoverTool, ColumnDataSource
import numpy as np
plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# finds each combination of values
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)
#[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]


# zip * is like unzip!
xs, ys = zip(*grid)
print(xs)
print(ys)

#this is a way of alternating the red and blue for the length of the grid see example in comment below
colors = [plot_colors[i%2] for i in range(len(grid))]
print(colors)

# In [11]: plot_colors[0]
# Out[11]: 'red'

# In [12]: plot_colors[1]
# Out[12]: 'blue'

# In [13]: plot_colors[2%2]
# Out[13]: 'red'

# In [14]: plot_colors[3%2]
# Out[14]: 'blue'

# now imagine that we want a range of transparencies (alphas) from 0 to 1
alphas = np.linspace(0, 1, len(grid))
# array([0.        , 0.04166667, 0.08333333, 0.125     , 0.16666667,
#        0.20833333, 0.25      , 0.29166667, 0.33333333, 0.375     ,
#        0.41666667, 0.45833333, 0.5       , 0.54166667, 0.58333333,
#        0.625     , 0.66666667, 0.70833333, 0.75      , 0.79166667,
#        0.83333333, 0.875     , 0.91666667, 0.95833333, 1.        ])


# to make a bokeh dataframe with colors, transparencies as well as x and y coordinates the format is as follows;
source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)

# and this is all the junk ypu need to plot it!
output_file("Basic_Example.html", title="Basic Example")
fig = figure(tools="hover, save")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }

# above will only work with:
from bokeh.plotting import figure, output_file, show
# required for 

# Exercise 2

cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = dict(zip(region_colors, cluster_colors))
In [36]: print(region_colors)
{'Speyside': 'red', 'Highlands': 'orange', 'Lowlands': 'green', 'Islands': 'blue', 'Campbelltown': 'purple', 'Islay': 'gray'}

#Exercise 3
distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[j][i] <0.7:
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if whisky['Group'][i] == whisky['Group'][j]:
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.

                
# exercise 4
source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": ## ENTER CODE HERE! ##,
        "correlations": ## ENTER CODE HERE! ##,
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(title="Whisky Correlations",
    x_axis_location="above", tools="resize,hover,save",
    x_range=list(reversed(distilleries)), y_range=distilleries)
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3

fig.rect('x', 'y', .9, .9, source=source,
     color='colors', alpha='correlations')
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}
show(fig)

# exercise 4
# needs the following:
distilleries = ['Tullibardine', 'GlenElgin', 'GlenDeveronMacduff', 'GlenSpey', 'Glenfiddich', 'Glenkinchie' 'Glenlivet', 'Inchgower', 'Bowmore', 'GlenGarioch', 'Bladnoch', 'Linkwood' 'Benriach', 'GlenOrd', 'Speyburn', 'Belvenie', 'Tomintoul', 'RoyalBrackla', 'Teaninich', 'ArranIsleOf', 'GlenScotia', 'Isle of Jura', 'Bruichladdich' 'OldPulteney', 'Oban', 'Glenturret', 'Glenrothes', 'Mortlach', 'RoyalLochnagar', 'Springbank', 'Glenfarclas', 'Glendullan', 'Tormore', 'Tomatin', 'Highland Park', 'Macallan', 'Glendronach', 'Auchroisk', 'Aberlour', 'Balmenach', 'Deanston', 'GlenKeith', 'Dalmore', 'Dailuaine', 'Balblair', 'Strathmill', 'Loch Lomond', 'Tamnavulin', 'Bunnahabhain', 'Auchentoshan', 'Cardhu', 'GlenMoray', 'Glenmorangie', 'AnCnoc', 'Dufftown', 'Glenallachie', 'Tobermory', 'Dalwhinnie', 'Craigganmore', 'Craigallechie', 'Glenlossie', 'Laphroig' 'Clynelish', 'Talisker', 'Ardbeg', 'Lagavulin', 'Caol Ila', 'Tamdhu', 'Strathisla', 'Ardmore', 'Speyside', 'Longmorn', 'Aultmore', 'OldFettercairn' 'BenNevis', 'Miltonduff', 'Mannochmore' 'Benrinnes', 'Benromach', 'Knochando', 'BlairAthol', 'Glengoyne', 'Edradour', 'GlenGrant', 'Scapa', 'Aberfeldy'] 

In [10]: 
source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "correlations": correlations.flatten(),
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(title="Whisky Correlations",
    x_axis_location="above", tools="resize,hover,save",
    x_range=list(reversed(distilleries)), y_range=distilleries)
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3

fig.rect('x', 'y', .9, .9, source=source,
     color='colors', alpha='correlations')
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}
show(fig)

#exercise 5
points = [(0,0), (1,2), (3,1)]
xs, ys = zip(*points)
colors = ["red", "blue", "green"]

output_file("Spatial_Example.html", title="Regional Example")
location_source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
    }
)

fig = figure(title = "Title",
    x_axis_location = "above", tools="resize, hover, save")
fig.plot_width  = 300
fig.plot_height = 380
fig.circle("x", "y", 10, 10, size=10, source=location_source,
     color='colors', line_color = None)

hover = fig.select(dict(type = HoverTool))
hover.tooltips = {
    "Location": "(@x, @y)"
}
show(fig)

#Exercise 6

def location_plot(title, colors):
    output_file(title+".html")
    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title = title,
        x_axis_location = "above", tools="resize, hover, save")
    fig.plot_width  = 400
    fig.plot_height = 500
    fig.circle("x", "y", 10, 10, size=9, source=location_source,
    color='colors', line_color = None)
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type = HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }
    return show(fig)

region_cols = [region_colors[region] for region in whisky.Region]

location_plot("Whisky Locations and Regions", region_cols)


#Exercise 7
region_cols = [region_colors[region] for region in whisky.Region]

classification_cols = [cluster_colors[cluster] for cluster in whisky.Group]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)

# from discussion:
# I found that the tools option can be replaced with tools="pan, box_zoom, wheel_zoom, save, reset, hover" to show this functionality for the interactive plot
# to replace deprecated resize?
