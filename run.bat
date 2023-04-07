@echo Starting...



@echo ON
echo Making a new venv environment

call python -m venv venv
@echo ON
echo venv created
echo installing requirements

@echo ON
@echo Activating python venv

python.exe -m pip install --upgrade pip

call pip3 install -r .\requirements.txt


call .\venv\Scripts\activate

@echo ON
call python main.py

timeout /t 15