from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.topic import Topic

import cgi
import uuid

class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You are not logged in.")

        title = cgi.escape(self.request.get("title"))
        text = cgi.escape(self.request.get("text"))

        new_topic = Topic(title=title, content=text, author_email=user.email())

        new_topic.put()

        return self.redirect_to("topic_details", topic_id=new_topic.key.id())

class TopicHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))

        params = {"topic": topic}

        return self.render_template("topic_details.html", params=params)



