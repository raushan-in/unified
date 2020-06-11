0. create new empty list 
1. convert the hotel name in lowercase and strip
2. get hotel name words list by removing common bussiness word
3. calculate distance between two location

4. if hotel name, lat, log 100 % match
     - append object into new list
     - remove object from second list
     - break

5. else if string list match and location is near by(500 meter)
     - append object into new list
     - remove from second list
     - break

6. else
     - append hotel in new list

7. append the remaing hotel of 2nd list in new list

8. return the new list

