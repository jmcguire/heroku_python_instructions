import web
import datetime

urls = (
  '/', 'index'
)

class index:
  def GET(self):
    return "The time is:", datetime.datetime.now()

if __name__ == "__main__": 
  app = web.application(urls, globals())
  app.run() 

