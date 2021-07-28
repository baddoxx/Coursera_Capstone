
# Capstone Project - Week 1 #

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
