from wsgiref.simple_server import make_server


def application(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, response_headers)

    # return ["Hola, gente de bien".encode('utf-8')]
    # return [bytes("Hola, gente de bien", 'utf-8')]


server = make_server('localhost', 8000, application)
server.serve_forever()
