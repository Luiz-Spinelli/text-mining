# Imports

"""
I will begin by installing the required packages.
"""
from tracemalloc import stop
from imdb import Cinemagoer
import imdb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


"""
The purpose of this section is search for ID's of three of the best movies in their respective genre (Top Gun: Maverick - action; Ticket to Paradise - romantic comedy; Death on the nile - drama/suspense)
and then compile of the reviews, using their respective movie ID's. 
"""

# create an instance of the Cinemagoer class
ia = imdb.Cinemagoer()

movie_1_name = "Top Gun: Maverick"
movie_2_name = "Ticket to Paradise"
movie_3_name = "Death on the nile"

# # search movie in IMDB database
# movie_1 = ia.search_movie(movie_1_name)[0]
# movie_2 = ia.search_movie(movie_2_name)[0]
# movie_3 = ia.search_movie(movie_3_name)[0]


# printing movies IDs

# print(movie_1.movieID)
# print(movie_2.movieID)
# print(movie_3.movieID)

# movie_1_id = movie_1.movieID    # ID1 = 1745960
# movie_2_id = movie_2.movieID    # ID2 = 14109724
# movie_3_id = movie_3.movieID    # ID3 = 7657566

## or 

movie_1_id = '1745960'   
movie_2_id = '14109724'    
movie_3_id = '7657566'    



# # Getting reviews of Top Gun, Ticket to Paradise, and Death on the Nile- while searching for movied ID
movie_1_review = ia.get_movie_reviews('1745960')
# print(movie_1_review['data']['reviews'][0]['content'])
# movie_2_review = ia.get_movie_reviews('14109724')
# print(movie_2_review['data']['reviews'][0]['content'])
# movie_3_review = ia.get_movie_reviews('7657566')
# print(movie_3_review['data']['reviews'][0]['content'])

"""
Next, i will create a list of the top 20 reviews of each movie.

"""
def list_of_all_reviews(movie_id,number_reviews):
    list_results = []
    each_movie_reviews = ia.get_movie_reviews(movie_id)


    ## this iteration will append the first 20 movie reviews of each movie
    for i in range(number_reviews):
        list_results.append(each_movie_reviews['data']['reviews'][i]['content'])
    return list_results

## The functions below will get the 20 reviews of each movie and will make a txt file for each movie (with list_of_all_reviews)

m1_list_of_all_reviews = list_of_all_reviews(movie_1_id, 20)
with open('data/M1reviews.txt', 'w') as f: 
    for review in m1_list_of_all_reviews:
        f.write("%s\n" % review)


m2_list_of_all_reviews = list_of_all_reviews(movie_2_id, 20)
with open('data/M2reviews.txt', 'w') as f: 
    for review in m2_list_of_all_reviews:
        f.write("%s\n" % review)

m3_list_of_all_reviews = list_of_all_reviews(movie_3_id, 20)
with open('data/M3reviews.txt', 'w') as f: 
    for review in m3_list_of_all_reviews:
        f.write("%s\n" % review)


"""
Now, I attempt to take out the common stop words out of each movie's list of 20 reviews. 
And assign the new_words list to the next dictionary function which counts the most frequency of the words in the cleaned of stop words list. 
"""

sw_nltk = stopwords.words('english')
# print(sw_nltk)


"""
In order to count the frequency of each word I will create a function that converts the list of words of reviews into a dictionary

"""
def d(all_reviews):
    """
    This function returns words and frequencies in a dictonary, from each movie list of all reviews txt file - after removing the list of stopwords from each.  

    """
    result = {}

    fp = open(all_reviews)

    for line in fp:
        for word in line.split():
            word = word.lower() 
            if word not in sw_nltk:
                result[word] = result.get(word, 0) + 1
            else:
                continue

    return result

m1_dictionary = d('data/M1reviews.txt')
m2_dictionary = d('data/M2reviews.txt')
m3_dictionary = d('data/M3reviews.txt')

# print(m1_dictionary)
# print(m2_dictionary)
# print(m3_dictionary)

"""
After converting each movie's list of all reviews text file into a dictionary, with the key = word and value= frequency of the word, I decided to sort that dictionary. 
To sort the dictonary of words from high to low word frequency, I decided to use the sorted function and assign the result to a new variable (sorted_M#_dict)
"""

sorted_M1_dict = sorted(m1_dictionary, key = m1_dictionary.get , reverse = True)
print(sorted_M1_dict)

print("/n")
print("Sorted dictionary 2/n")

sorted_M2_dict = sorted(m2_dictionary, key = m2_dictionary.get , reverse = True)
print(sorted_M2_dict)

print("Sorted dictionary 3/n")
sorted_M3_dict = sorted(m3_dictionary, key = m3_dictionary.get , reverse = True)
print(sorted_M3_dict)



"""
Laslty, for the sentiment analysis: I decided to use natural language processing to gauge the 'coumpound' mood for each movie's review. Therefore, for each movie it would have 20 compound scores. 
To do that I created a function called f(list_reviews) and applied for all 3 movies.
"""



def f(list_reviews):
    """
    This fuction look at each review, applies the Sentiment analysis giving a 'compound' score, and append each score into a list called scores[]
    """
    scores = []
    for review in list_reviews:
        score = SentimentIntensityAnalyzer().polarity_scores(review)
        scores.append(score['compound'])

    return scores

# print(f(m1_list_of_all_reviews))
# print(f(m2_list_of_all_reviews))
# print(f(m3_list_of_all_reviews))


def main():
    print(movie_1_name) 
    print(movie_2_name) 
    print(movie_3_name) 


    print(movie_1_id) 
    print(movie_2_id)   
    print(movie_3_id)   

    m1_list_of_all_reviews = list_of_all_reviews(movie_1_id, 20)
    m2_list_of_all_reviews = list_of_all_reviews(movie_2_id, 20)
    m3_list_of_all_reviews = list_of_all_reviews(movie_3_id, 20)

    m1_dictionary 
    m2_dictionary 
    m3_dictionary 

    print(sorted_M1_dict) 
    print(sorted_M2_dict)
    print(sorted_M3_dict) 
    
    print(f(m1_list_of_all_reviews))
    print(f(m2_list_of_all_reviews))
    print(f(m3_list_of_all_reviews))

# if __name__ == "__main__":
#     main()