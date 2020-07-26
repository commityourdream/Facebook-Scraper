import facebook
token = 'EAAItNZBln2rUBALNV9skq7EHW6fsACWZCkC1KiMfsYBGbDtwO1FfzErVqnaGlBJy1NchrF3sAjRLDLmSMZCQL9tOpIZC1hyfKtlmYEqPkHcIEHLfbeCxHM5wDxujWveAXABZBG8ZBas8odVWJYVyVUMJbe1kucUSlzmtV4QOedWPGh5ctbeIHm22hUPzsLoN4ZD'
graph =facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections('me?fields=id,name,friendlists')
friend_list = [friend['name'] for friend in friends['data']]
print friend_list
