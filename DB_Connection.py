import ibm_db
import ibm_db_dbi
import pandas as pd
import time
import DB_Details
def WLSDBConnection():
    try:
        WLSDBconn = ibm_db.connect("DATABASE={};".format(DB_Details.RIQ_DATABASE) + \
                                   "HOSTNAME={};".format(DB_Details.RIQ_HOSTNAME) + \
                                   "PORT={};".format(DB_Details.RIQ_PORT) + \
                                   "UID={};".format(DB_Details.RIQ_UID) + \
                                   "PWD={};".format(DB_Details.RIQ_PWD) + \
                                   "SSLServerCertificate={};".format(DB_Details.RIQ_SSLServerCertificate) + \
                                   "SECURITY={};".format(DB_Details.RIQ_SECURITY),
                                   "", "")
        WLSDBpdconn = ibm_db_dbi.Connection(WLSDBconn)

    except Exception as e:
        print(e, "RIQ connection was unsuccessful")
    else:
        print('RIQ connection was successful')
        return WLSDBpdconn

if __name__ == "__main__":
    WLSDBConnection()
