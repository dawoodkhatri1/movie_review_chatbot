# movie_review_chatbot

The code will run in pycharm and vs code.

# Explanation:

## **Importing necessary libraries and downloading the movie reviews dataset**

The code starts by importing the necessary libraries, including NLTK (Natural Language Toolkit) for NLP tasks, sklearn for machine learning, and tkinter for building a graphical user interface (GUI). The nltk.download('movie_reviews') line downloads the movie reviews dataset, which is a collection of movie reviews labeled as positive or negative.

## **Preprocessing the text data**

The preprocess_text function is defined to preprocess the text data. It takes a text input, tokenizes it into individual words, converts it to lowercase, removes stopwords (common words like "the", "and", etc. that do not carry much meaning), and removes punctuation. The preprocessed text is then returned as a string.

## **Creating a CountVectorizer object and fitting it to the preprocessed text corpus**

A CountVectorizer object is created to extract features from the preprocessed text data. The fit_transform method is used to fit the vectorizer to the preprocessed text corpus, which is a list of movie reviews.

## **Creating a list of (preprocessed text, category) tuples and shuffling the corpus**

A list of (preprocessed text, category) tuples is created, where each tuple contains a preprocessed movie review and its corresponding category (positive or negative). The corpus is then shuffled to ensure a random distribution of the data.

## **Splitting the corpus into features and labels and training a Multinomial Naive Bayes classifier**

The corpus is split into features (preprocessed text) and labels (categories). A Multinomial Naive Bayes classifier is trained on the features and labels using the fit method.

## **Defining the generate_response function**

The generate_response function takes a user input, preprocesses it, and uses the trained classifier to predict a response category. It then chooses a random movie review from the predicted category and returns the review text as the chatbot response.

## **Creating a GUI using tkinter**

A GUI is created using tkinter to interact with the chatbot. The GUI has a text input field, a send button, and a response field. When the send button is clicked, the send_message method is called, which gets the user input, generates a response using the generate_response function, and displays the response in the response field.

## **Running the GUI event loop**

The GUI event loop is started using the mainloop method, which waits for user input and updates the GUI accordingly.

The output will be like this:

![Capture](https://github.com/user-attachments/assets/3037ad25-1cc8-4026-ab3a-7a62f980f560)
