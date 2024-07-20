# Load necessary libraries
library(ggplot2)
library(readr)

# Define the list of criteria
criteria <- c('service', 'cleanliness', 'overall', 'value', 'location', 'sleep_quality', 'rooms')

# Function to create bar chart for each criterion
create_bar_chart <- function(criterion) {
  # Read the CSV file
  data <- read_csv(paste0(criterion, "_ratings.csv"))
  
  # Create bar chart
  ggplot(data, aes(x = Hotel, y = Average_Rating)) +
    geom_bar(stat = "identity", fill = "skyblue") +
    labs(title = paste("Average", criterion, "Rating per Hotel"), x = "Hotel Name", y = "Average Rating") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

# Iterate over each criterion and create bar chart
for (criterion in criteria) {
  plot <- create_bar_chart(criterion)
  print(plot)
}
