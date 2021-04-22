import pandas as pd
pd.set_option('display.max_colwidth', -1)

# Let's import and investigate the raw csv
jeopardy_data = pd.read_csv('jeopardy.csv')
#print(jeopardy_data.head())
#print(jeopardy_data.columns)

# There is an annoying space before the column name, let's get rid of that
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
# Check to make sure everything renamed correctly
#print(jeopardy_data.columns)

# Write a function that returns questions which contain "King" AND 'England
# How about we do this for any list of words?
def question_filter(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['Question'].apply(filter)]
questions = question_filter(jeopardy_data, ['King', 'England'])
#print(questions['Question'])

# The Value column is a string, this seems not good
# Convert Value column to floats from strings
jeopardy_data['Value_Float'] = jeopardy_data['Value'].apply(lambda x: float(x[1:].replace(',', '')) if x != 'None' else 0)
#print(jeopardy_data.Value_Float.head())

# How about we find questions that contain King?
questions_king = question_filter(jeopardy_data, ['king'])
#print(questions_king['Question'])
print(questions_king['Value_Float'].mean())

# How often are the answer to our King questions unique?
# Write a function that returns unique answers
def unique_answers_count(data):
  return data['Answer'].value_counts()

print(unique_answers_count(questions_king))