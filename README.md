# Movierecoommender
Dowloaded the data set from, TMDB dataset on kaggle
Cleaned the data , discarding,data from crew, actors, movie date, etc etc
dropped, missing values ,duplicate data'
then imported ast library to convert string of list to list of strings,applied that to columns
extracted first 3 actors in the movie, 
then created a tag column ,combining all the columns, this is how i get a list of words identified as tags for my movie.
This is a content based movie recommender, hence using words to recommend.
created a vectors for count of different words, took 5000 words, as the number of wrods, ignorning stop words, using scikit learn,sklearn.feature_extraction.text import CountVectorizer
used the cosine simmliarity for comparing two movies
then rest is deployment, used streamlit, to process API calls from TMDB, then, deployed using Heroku.
