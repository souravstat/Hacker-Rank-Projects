#Project Work In ISI Kolkata in Dec 2017
#Python 2 is used
import re
query = ['axe deo','best-seller books','calvin klein','camcorder','camera','chemistry','chromebook','c programming','data structures algorithms','dell laptops','dslr canon','mathematics','nike-deodrant','physics','sony cybershot','spoken english','timex watch','titan watch','tommy watch','written english']
train_data = []			
test_data = []			
train_y = []
index = -1
for line in open('training.txt'):  
        if index == -1:
            index = int(line.strip())
        else:
            tmp = re.split(r'\t+', line)            
            train_data.append(tmp[0])
            word = tmp[1].split('\n')
            
            train_y.append(query.index(word[0]))
#print train_data
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
count_vect = CountVectorizer(ngram_range = (1,1),max_df = 0.1)
tfidf_transformer = TfidfTransformer(use_idf=False)
X_train_counts = count_vect.fit_transform(train_data)	

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)



from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100,max_depth = None,random_state = 0)
clf = clf.fit(X_train_tfidf.toarray(), train_y)

#print clf.score(X_train_tfidf,train_y)
N = int(raw_input())
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+|[+]{2}")



test2 = []
for i in range(N):
    tm = raw_input()
    liness = tokenizer.tokenize(tm)
    test2.append(liness)
    test_data.append(tm)
X_new_counts = count_vect.transform(test_data)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)    
predicted = clf.predict(X_new_tfidf.toarray())
#print clf.predict_proba(X_new_tfidf)
for x in range(len(predicted)):
    tmp = [t.lower() for t in test2[x]]
    for y in query:
        flag = 1
        for z in y.split():            
            if z not in tmp:              
                flag = 0
                break
        if flag == 1:             
            print y
            break
           
#Print the results.
     