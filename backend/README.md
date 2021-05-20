# Cuemby Backend Test

The objective of this test is to build a replica of 
the API of the FIFA 21 Ultimate Team game that allows 
you to search for players and teams.

## Script 

We must create a script to extract the information from 
the dataset located in the FUT21 API and add it to a 
database to allow the query and modification of data 
stored there.

The following databases are allowed: 

- Postgresql 
- MariaDB 
- MySQL 
- MongoDB

API URL: `https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1`

The players are in the response in the items field, of these 
it is interesting to store the name of the player, the 
position in which he plays, his nationality and the name of 
the team to which he belongs. Additionally, it must iterate up 
to the page number that the endpoint response returns and 
save the players in the database.

## API REST

Build a microservice that exposes the following endpoints 
through the REST API:

### POST `/api/v1/team`

Gets the players of a team regardless of whether it is 
written in lowercase or uppercase.

- Request example:
```
[
  "Name": "real madrid",
  "Page": 1,
]
```

- Response example:
```
{
  "Page": 1,
  "totalPages": 2,
  "Items": 10,
  "totalItems": 20,
  "Players": [
    {"name": "Marcelo", "position": "LB", "nation": "Brazil"},
    ...
  ]
}
```

### GET `/api/v1/players`

Finds the players that contain the String in the player 
name fields, either a partial or total match, and regardless 
of whether it is uppercase or lowercase.

The order can be asc or desc and defines the order from the 
name alphabetically, by default it will be asc 
(if it is not received in the url)

- Request example: `/api/v1/players?search=cristi&order=asc&page=1`

- Response example:

```
{
  "Page": 1,
  "totalPages": 1,
  "Items": 10,
  "totalItems": 10,
  "Players": [
    {"name": "Cristiano Ronaldo", "position": "ST", "nation": "Portugal", "team": "Juventus"}
    ...
  ]
}
```

## Plus (*optional*)

We would love if you can also accomplish the following tasks in this project:

### Protect the API

Protect the endpoints with an x-api-key header that is loaded by 
environment variable when running the application.

### Docker

Create the Dockerfile of the application that allows its 
publication in a registry and a simple deployment of the 
application.
