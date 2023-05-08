# *HTTP LIKE SERVER*
*This program impliments http server which supports GET request and respond<br />
The webroot is taken from "Gvahim"'s network book*

Constants are defined as below:<br /><br />
IP = '0.0.0.0'<br />
PORT = 80<br />
SOCKET_TIMEOUT = 15<br />
GET_METHOD = "GET "<br />
URL = "http://127.0.0.1:80 "<br />
HTTP_VERSION = "HTTP/1.1"<br />
DEFAULT_URL = '/'<br />
DEFAULT_ROOT = "./webroot"<br />
DEFAULT_FILE = '/index.html'

FIXED_RESPONSE = "OK"<br />
DATA_BUFFER_SIZE = 4096

STATUS_CODE_200_OK = 200<br />
STATUS_CODE_302_MOVED_TEMPORARILY = 302<br />
STATUS_CODE_403_FORBIDDEN = 403<br />
STATUS_CODE_404_NOT_FOUND = 404<br />
STATUS_CODE_500_INTERNAL_SERVER_ERROR = 500

HTML_SUFFIX = ".html"<br />
CSS_SUFFIX = ".css"<br />
JPEG_SUFFIX = ".jpeg"<br />
JPG_SUFFIX = ".jpg"<br />
JS_SUFFIF = ".js"<br />
ICO_SUFFIX = "ico"<br />
GIF_SUFFIX = ".gif"

OK_200_RESPONSE = 'HTTP/1.1 200 OK\r\n'<br />
REDIRECT_302_RESPONSE = 'HTTP/1.1 302 Found\r\n'<br />
NOT_FOUND_404_RESPONSE = 'HTTP/1.1 404 NOT FOUND\r\n'<br />
INTERNAL_SERVER_ERROR_500_RESPONSE = 'HTTP/1.1 500 Internal Server Error\r\n'

CONTENT_TYPE_TEXT_PLAIN = 'Content-Type: text/plain\r\n'<br />
CONTENT_TYPE_TEXT_HTML = 'Content-Type: text/html; charset=utf-8\r\n'<br />
CONTENT_TYPE_IMAGE = 'Content-Type: image/jpeg\r\n'<br />
CONTENT_TYPE_TEXT_JS = "Content-Type: text/javascript; charset=UTF-8\r\n"<br />
CONTENT_TYPE_TEXT_CSS = "Content-Type: text/css\r\n"<br />
CONTENT_TYPE_ICON = "Content-Type: image/vnd.microsoft.icon\r\n"<br />
CONTENT_TYPE_APPLICATION = 'Content-Type: application/*\r\n'<br />
CONTENT_LENGTH = 'Content-Length: '<br />
LOCATION = 'Location: '<br />
NEW_LINE = '\r\n'<br />
