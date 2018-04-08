top_counts <- read.csv("/Users/beaubritain/downloads/top_edit_counts.csv")
head(top_counts)
library(ggplot2)
hist(top_counts$count)
mean(top_counts$count)
sd(top_counts$count)

qplot(top_counts$count, geom = "histogram", xlab = "number of edits", ylab = "count of articles", fill = I("lightblue"), col = I("black")) + theme_light()
