for /F "tokens=*" %%L in (locations.txt) do ( 
    for /F "tokens=*" %%J in (jobs.txt) do start /B /wait .\jobs_functions.py %%J  %%L 90
)