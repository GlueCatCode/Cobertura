import shlex
from subprocess import Popen, PIPE
from threading import Timer

# Return std, output
# std == 0 time expired
# std == 1 success
# std == 2 error
def run(cmd, timeout_sec):
    proc = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    timer = Timer(timeout_sec, proc.kill)
    try:
        timer.start()
        stdout, stderr = proc.communicate()
        if timer.is_alive():
            if stderr:
                return 2, stderr.decode("utf-8")
            else:
                return 1, stdout.decode("utf-8")
        else:
            html = '''<div class="card p-3 mb-2 bg-danger text-white" style="height: 262px;">
            <h5>Tempo excedido por {} segundos...</h5><br>
            {}
            </div>'''
            return 0, html.format(timeout_sec, cmd)
    finally:
        timer.cancel()

# Return tag script to inject spaces
def getScriptFrom(spaces):
    temp = ''
    for i in spaces:
        temp += ('\nsetSpace(' + str(i) + ');')
    return '''<script>\n$(function(){{{}\n}});\n</script>'''.format(temp)