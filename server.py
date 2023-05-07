import socket 

IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 15
GET_METHOD = "GET "
URL = "http://127.0.0.1:80 "
HTTP_VERSION = "HTTP/1.1"
DEFAULT_URL = '/'
DEFAULT_ROOT = "./webroot"
DEFAULT_FILE = '/index.html'

FIXED_RESPONSE = "OK"
DATA_BUFFER_SIZE = 4096

STATUS_CODE_200_OK = 200
STATUS_CODE_302_MOVED_TEMPORARILY = 302
STATUS_CODE_403_FORBIDDEN = 403
STATUS_CODE_404_NOT_FOUND = 404
STATUS_CODE_500_INTERNAL_SERVER_ERROR = 500 

HTML_SUFFIX = ".html"
CSS_SUFFIX = ".css"
JPEG_SUFFIX = ".jpeg"
JPG_SUFFIX = ".jpg"
JS_SUFFIF = ".js"
ICO_SUFFIX = "ico"
GIF_SUFFIX = ".gif"

OK_200_RESPONSE = 'HTTP/1.1 200 OK\r\n'
REDIRECT_302_RESPONSE = 'HTTP/1.1 302 Found\r\n'
NOT_FOUND_404_RESPONSE = 'HTTP/1.1 404 NOT FOUND\r\n'
INTERNAL_SERVER_ERROR_500_RESPONSE = 'HTTP/1.1 500 Internal Server Error\r\n'

CONTENT_TYPE_TEXT_PLAIN = 'Content-Type: text/plain\r\n'
CONTENT_TYPE_TEXT_HTML = 'Content-Type: text/html; charset=utf-8\r\n'
CONTENT_TYPE_IMAGE = 'Content-Type: image/jpeg\r\n'
CONTENT_TYPE_TEXT_JS = "Content-Type: text/javascript; charset=UTF-8\r\n"
CONTENT_TYPE_TEXT_CSS = "Content-Type: text/css\r\n"
CONTENT_TYPE_ICON = "Content-Type: image/vnd.microsoft.icon\r\n"
CONTENT_TYPE_APPLICATION = 'Content-Type: application/*\r\n'
CONTENT_LENGTH = 'Content-Length: '
LOCATION = 'Location: '
NEW_LINE = '\r\n'



def get_file_data(file_name):
    try:
        required_file = open(file_name,'rb')
        file_data = required_file.read()
        required_file.close()
    except:
        print("file: %s was not found" % file_name)
        return "";
    return file_data #to be checked



def handle_client_request(resource, client_socket):

    #print("resours: %s" % resource)

    if resource == DEFAULT_URL:
        url = DEFAULT_ROOT + DEFAULT_FILE
    else:
        url = DEFAULT_ROOT + resource

    """
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response
        pass

    # TO DO: extract requested file tupe from URL (html, jpg etc)
    if filetype == 'html':
        http_header = # TO DO: generate proper HTTP header
    elif filetype == 'jpg':
        http_header = # TO DO: generate proper jpg header
    # TO DO: handle all other headers
    """
    file_name = url
    data = get_file_data(file_name)
    http_header = create_response_header(url)
    http_response = http_header.encode() + data
    client_socket.send(http_response)
    

def create_response_header(url):
    response = "%s %s \r\n" % (HTTP_VERSION, STATUS_CODE_200_OK)
    response += "DATE: 12/04/2023\r\n"

    if url.endswith(HTML_SUFFIX):
        response += "Content-Type: %s" % CONTENT_TYPE_TEXT_HTML
    elif url.endswith(JPEG_SUFFIX) or url.endswith(JPG_SUFFIX):
        response += "Content-Type: %s" % CONTENT_TYPE_IMAGE
    elif url.endswith(CSS_SUFFIX):
        print(url)
        #response += "Content-Type: %s" % CONTENT_TYPE_TEXT_CSS
    elif url.endswith(ICO_SUFFIX):
        response += "Content-Type: %s" % CONTENT_TYPE_ICON
    elif url.endswith(JS_SUFFIF):
        response += "Content-Type: %s" % CONTENT_TYPE_TEXT_JS


    response += "\r\n"
    return response



def validate_http_request(request):  
    request_lines = request.split('\r\n')
    get_command_line = request_lines[0]
    resource = ""
    valid = False

    command_parts = get_command_line.split(' ')
    if len(command_parts) == 3:
        method, resource, version = command_parts
        valid = ( method == 'GET' and version.startswith('HTTP/1.') )
    return valid, resource




def handle_client(client_socket):
    print(("client connected"))

    while True:
        try:
            client_request = client_socket.recv(DATA_BUFFER_SIZE).decode()
            valid_http, recource = validate_http_request(client_request)
            if valid_http:
                print("got valid HTTP request")
                handle_client_request(recource, client_socket)
                break
            else:
                print('Error: Not a valid HTTP request')
                #send error to the client
                #client_didnt_exit = False???
                break
        except:
            print("Exception while receiving. Disconnecting... \n " )
            #PrintException()
            break

    print("closing connection")
    client_socket.close()
    pass


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("listening for connections on port {}".format(PORT))

    while True:
        (client_socket, client_address) = server_socket.accept()
        print("new connection recived")
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)

if __name__ == "__main__":
    run_server()
