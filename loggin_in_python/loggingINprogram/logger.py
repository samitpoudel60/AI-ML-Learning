import logging
logging.basicConfig(   
    level=logging.DEBUG,  ##this will set the logging level to debug so that all the messages with level debug and above will be logged
    filename='log_file.log',  ##this will save the log messages to a file named app.log
    filemode='w',  ##this will overwrite the log messages to the file instead of appending if we had to add the log message we would use append but we have to overwrite so we are using 'w'
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' ,##this is for the date time format 
    force=True

)
##hamile yo file ma logging configuration gareko ho ani aba yo file lai aru file ma import garera logging use garna sakincha
