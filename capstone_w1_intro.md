# Capstone Project - Week 1 #

## Problem ##
Locate candidate locations for opening a cafe within a specified square area (this example: Oxford Circus, London, UK)

## Target Audience ##
Entrepreneurs looking for opportunities to open a store in (relatively) quieter areas of a city center.  This example considers cafes and coffee shops and uses a particular metric to construct the candidate area list but both the category (cafe/coffee shop) and metric are simple to modify for other requirements.

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
