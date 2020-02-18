nameScore <- function(name) {
  fullname <- data.frame(name)
  fullname$name <- as.character(fullname$name)
  i <- gsub("(?<=[A-Z])[^A-Z]+", "", fullname$name, perl = TRUE)
  
  i1 <- strsplit(i, split = "")
  i2 <- unlist(i1, use.names = FALSE)
  alphabet <- c(LETTERS[1:26])
  l <- match(i2,alphabet)
  
  l1 <- as.list(l)
  nameScore <- l1[[1]]*10+l1[[2]]
}

#TEST
print(nameScore("Xiangyu Gao"))
