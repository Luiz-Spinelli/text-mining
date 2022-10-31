# text-mining

Please read the [instructions](instructions.md).

Project Overview: 
    The purpose of this project was to pick three great movies  ("Top Gun: Maverick" ,"Ticket to Paradise", and "Death on the Nile")of different categories (action/adventure, Romantic Comedy, and drama/suspense) and analyze both the most frequently used words and the sentiment analysis of the top 20 movies reviews. 
    Using text mining techniques characterizing by word frequencies and natural language processing, I was hoping to test the hyposthesis that romantic comedy would not only have the most positive reviews (accordign to sentiment analysis data) but also would have positive words (such as "loved", "amazing", "funny") as the most frequent out of all three films.
    The main data source I used for this project was IMDB database of movie reviews. 

Implementation:
    I decided to break this project into 3 major parts. The first part was pulling all the correct movie reviews from the IMDB database. To do that first part, I first took the particular nmae of each film ("Top Gun: Maverick" ,"Ticket to Paradise", and "Death on the Nile") and used it to get the id. Then, I used the id to get the list of the top 20 reviews for each film. I decided to assign each movie's 20 reviews into a list - for easier use of manipulation. In fact, because i used list (and not dictionary, at first) I was able to append reviews in new lines, and splice the words in each review to later count the most frequent words. 
    In the second part, I decided to convert the list of 20 reviews from each movie into a dictonary, so I was able to count the frequency of words in each list of all reviews, per movie. To do that dictonaries was the best choice, because I was able to make the word as the key and the frequency of each word as the value. This choice made it extremely easy to find the top 25 most frequent words in all top 20 reviews for each movie.
    In the last part, I decided to use sentiment analyses for each txt file with all top 20 reviews. And I decided the best choice would be to use a list, because I would need to manipulate the list (by appending a new item to the list after scoring each review/line).

