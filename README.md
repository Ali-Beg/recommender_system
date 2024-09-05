# 🎬 Movie Recommender System

This project is a **Collaborative-based Movie Recommender System** that uses data from the **TMDB (The Movie Database)** to suggest the top 5 similar movies based on the user's input. By leveraging **data preprocessing**, **Exploratory Data Analysis (EDA)**, and **cosine similarity** on vectorized movie data, the system provides personalized movie recommendations.

## 🧠 How It Works

### 1. **Data Collection**
The movie data is sourced from the TMDB dataset, which contains information on thousands of movies, including:
- Movie titles
- Genre
- Plot summaries
- Cast and crew
- User ratings, etc.

### 2. **Data Preprocessing**
Before building the recommendation system, the data undergoes cleaning and transformation:
- **Handling missing values:** Movies without essential data are removed.
- **Feature extraction:** Only relevant features like movie titles, genre, and overview are used.
- **Text normalization:** Stop words, punctuation, and special characters are removed to clean up textual data.

### 3. **Exploratory Data Analysis (EDA)**
Exploratory Data Analysis is performed to understand the data's structure and relationships. Visualizations are created to explore:
- Popular genres

### 4. **Vectorization**
Once the data is preprocessed, it is vectorized using techniques like:
- **BoW (bag of word)**: This converts textual movie data into vectors.
- **Cosine Similarity**: Measures the cosine of the angle between two vectors (in this case, two movies). Movies with the smallest angles (i.e., higher cosine similarity) are considered more similar.

### 5. **Cosine Similarity for Recommendations**
For a given movie query, the system compares it to all other movies using **cosine similarity**. It then returns the **top 5 most similar movies** based on the vector distances.

## 💻 Tech Stack

- **Python:** The core programming language used for development.
- **Pandas & NumPy:** Libraries for data manipulation and analysis.
- **Scikit-learn:** Used for vectorization and calculating cosine similarity.
- **Streamlit:** Frontend framework to create an interactive user interface.
- **Matplotlib & Seaborn:** Libraries for visualizations during EDA.
- **TMDB API:** Data source for movie metadata.

## 🛠️ Features

- **Search for Movies:** Users can search for any movie by title.
- **Top 5 Movie Recommendations:** The system recommends 5 movies most similar to the one searched.
- **Cosine Similarity:** Ensures high accuracy in finding similar movies.
- **User-friendly Interface:** Powered by Streamlit for a seamless experience.

## 🚀 How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ali-Beg/recommender_system/
   cd recommender_system
   ```

2. **Install Dependencies:**
   Install the required Python packages using the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Start the Streamlit application by running:
   ```bash
   streamlit run app.py
   ```

4. **Enter a Movie Name:**
   Use the search bar to input a movie title, and the system will return the top 5 similar movies.

## 🔧 Key Files

- `app.py`: The main application file.
- `similarity.pkl`: Precomputed similarity matrix for efficient recommendation.
- `README.md`: Documentation for the project.

## 📊 Example Outputs

1. **User Query: "Inception"**
   - Top 5 recommendations:
     - Interstellar
     - The Prestige
     - The Matrix
     - Shutter Island
     - Memento

2. **User Query: "The Avengers"**
   - Top 5 recommendations:
     - Iron Man 3
     - Captain America: The Winter Soldier
     - Guardians of the Galaxy
     - Thor: Ragnarok
     - Avengers: Age of Ultron

## 📈 Data Insights (EDA)

- **Popular Genres:** Action, Drama, Comedy, and Adventure dominate the dataset.

## 🤝 Contributions

Feel free to contribute to the project by opening issues and submitting pull requests. Your feedback is appreciated!
