import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv("IMDB-Movie-Data.csv")

# Filter the DataFrame based on the rating and drop rows with missing genre information
filtered_data = data[(data["Rating"] >= 8.0) & (data["Genre"].notna())]

# Split the genres and count the occurrences
genre_count = {}
for genres in filtered_data["Genre"]:
    for genre in genres.split(","):
        genre_count[genre] = genre_count.get(genre, 0) + 1

# Convert the genre count dictionary to a DataFrame
genre_count_df = pd.DataFrame(list(genre_count.items()), columns=["Genre", "Count"])

# Sort the DataFrame by the count in descending order
sorted_genre_count = genre_count_df.sort_values(by="Count", ascending=False)

# Plot the bar chart
plt.figure(figsize=(10, 5))
plt.bar(sorted_genre_count["Genre"], sorted_genre_count["Count"])
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.title("Number of Movies with Rating 8.0 or Higher by Genre")
plt.xticks(rotation=45)
plt.savefig("top_genres.png")
plt.show()
