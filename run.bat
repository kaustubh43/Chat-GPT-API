@echo Starting...



@echo ON
echo Making a new venv environment
@echo OFF

call python -m venv venv
@echo ON
echo venv created
echo installing requirements
@echo OFF

@echo ON
@echo Activating python venv
@echo OFF

python.exe -m pip install --upgrade pip

call pip3 install -r .\requirements.txt


call .\venv\Scripts\activate

@echo ON
@echo Running your script... Please wait
@echo OFF
call .\venv\Scripts\python.exe .\main.py

timeout /t 15