#https://github.com/pyfa-org/Pyfa/tree/master/service/server.py
import http.server
import socket
import urllib.parse

import threading
import service
import config

HTML = '''
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>''' + config.APP_NAME + ''' Local Server</title>
    <style type="text/css">
        body {{ text-align: center; padding: 150px; }}
        h1 {{ font-size: 40px; }}
        h2 {{ font-size: 32px; }}
        body {{ font: 20px Helvetica, sans-serif; color: #333; }}
        #article {{ display: block; text-align: left; width: 650px; margin: 0 auto; }}
        a {{ color: #dc8100; text-decoration: none; }}
        a:hover {{ color: #333; text-decoration: none; }}
    </style>
</head>

<body>

<!-- Layout from Short Circuit's CREST login. Shout out! https://github.com/farshield/shortcircuit -->
<div id="article">
    <h1>''' + config.APP_NAME + '''</h1>
    {0}
</div>

<script type="text/javascript">
function extractFromHash(name, hash) {{
    var match = hash.match(new RegExp(name + "=([^&]+)"));
    return !!match && match[1];
}}

var hash = window.location.hash;
var token = extractFromHash("access_token", hash);
var step2 = extractFromHash("step2", hash);

function doRedirect() {{
    if (token){{
        // implicit authentication
        var redirect = window.location.origin.concat('/?', window.location.hash.substr(1), '&step=2');
        window.location = redirect;
    }}
    else {{
        // user-defined
        var redirect = window.location.href + '&step=2';
        window.location = redirect;
    }}
}}

// do redirect if we are not already on step 2
if (window.location.href.indexOf('step=2') == -1) {{
    setTimeout(doRedirect(), 1000);
}}
</script>
</body>
</html>
'''


# https://github.com/fuzzysteve/CREST-Market-Downloader/
class AuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            return

        parsed_path = urllib.parse.urlparse(self.path)
        parts = urllib.parse.parse_qs(parsed_path.query)
        msg = ""

        # print(parts)
        step2 = 'step' in parts
        try:
            if step2:
                self.server.callback(parts)
                print("Successfully logged into ESI.\n")
                msg = "If you see this message then it means you should be logged into ESI. You may close this window and return to the application."
            else:
                # For implicit mode, we have to serve up the page which will take the hash and redirect useing a querystring
                print("Processing response from EVE Online.")
                msg = "Processing response from EVE Online"
        except Exception as ex:
            print("Error in ESI AuthHandler")
            print(ex)
            msg = "<h2>Error</h2>\n<p>{}</p>".format(ex)
        finally:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(HTML.format(msg)))

        if step2:
            # Only stop once if we've received something in the querystring
            self.server.stop()

    def log_message(self, format, *args):
        return


# http://code.activestate.com/recipes/425210-simple-stoppable-server-using-socket-timeout/
class StoppableHTTPServer(http.server.HTTPServer):
    def server_bind(self):
        http.server.HTTPServer.server_bind(self)
        # self.settings = CRESTSettings.getInstance()

        # Allow listening for x seconds
        sec = 100  # self.settings.get('timeout')
        print("Running server for {0} seconds", sec)

        self.socket.settimeout(1)
        self.max_tries = sec / self.socket.gettimeout()
        self.tries = 0
        self.run = True

    def get_request(self):
        while self.run:
            try:
                sock, addr = self.socket.accept()
                sock.settimeout(None)
                return sock, addr
            except socket.timeout:
                print("Server timed out waiting for connection")
                pass

    def stop(self):
        print("Setting ESI server to stop.")
        self.run = False

    def handle_timeout(self):
        print("Number of tries: {0}", self.tries)
        self.tries += 1
        if self.tries == self.max_tries:
            print("Server timed out waiting for connection")
            self.stop()

    def serve(self, callback=None):
        self.callback = callback
        while self.run:
            try:
                self.handle_request()
            except TypeError:
                print("Caught exception in serve")
                pass

        self.server_close()


if __name__=="__main__":
    httpd = StoppableHTTPServer(("127.0.0.1", service.config.PORT), AuthHandler)
    threading._start_new_thread(httpd.serve, ())
    input("Press <RETURN> to stop server\n")
    httpd.stop()
