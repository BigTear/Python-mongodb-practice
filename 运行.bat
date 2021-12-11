@echo off 
Title DataBase                                              
Color 0A   
:caozuo  
echo. 
echo ═══════════════════════════════════════
echo 【操作】：      
echo    1.录入 
echo    2.查询
echo.
set /p n=输入操作号: 
if "%n%"=="" cls&goto :caozuo 
if "%n%"=="1" call :1 
if "%n%"=="2" call :2
if /i "%n%"=="n" exit 
pause 
goto :eof 

:1 
echo 录入 
D:\Projects\qt\venv\Scripts\python.exe D:/tizen/Documents/GitHub/WebRoad/Python/Python-practice/录入.py
goto :caozuo 

:2 
echo 查询 
D:\Projects\qt\venv\Scripts\python.exe D:/tizen/Documents/GitHub/WebRoad/Python/Python-practice/查询.py
goto :caozuo
