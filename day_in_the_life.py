import fitbit
import ConfigParser
import json
 
#Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')
CI_id              = parser.get('Login Parameters', 'CLIENT_ID')
CI_client_secret   = parser.get('Login Parameters', 'CLIENT_SECRET')
CI_access_token    = parser.get('Login Parameters', 'ACCESS_TOKEN')
CI_refresh_token   = parser.get('Login Parameters', 'REFRESH_TOKEN')

authd_client = fitbit.Fitbit(CI_id, CI_client_secret, oauth2=True, access_token=CI_access_token, refresh_token=CI_refresh_token)

base_date = '2017-02-01'

intradayH = authd_client.intraday_time_series('activities/heart', base_date = base_date, 
    detail_level = '1sec', start_time = None, end_time = None)

f = open('output/'+base_date+'_datadumpHeart.json', 'w')
json.dump(intradayH, f)
f.close()