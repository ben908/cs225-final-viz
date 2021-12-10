# cs225-final-viz

## Vizulaizatoin of CS225 Website Based off our scrapper

This exculdes all doxygen graphs except for the main link from the central website due to the fact that if they were include more than 5 million edges would need to render and from our attempt to do so, rendering the page once took more than 30 minute and in excess of 34GB of RAM, so for feasibility we are not ilcuding them in the visualization.

This visualization is done using d3's force graph. To get this to work with our data we had to write a converter from our raw data files to json. The colors on the graph represent the top two paths on a url after `/cs225/fa2021/`.