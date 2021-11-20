import credentials 


db = credentials.firebase.database()

data={'age':33, 'name':'Rushikesh' , 'surname':'Ahire' }
db.push(data)

