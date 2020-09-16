#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install nltk


# In[2]:


import nltk 


# In[3]:


nltk.download('punkt')


# In[4]:


from nltk.tokenize import sent_tokenize
text=" Welcome readers. I hope you find it interesting. Please do reply."
sent_tokenize(text)


# In[5]:


tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text=" Welcome readers. I hope you find it interesting. Please do reply."
tokenizer.tokenize(text)


# In[6]:


from nltk.tokenize import sent_tokenize
Arabic_text="مرحبا بكم. نحن نتعلم اساسيات مبادئ استرجاع المعلومات."
tokenizer.tokenize(Arabic_text)


# In[7]:


text=nltk.word_tokenize("Welcome readers. I hope you find it interesting. Please do reply..»") 
print(text) 


# In[14]:


from nltk.tokenize import sent_tokenize
Arabic=input("Please write a text")
print (Arabic)


# In[15]:


tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
Arabic=nltk.word_tokenize(input("Please write a text"))
print (Arabic)


# In[16]:


from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w]+""\S+@\S+")
tokenizer.tokenize("Don't hesitate to ask questions or send to me your question to mohsarem@gmail.com") 


# In[17]:


text=[" It is a pleasant evening.","Guests, who came from US arrived at the venue","Food was tasty."]
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc) for doc in text]
print(tokenized_docs) 


# In[18]:


import re
import string
x=re.compile('[%s]' % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review:
        new_token = x.sub(u'',token)
        if not new_token == u'':
            new_review.append(new_token)
    tokenized_docs_no_punctuation.append(new_review)
print(tokenized_docs_no_punctuation) 


# In[27]:


Text= "NLTK allows you to convert Text into Lowercase and uppercase"
print(Text.lower())
print(Text.upper())


# In[31]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
words=["Don't",'hesitate','to','ask','questions']
[word for word in words if word not in stops] 


# In[34]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stops=set(stopwords.words('english'))
text = "Nick likes to play football, however he is not too fond of tennis."
words = word_tokenize(text)
[word for word in words  if word not in stops]


# In[22]:


print(stopwords.words('english'))


# In[35]:


print(stopwords.words('Arabic'))


# In[8]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stops=set(stopwords.words('english'))
file_content = open(r"C:\Users\USER\Desktop\aa.txt").read()
words = word_tokenize(file_content)
[word for word in words  if word not in stops]

