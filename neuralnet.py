#import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
media=0
maior=0
debug=0

def exe():
        dataset=pd.read_csv('train.csv')
    	label=dataset.iloc[0:890,1] #separa o "survived" do dataset
    	data=dataset.iloc[0:890,[2,4,5]] #separa o "pclass" "sex" e "age" do dataset
    	x=[data]    
    	
    	for change in x:
    	    change['Sex']=change['Sex'].map({'female':0,'male':1}).astype(int)
    	    
    	mediaidade = 0
        
        
    	count=0
        for index, row in data.iterrows():
    	    if math.isnan(row["Age"]) == True:
                pass
            else:
    		mediaidade = mediaidade + row["Age"]
    		count = count+1
    		
    	    
    	mediaidade = mediaidade/count
    	mediaidade = math.ceil(mediaidade)
        
        #data=(data.fillna(0)) #filling NA values
        data=(data.fillna(mediaidade))
    	
    
        from sklearn.model_selection import train_test_split
    
        train_a,test_a,y_train,y_test=train_test_split(data,label,random_state=None,train_size=0.75)
    
        from sklearn.neural_network import MLPClassifier
        
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(21), random_state=None)
        
        clf.fit(train_a,y_train)
    
        predictions=clf.predict(test_a)
        #predictions = clf.predict_proba(test_a)
    
        from sklearn.metrics import accuracy_score
        if debug==0:
            print(accuracy_score(y_test,predictions))
           
        
        
        #result=clf.predict(test_a)
    
        #print(result)
        return(accuracy_score(y_test,predictions))
        
if debug==1:
    for x in range(0,50):
        new=exe()
        media = media + new
        if new > maior:
            maior = new
        
         
    media = media/50
    print("media: "+str(media))
    print("maior: "+str(maior))
    
else:
    exe()
