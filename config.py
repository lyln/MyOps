CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

MYSQL_HOST='localhost'
DB_USER = 'root'
DB_PASSWD = 'root123'
DB_NAME = 'myblog'
DB_URL = 'mysql://' + DB_USER + ':' + DB_PASSWD +'@' + MYSQL_HOST + '/' + DB_NAME

# page_size
PER_PAGE = 5

UPLOAD_FOLDER = 'F:\codes\pycode\upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','gzip'])


OPENID_PROVIDERS = [
    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'MyOpenID','url':'https://www.myopenid.com'}
]