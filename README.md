# Zone Manager

## Purpose
This project allows the user to create, delete and get existing zones. A zone will contain an id, name and a list of 4 points 

example for a zone: 
```json
{
  "id": 1,
  "name": "zone 1",
  "points": [[12.3, 12.0], [16.3, 12.0], [16.3, 8.0], [11.4, 8.7]]
}
```

## Installation
the project is using flask which needs to be installed
```bash
pip install Flask
pip install flask-cors
```
