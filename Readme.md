# Rest api

uses flask on python

getting requests for info on users and such

GET SPECIFIC USER BY ID :
```
curl --header "Content-Type: application/json" --request GET "http://<host>/?id=<THE USER ID>"
```

GET SPECIFIC USER BY EMAIL :
```
curl --header "Content-Type: application/json" --request GET "http://<host>/?email=<THE USER email>"
```

POST-CREAT NEW USER BY ID : 
```
curl --header "Content-Type: application/json" --request POST  --data '[<LIST OF KEY AND VALUE OBJECTS FOR EACH NOT NULL COLUMN IN THE TABLE, SEPERATE OBJECT FOR EVERY FIELD> SUCH AS:{"key":"name","value":"Bob"})]' "<host>/?id=<THE USER id>"
```

PUT-UPDATE USER DATA:
```
curl --header "Content-Type: application/json" --request PUT  --data '[<LIST OF KEY AND VALUE OBJECTS FOR EACH FIELD THAT UPDATED (SEPERATE OBJECT FOR EVERY FIELD)> SUCH AS:{"key":"name","value":"Alice"})]' "http://<host>/?id=<THE USER id>
```

DELETE USER (TOGGLE ACTIVATION FIELD IN DATABASE TO 0):
```
curl --header "Content-Type: application/json" --request DELETE "http://<host>/?id=<THE USER ID>"
```
