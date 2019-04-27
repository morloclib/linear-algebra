library(ape)

random_distance_matrix <- function(n){
  cophenetic(rtree(n))
}
