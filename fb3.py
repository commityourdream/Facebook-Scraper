import Facebook
token = 'EAAItNZBln2rUBAMB5HPb5Sls8e8uGQaxcjtHIxaCsCAwRBd5pLxzHxyNZBPznlpSe8TD1nnji8Ks1D05pM4vwX3JmfQVZBGHQ7yvr7ppq9iy1okqGVqZCmH5XRCumay5KtaPgZA9soCnkpIlmqtMh0PQNzIFbMwAeZArfwCYKlgfjWy3ACwqfMnXkiIZBLntuaBdACJwVSDhQZDZD'
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print friend_list
