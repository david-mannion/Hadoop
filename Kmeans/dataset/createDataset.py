import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def text_preprocesser(data, fiton):  # fiton specifies what data to fit the pre processor on
    documents = pd.DataFrame(data['Review'])

    # removing numbers
    documents['Review'] = documents['Review'].str.replace(r'\d+', '')

    # Make the review data Lower case
    documents['Review'] = documents['Review'].str.lower()

    # Filtering out stop words
    vectorizer = CountVectorizer(stop_words='english')
    tokenize = vectorizer.build_tokenizer()
    documents['Review'] = documents['Review'].apply(tokenize)

    # Stemming the text data
    stemmer = SnowballStemmer('english')  # snowball stemmer is said to be better than PorterStemmer
    documents['Review'] = documents['Review'].apply(lambda x: [stemmer.stem(y) for y in x])

    # Lemmatizing the data
    lemmatizer = WordNetLemmatizer()
    documents['Review'] = documents['Review'].apply(lambda x: [lemmatizer.lemmatize(y, 'v') for y in x])
    documents['Review'] = documents['Review'].apply(lambda x: ' '.join([str(elm) for elm in x]))

    # Performing TfidfVectorization
    vectorizer = CountVectorizer(min_df=5,encoding='latin-1', stop_words='english')

    vectorizer = vectorizer.fit(fiton['Review'])
    X = vectorizer.transform(documents['Review'])

    df = pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names())
    return df

auto = pd.read_csv('Automotive_review_data.csv')
term_vec = text_preprocesser(auto,auto).values


from scipy.linalg import svd
U,s,VT = svd(term_vec)

def get_Sigma(A,s,n_elements = 2):
    Sigma = np.zeros((A.shape[0], A.shape[1]))
    # populate Sigma with n x n diagonal matrix
    Sigma[:A.shape[0], :A.shape[0]] = np.diag(s)
    # select
    Sigma = Sigma[:, :n_elements]
    return Sigma

from scipy.linalg import svd
U,s,VT = svd(term_vec)

X = np.matmul(U,get_Sigma(term_vec,s))
np.savetxt('C:/Users/david/Documents/Masters/COMP41110_Cloud_Computing/Project/Kmeans/MapReduce/dataset.txt',X,delimiter = ',',fmt='%f')

