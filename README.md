# cs225-final-viz

## Visualization of CS225 Website Based off our scrapper

This is a visualization of the structure of the CS225 Website for the Fall 2021 semester. This is implemented using d3.js's directed force graph.

This visualization exculdes all parts of the site that are doxygen, except for the main link from the central website. This is due to the fact that if doxygen sites were include, more than 1 million edges would need to render and from testing, rendering the page once took more than 30 minute and in excess of 34GB of RAM, so for feasibility they are not inlcuded.

To get this visualization to work with the raw scrapped data, a parser and converter was written to transfrom the raw data files to json. 

In the visualization, the colors of vertices in the graph represent the top two paths on a url after `/cs225/fa2021/`.

To run this visualization locally run these commands in the following order:
~~~
npm ci
npm run build
npm run preview
~~~
