#week 4 hw 1 whiskies
Exercise 1
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

In this exercise, we provide a basic demonstration of an interactive grid plot using Bokeh. Make sure to study this code now, as we will edit similar code in the exercises that follow.

INSTRUCTIONS
100 XP
Execute the following code and follow along with the comments. We will later adapt this code to plot the correlations among distillery flavor profiles as well as plot a geographical map of distilleries colored by region and flavor profile.
Once you have plotted the code, hover, click, and drag your cursor on the plot to interact with it. Additionally, explore the icons in the top-right corner of the plot for more interactive options!
Take Hint (-30 XP)


Exercise 2
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

In this exercise, we will create the names and colors we will use to plot the correlation matrix of whisky flavors. Later, we will also use these colors to plot each distillery geographically.

INSTRUCTIONS
100 XP
Create a dictionary region_colors with regions as keys and cluster_colors as values.
Print region_colors.
Take Hint (-30 XP)
SCRIPT.PY

Exercise 3
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

correlations is a two-dimensional np.array with both rows and columns corresponding to distilleries and elements corresponding to the flavor correlation of each row/column pair. In this exercise, we will define a list correlation_colors, with string values corresponding to colors to be used to plot each distillery pair. Low correlations among distillery pairs will be white, high correlations will be a distinct group color if the distilleries from the same group, and gray otherwise.

INSTRUCTIONS
100 XP
INSTRUCTIONS
100 XP
Edit the code to define correlation_colors for each distillery pair to have input 'white' if their correlation is less than 0.7.
whisky is a pandas dataframe, and Group is a column consisting of distillery group memberships. For distillery pairs with correlation greater than 0.7, if they share the same whisky group, use the corresponding color from cluster_colors. Otherwise, the correlation_colors value for that distillery pair will be defined as 'lightgray'.
Take Hint (-30 XP)
SCRIPT.PY

   
Exercise 4
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

In this exercise, we will edit the given code to make an interactive grid of the correlations among distillery pairs based on the quantities found in previous exercises. Most plotting specifications are made by editing ColumnDataSource, a bokeh structure used for defining interactive plotting inputs. The rest of the plotting code is already complete.

INSTRUCTIONS
100 XP
INSTRUCTIONS
100 XP
correlation_colors is a list of string colors for each pair of distilleries. Set this as color in ColumnDataSource.
Define correlations in source using correlations from the previous exercise. To convert correlations from a np.array to a list, use the flatten() method. This correlation coefficient will be used to define both the color transparency as well as the hover text for each square.

Exercise 5
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

In this exercise, we give a demonstration of plotting geographic points.

INSTRUCTIONS
100 XP
Run the following code, to be adapted in the next section. Compare this code to that used in plotting the distillery correlations.
Take Hint (-30 XP)
SCRIPT.PY


Exercise 6
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

In this exercise, we will define a function location_plot(title, colors) that takes a string title and a list of colors corresponding to each distillery and outputs a Bokeh plot of each distillery by latitude and longitude. It will also display the distillery name, latitude, and longitude as hover text.

INSTRUCTIONS
100 XP
Adapt the given code beginning with the first comment and ending with show(fig) to create the function location_plot(), as described above.
Region is a column of in the pandas dataframe whisky, containing the regional group membership for each distillery. Make a list consisting of the value of region_colors for each distillery, and store this list as region_cols.
Use location_plot to plot each distillery, colored by its regional grouping.
Take Hint (-30 XP)
SCRIPT.PY


Exercise 7
In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple and interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

location_plot remains stored from the previous exercise. In this exercise, we will use this function to plot each distillery, colored by region and taste coclustering classification, respectively.

INSTRUCTIONS
100 XP
Create the list region_cols consisting of the color in region_colors that corresponds to each whisky in whisky.Region.
Similarly, create a list classification_cols consisting of the color in cluster_colors that corresponds to each cluster membership in whisky.Group.
Create two interactive plots of distilleries, one using region_cols and the other with colors defined by called classification_cols. How well do the coclustering groupings match the regional groupings?
Take Hint (-30 XP)
SCRIPT.PY


  
IPYTHON SHELL


  
