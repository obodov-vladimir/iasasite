from iasasite import mongo, bcrypt

ROLE_USER = 0
ROLE_ADMIN = 1


class User():

    def __init__(self, user):
        self.id = user['_id']
        self.name = user['name']
        self.surename = user['surename']
        self.email = user['email']
        self.password = user['password']

    def toJson(self):
    	return {
            'id': self.id,
            'name' : self.name, 
    		'surename' : self.surename,
    		'email' : self.email,
    		'password' : self.password
        }

    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)

class Post():
    
    def __init__(self, news):
        self.id = str(news['_id'])
        self.title = news['title'].encode('utf-8').decode()
        self.text = news['text'].encode('utf-8').decode()
        self.date = str(news['date'])

    def toJson(self):
        return {
            'id': self.id,
    		'title' : self.title,
    		'text' : self.text,
            'date' : self.date
        }
