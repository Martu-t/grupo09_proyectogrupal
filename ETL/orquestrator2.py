import os
import datetime
import time



cycle = 15 #in [min] -> minutes between cycles
delta = datetime.timedelta(minutes = cycle)


while True:
    okcycle = True
    os.system('cls')
    os.system('echo [101;93m STARTING ETL PIPELINE CYCLE AT: '+str(datetime.datetime.now().strftime('%Y-%b-%d %H:%M:%S'))+' [0m')
    os.system('echo [34m EXTRACTING DATA... [0m')
    try:
        import extract2
        extract2.extr()
        os.system('echo [32m EXTRACTED DATA OK [0m')
    except:
        okcycle = False
        os.system('echo [31m ERROR EXTRACTING DATA [0m')

    if okcycle == True:
        os.system('echo [34m TRANSFORMING DATA... [0m')
        try:
            import transform2
            transform2.transf()        
            os.system('echo [32m DATA TRANSFORMED OK [0m')
        except:
            okcycle = False
            os.system('echo [31m ERROR TRANSFORMING DATA [0m')

    if okcycle == True:
        os.system('echo [34m LOADING DATA INTO DB... [0m')
        try:
            import load2
            load2.loader()
            os.system('echo [32m DATA LOADED OK [0m')
        except:
            okcycle = False
            os.system('echo [31m ERROR LOADING DATA [0m')

    if okcycle == True:
        os.system('echo [102m ETL PIPELINE FINISHED SUCCESSFULLY [0m')
    else:
        os.system('echo [101m ETL PIPELINE FINISHED WITH ERRORS [0m')
        
    os.system('echo [101;93m NEXT CYCLE STARTS: '+str((datetime.datetime.now()+delta).strftime('%Y-%b-%d %H:%M:%S'))+' [0m')
    time.sleep(cycle*60)
































