import datetime

import utils

src_url = 'https://www.python.org/'
pause_between_requests = 1
max_date = utils.get_max_date(datetime.datetime.now().utcnow(), 2)
