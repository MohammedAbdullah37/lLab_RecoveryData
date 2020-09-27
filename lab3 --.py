#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[39]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("[a-m]", txt)
print(x)


# In[40]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("\d", txt)
print(x)


# In[41]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("AL....di", txt)
print(x)


# In[42]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
        


# In[43]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("3700578$", txt)
if x:
  print("Yes, the string ends with 3700578")
else:
  print("No match")


# In[44]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")


# In[45]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("adx*", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[46]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("adi+", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[47]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("AL{1}", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[24]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall("Saadi|mohe", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[50]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall(r"\ba", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[55]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall(r"d\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[58]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall(r"\Bme", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[60]:


txt = "mohammed abdullih AL-Saadi 3700578"
x = re.findall(r"du\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[61]:


txt = "Regular expression is a sequence of character(s) mainly us ed to find and replace patterns in a string or file"
start = txt.find("Regular") 
end = txt.find("file") + + len("file")
substring = txt[start:end]
print(substring)


# In[62]:


replacement_patterns = [ (r'won\'t', 'will not'), (r'can\'t', 'can not'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'),(r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'), (r'(\w+)\'ve', '\g<1> have'),(r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'), (r'(\w+)\'d', '\g<1> would')]
class RegexReplacer(object):
  def __init__(self, patterns=replacement_patterns):
    self.patterns = [(re.compile(regex), repl) for (regex, repl)in patterns]
  def replace(self, text):
    s = text
    for (pattern, repl) in self.patterns:
      (s, count) = re.subn(pattern, repl, s)
    return s

a= RegexReplacer()
aaa="We'll see how to replace words using regu lar expressions such doesn't, can't and so on"
print(a.replace(aaa))


# In[63]:


class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3' 
    def replace(self, word):
        repl_word = self.repeat_regexp.sub(self.repl, word) 
        if repl_word != word:
            return self.replace(repl_word) 
        else:
            return repl_word

a= RepeatReplacer()
aaa = input("type :")
a.replace(aaa)

