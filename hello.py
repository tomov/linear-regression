import pygal
import json
from urllib2 import urlopen  # python 2 syntax
# from urllib.request import urlopen # python 3 syntax
 
 
from flask import Flask
from pygal.style import DarkSolarizedStyle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def bars(x, y, title):
    assert len(x) == len(y)
    bar_chart = pygal.Bar(width=1200, height=600,
                          explicit_size=True, title=title, style=DarkSolarizedStyle)
    bar_chart.x_labels = x
    bar_chart.add('Y', y)
    return bar_chart

@app.route('/weather')
def get_weather_data(date='20140415', state='IA', city='Ames'):
    """
    Date must be in YYYYMMDD
    """
    api_key = '23515cde0fad7e24'
    url = 'http://api.wunderground.com/api/{key}/history_{date}/q/{state}/{city}.json'
    new_url = url.format(key=api_key,
                         date=date,
                         state=state,
                         city=city)
    result = urlopen(new_url)
    js_string = result.read()
    parsed = json.loads(js_string)
    history = parsed['history']['observations']
 
    imp_temps = [float(i['tempi']) for i in history]
    print imp_temps
    times = ['%s:%s' % (i['utcdate']['hour'], i['utcdate']['min']) for i in history]
 
    # create a bar chart
    title = 'Temps for %s, %s on %s' % (city, state, date)
    bar_chart = pygal.Bar(width=1200, height=600,
                          explicit_size=True, title=title, style=DarkSolarizedStyle)
    #bar_chart = pygal.StackedLine(width=1200, height=600,
    #                      explicit_size=True, title=title, fill=True)
 
    bar_chart.x_labels = times
    bar_chart.add('Temps in F', imp_temps)

    bar_chart = bars(times, imp_temps, title)
    bar_chart = bars([1, 2, 3, 4, 100], [1000, 2000, 3000, 1000, 1500], title)
 
    html = """
        <html>
             <head>
                  <title>%s</title>
             </head>
              <body>
                 %s
             </body>
        </html>
        """ % (title, bar_chart.render())
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)
