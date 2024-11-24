# Noloco Technical Exercise: Bike Station

This is a backend service built using FastAPI that fetches the [Dublin Bikes dataset](https://app-media.noloco.app/noloco/dublin-bikes.json),deriving its schema and querying the data

## Tech Choices

- Main Tech: FastAPI (Python Framework thats great at creating fast and efficient APIs)

## Lessons Learned

What would I do if I had more time?

- Modifying my `POST: /data` endpoint to allow querying of multiple fields. I felt given the time that I should focus on completing the main task first before addressing the other requirements so I didnt prioritize it at the time.

- Implementing the other query parameters like `orderBy` and `sort` to have a more complete API

- With Fast API I'm more used to the utilizing SQL databases and SQL queries in order to retrieve and modify data. So if I was possible I would've liked to be retrieve the data from a database. (But maybe thats too much for a 3 hour test)

What challenges did you face and how did you overcome them?

- Finding the right libraries took up a good part of my time. Maybe I should've done a bit more research beforehand but I the end once I found the right ones they were not so difficult to implement.

## Screenshots

- `GET: /schema`
  ![Screenshot 2024-11-24 123047](https://github.com/user-attachments/assets/c8e0fa4c-6a81-4eaa-a7c0-e6817d6e2d74)

![Screenshot 2024-11-24 123149](https://github.com/user-attachments/assets/759432ca-675f-4b31-9ddf-eb792d7e77d6)

- `POST: /data`
  ![Screenshot 2024-11-24 123320](https://github.com/user-attachments/assets/cd8643f3-ee2e-42b6-ad7f-465432a7e90b)

![Screenshot 2024-11-24 123354](https://github.com/user-attachments/assets/d0cbfcb9-e089-41c8-a138-49178c514c81)

- `GET: /data/{id}`
  ![Screenshot 2024-11-24 123451](https://github.com/user-attachments/assets/051cc2c5-73ec-4974-a523-57202c43856a)

- `DELETE: /data/{id}`
  ![Screenshot 2024-11-24 123522](https://github.com/user-attachments/assets/e3ca525b-7561-4a3b-9a12-7777c6cfe5dd)

## Installation

1. Clone the repo: `git clone {REPO_URL}`

2. CD into the repo: `cd /path/to/repo`

3. Activate virtual environment: If Windows - `.\.venv\Scripts\activate ` / If Mac or Linux - `source .\.venv\bin\activate `

4. Install dependencies: `pip install -r .\requirements.txt` or `pip3 install -r .\requirements.txt`

5. Run server: `python .\main.py` or `python3 .\main.py`

6. Once running, visit `http://localhost:8000/{endpoint_name}` to call the enpoints. Also you can visit `http://localhost:8000/docs` to view the documentation.

If you're experiencing issues then delete the `.venv` file and make a new one with `python -m venv .venv`
