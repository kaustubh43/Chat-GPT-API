@echo Running
@echo ON
@echo Activating python venv
@echo OFF

call .\venv\Scripts\activate

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