Results: 

    Top Gun: Maverick 
        Top 50 words: 
        ['the', 'and', 'to', 'a', 'is', 'of', 'in', 'it', 'i', 'that', 'was', 'this', 'as', 'with', 'for', 'you', 'are', 'but', 'maverick', 'movie', 'on', 'his', 'first', 'top', '-', 'film', 'he', 'one', 'we', 'from', 'cruise', 'by', 'tom', 'be', "it's", 'original', 'so', 'action', 'also', 'not', 'has', 'an', 'all', 'had', 'my', 'there', 'see', 'have', 'new']

        Sentiment Analysis: 
        [0.9944, 0.9211, 0.9829, 0.9922, 0.5983, -0.7227, 0.9708, 0.9982, 0.91, 0.9976, 0.9952, 0.997, 0.9569, 0.9741, 0.9935, 0.9937, 0.9906, 0.9577, 0.9602, 0.9232]


        As expected the top 50 most frequent words of the top 20 reviews were commonly used words that connects words to form a sentence, such as ['the', 'and', 'to', 'a', 'is', 'of', 'in', 'it', 'i', 'that', 'was', 'this', 'as', 'with', 'for', 'you', 'are', 'but']. However, if we take that out, it was very interesting to see words such as 'first', 'top', 'cruise', 'original', 'great', and 'best' in the top 50 words. To start, out of the last 5 words written four are extremely positive, which show an indication of how much the audience like the movie. And that is in fact in accordance with reality, because this movie became the most sold movie of all tim (in gross value of tickets sold). Moreover, the word 'cruise' as one of the most frequent words speaks to the excellent job made by Tom Cruise, the leading actor. In fact, so much so that this movie's name and his name are almost a synonym. 

        The sentiment analysis is in accordance with the positivity words. In fact, the 15 out of the top 20 reviews had a score >= .95, which shows extreme positivity - since the range is from 0 to 1 & the closer to +1 being the extreme positive and the close to -1 being the most negative.  

    "Ticket to Paradise"
        Top (around) 100 words:
        ['the', 'and', 'a', 'to', 'of', 'i', 'is', 'in', 'it', 'that', 'was', 'this', 'with', 'not', 'but', 'on', 'movie', 'for', 'have', 'they', 'as', 'so', 'are', 'also', 'you', '-', 'about', 'like', 'or', 'when', 'their', 'even', 'all', 'clooney', 'by', 'how', 'he', 'her', 'if', 'be', 'film', 'julia', 'more', 'really', 'just', 'each', 'were', 'roberts', 'george', 'good','other', 'at', 'she', 'two', 'what', 'been', 'there', 'them', 'actors', 'we', 'only', 'one', 'which', 'his', "it's", 'could', 'here', 'maybe', 'romantic', 'see', 'very', 'has', 'up', 'do', 'much', 'will', 'make', 'had', 'then', 'daughter', 'would', "clooney's", 'character', 'together', 
        'great', 'no', 'made', 'love', 'me', 'an', 'who', 'get', 'why', 'did', 'from', 'funny']

        Sentiment Analysis:
        [0.9222, 0.9971, 0.9912, 0.9571, 0.9977, 0.9932, 0.9142, 0.9332, 0.9986, 0.9395, 0.9848, 0.7003, 0.9712, 0.952, 0.9282, 0.972, 0.8491, 0.9959, -0.9132, 0.8863]
    

        Again, as both expected and unfortunately the top 50 most frequent words of the top 20 reviews were commonly used words that connects words to form a sentence. However, following these common words are the very interesting words to analyze ['clooney','julia', 'roberts', 'george', 'romantic', 'love', 'funny']. These words have a very interesting because they indicate 3 important factors behind them. First, the actors are very cited which indicate people really noticed their performance. Combined with positive words such as 'funny', it show that customers really liked the movie, and (as intedend for any romantic commedy) particularly liked about the jokes and romance.

        The sentimental analysis of this film is good- showing alignemnt with the most frequent words. Out of the top 20 reviews, 11 had a score of >= 0.95. Which shows a moderate amount of extreme positivity. 
    
    "Death in the Nile"
        Top (around) 100 words:
        [the', 'and', 'a', 'of', 'is', 'in', 'to', 'this', 'with', 'it', 'but', 'on', 'i', 'was', 'that', 'are', 'an', 'just', 'film', 'not', 'for', 'or', 'from', 'characters', 'as', 'movie', 'be', 'by', 'like', 'at', 'no', 'has', 'branagh', 'even', 'all', "it's", 'her', 'she', 'out', 'christie', 'very', 'when', 'have', 'there', 'you', 'they', 'so', 'were', 'one', 'story', 'great', 'some', 'better', 'kenneth', 'about', 'more', 'many', 'poirot', 'much', 'actors', 'most', 'cgi', 'than', 'everything', 'nile', 'only', 'what', 'bad', 'script', 'boring', 'he', 'watch', 'make', 'version', 'felt', 'over', 'because', 'their', '1978', "don't", 'why', 'first', 'too', 'really', 'mystery', 'character', 'agatha', 'british', 'will', 'egypt', 'him', 'cast', 'murder', 'orient', 'performances', 'cinematography', 'effects']

        Sentiment Analysis:
        [0.8566, -0.8863, 0.2664, 0.1779, 0.7242, 0.8623, 0.9915, -0.6352, 0.7822, -0.5538, 0.9476, -0.66, 0.3818, -0.9328, -0.6874, 0.9413, 0.6357, 0.8577, -0.985, -0.8433]

        In this film, particularly, the words that seemed most interesting to me were that words of positivity ['great',' 'much'] were almost just as frequent as negative words ['bad', 'boring']. This is particularly shocking because a drama/suspense film that tries to investigate a murder it should be nothing but boring. In fact, while the romantic commedy had the wanted reaction (funny and romantic), this drama/suspense film did not. At least in first sight. 

        The sentimental analysit is in accordance with the most frequent words, in particular, the negative tonality words. Differently from the first two films, these film had the most amount of negative compound scores, approaching about 8 out of 20 being negative and 1 neutral. 


Conclusion: 
    To conclude, overall i think my decision to do IMDB movie reviews was a good choice. I learned that my hypothesis, that the most liked movie would be in the genre of romantic comedy, was completely wrong. In fact, Top Gun:Maverick (adventure/action) was by far the most liked movie out of all of them. 

    What went well: I think i choose the appropriated data types and was able to consistently test my functions (using the print function) to see whether my functions were correct or not. Morevoer, I did well in choosing word frequency and sentiment analysis because they were two complementary techniques in testing my hypothesis. 

    Challenges: Pulling movie reviews from the IMDB database was harder than I thought they would be. 

    Before I started, I wish I had taught to take out the most common words and stopping words out of the dictionary. That way, my most frequent word list for every top 20 movie review would have beeing cleaner and easier to analyze.  

        
