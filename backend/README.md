# Parser Backend

Information for use the backend

>  Manuel Enrique Hernandez Duarte 

## Requirements

- [Python 3](https://www.python.org/downloads/)


- Create a virtual environment 

> ⚡️ Using [Virtualenv](https://pypi.org/project/virtualenv/)

```bash 
virtualenv .venv
```
- Activate the virtual environment

> Windows
```bash 
.\.venv\Scripts\activate.bat
```

> Unix 
```bash 
source ./.venv/bin/activate
```

- Install all the requirements for this project
```bash 
pip install -r requirements.txt 
```

## Usage

1.  Go to src

```bash
cd src 
```

2. Run the script 

```bash 
uvicorn app:app --reload
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)