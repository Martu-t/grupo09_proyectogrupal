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
        os.system('echo [34m DEPLOYING M.L. MODEL... [0m')
        try:
            import deploy_model
            deploy_model.clusterize()        
            os.system('echo [32m DATA CLUSTERIZED  OK [0m')
        except:
            okcycle = False
            os.system('echo [31m ERROR CLUSTERIZING DATA [0m')

    if okcycle == True:
        os.system('echo [34m CHECKING IF EVENTS SHOULD BE TWITTED... [0m')
        try:
            import twitter_selector
            twitter_selector.twitter_csv()        
            os.system('echo [32m DATA CHECKED FOR TWITTER OK [0m')
        except:
            okcycle = False
            os.system('echo [31m ERROR CHECKING DATA FOR TWITTER [0m')            

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

    os.system('echo [34m CHECKING IF THERE ARE EVENTS LEFT TO TWIT [0m')
    try:
        import twitterbot2
        twitterbot2.exec()
        os.system('echo [32m TWITTER PROCESS FINISHED OK [0m')
    except:
        okcycle = False
        os.system('echo [31m ERROR IN TWITTER PROCESS [0m')

    
        
    os.system('echo [101;93m NEXT CYCLE STARTS: '+str((datetime.datetime.now()+delta).strftime('%Y-%b-%d %H:%M:%S'))+' [0m')
    # break
    time.sleep(cycle*60)
































