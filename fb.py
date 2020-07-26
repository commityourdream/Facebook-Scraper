import facebook
import requests

at = "EAAItNZBln2rUBAFkPZADYqji65kuQl1ZBO8LG8DZCKi9LnF1jJlfLBaqRt9KnwyppkTaZCttLJMnZC5ZCloFZCTet7FvPBOZBRZBF15MJBoL0FFeFn5uUZAZBgDHp00ZAd4ogJs2FUNRPZB54Xj4H8dZBbOOKy8VXf7aX8KDrgC3lRteWvshtPFml9rym8ZBBg3HQvWlCEwkiVseVWQMvAZDZD"
pid = "my page id"
api = facebook.GraphAPI( at )
#args = {'fields' : 'conversations'}  #requested fields
conv = api.get_object('me?fields=id,name,feed{message,created_time}')
print conv
#args = {'fields' : 'message'}
#msg = api.get_object('/'+<message id>, **args)
#msg = api.get_object( conv['data'][0]['id']+'/messages')
#for el in msg['data']:
    #content = api.get_object( el['id'], **args)   #adding the field request
    #print conv
