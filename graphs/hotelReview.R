# Load necessary libraries
library(ggplot2)
library(readr)

# Read the CSV file
data <- read_csv("reviews_counts.csv")

# Create bar chart for positive reviews
ggplot(data, aes(x = name, y = Positive_Reviews)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(title = "Number of Positive Reviews per Hotel", x = "Hotel Name", y = "Number of Positive Reviews") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Create bar chart for negative reviews
ggplot(data, aes(x = name, y = Negative_Reviews)) +
  geom_bar(stat = "identity", fill = "red") +
  labs(title = "Number of Negative Reviews per Hotel", x = "Hotel Name", y = "Number of Negative Reviews") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
