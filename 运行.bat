@echo off 
Title DataBase                                              
Color 0A   
:caozuo  
echo. 
echo �T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T�T
echo ����������      
echo    1.¼�� 
echo    2.��ѯ
echo.
set /p n=���������: 
if "%n%"=="" cls&goto :caozuo 
if "%n%"=="1" call :1 
if "%n%"=="2" call :2
if /i "%n%"=="n" exit 
pause 
goto :eof 

:1 
echo ¼�� 
D:\Projects\qt\venv\Scripts\python.exe D:/tizen/Documents/GitHub/WebRoad/Python/Python-practice/¼��.py
goto :caozuo 

:2 
echo ��ѯ 
D:\Projects\qt\venv\Scripts\python.exe D:/tizen/Documents/GitHub/WebRoad/Python/Python-practice/��ѯ.py
goto :caozuo
