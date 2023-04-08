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

call .\venv\Scripts\activate

python.exe -m pip install --upgrade pip

call pip3 install -r .\requirements.txt




@echo ON
@echo Running your script... Please wait
@echo OFF
call .\venv\Scripts\python.exe .\main.py


@echo ON
@echo deactivating venv...
@echo OFF

call deactivate
timeout /t 10
@echo ON
@ Press any key to exit