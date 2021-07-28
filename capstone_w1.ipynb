# Capstone Project - Week 1 #

## Problem ##
Locate candidate locations for opening a cafe within a specified square area (this example: Oxford Circus, London, UK)

### Hypothesis ###
Within large city centres it is beneficial to open coffee shops far from other cafes (far in a local sense)

### Plan ###
- identify existing coffee shop density within a grid bounded by the specified area
- calculate a per grid cell metric reflecting an inversion of this density
- metric should also take into account immediately adjacent grid cells
- high values of this metric reflect a local relative absence of coffee shops
- filter data to include only the highest 3 values of this metric
- investigate if areas of low coffee shop density show clustering characteristics
    - use elbow method to determine optimum number of clusters for k-means algorithm
- display most promising candidate clusters for opening a new coffee shop


### Data
- Existing coffee shop locations will be obtained by the foursquare explore API
- we consider a $1km^2$ area of a city centre (London) split into a 10x10 grid
    * square area is a square of side length $r=\frac{1000}{2}$
    * each grid cell has a length of $\Delta=\frac{1000}{10}$
- we query a slightly larger area than this to allow a per grid cell metric calculation taking into account adjacent cells
    * metric <- $ n_{cafes} + \frac{1}{4} * \Sigma\left( n_{adjacent_cafes}\right) $
- to include adjacent cell information the query radius (used in the foursquare API call) will be
    * $\sqrt(2)*\left(r+\Delta\right)$
- to map from grid cells to latitude/longitude we use the  __[Haversine method](http://url)__
    * assume radius of the Earth to be 6371km
