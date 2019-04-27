library(ape)
library(jsonlite)

#  JSON -> Matrix
unpackMatrix = fromJSON

#  Matrix -> JSON
packMatrix = toJSON

random_distance_matrix <- function(n){
  cophenetic(rtree(n))
}
