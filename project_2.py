import nltk  
nltk.download('movie_reviews')  
from nltk.corpus import movie_reviews  
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
import string  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.naive_bayes import MultinomialNB  
import random  
import tkinter as tk  
  
def preprocess_text(text):  
   # Tokenize the text into individual words  
   tokens = word_tokenize(text.lower())  
   # Remove stopwords and punctuation  
   stop_words = set(stopwords.words('english') + list(string.punctuation))  
   filtered_tokens = [token for token in tokens if token not in stop_words]  
   # Return the filtered tokens as a string  
   return ''.join(filtered_tokens)  
  
# Create a CountVectorizer object to extract features  
vectorizer = CountVectorizer()  
  
# Fit the vectorizer to the preprocessed text corpus  
corpus = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]  
vectorizer.fit_transform([preprocess_text(text) for text in corpus])  
  
# Create a list of (preprocessed text, category) tuples  
corpus = [(preprocess_text(movie_reviews.raw(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]  
  
# Shuffle the corpus to ensure a random distribution  
random.shuffle(corpus)  
  
# Split the corpus into features and labels  
texts, labels = zip(*corpus)  
  
# Train a Multinomial Naive Bayes classifier  
X = vectorizer.fit_transform(texts)  
clf = MultinomialNB()  
clf.fit(X, labels)  
  
def generate_response(user_input):  
   # Preprocess and tokenize the user input  
   preprocessed_input = preprocess_text(user_input)  
   input_vector = vectorizer.transform([preprocessed_input])  
   # Use the classifier to predict a response  
   predicted_category = clf.predict(input_vector)  
   # Choose a random movie review from the predicted category  
   reviews_in_category = movie_reviews.fileids(predicted_category)  
   review_id = random.choice(reviews_in_category)  
   review_text = movie_reviews.raw(review_id)  
   # Return the review text as the chatbot response  
   return review_text  
  
class ChatbotGUI:  
   def __init__(self, master):  
      self.master = master  
      self.master.title("Movie Review Chatbot")  
      self.master.geometry("400x300")  
      self.input_field = tk.Text(self.master, height=10, width=40)  
      self.input_field.pack()  
      self.send_button = tk.Button(self.master, text="Send", command=self.send_message)  
      self.send_button.pack()  
      self.response_field = tk.Text(self.master, height=10, width=40)  
      self.response_field.pack()  
  
   def send_message(self):  
      user_input = self.input_field.get("1.0", "end-1c")  
      response = generate_response(user_input)  
      self.response_field.insert("1.0", response)  
  
root = tk.Tk()  
my_gui = ChatbotGUI(root)  
root.mainloop()
print("hi!how can i help you")