import facebook
import requests
import csv
at = "EAAKHIpZBSTYwBAF7AVnHTnGZCdNFLRklOVME4Nt7OZB2FlZBNYLZBfPebhjfHID4XL8yd8gCd4dh9lQX2TKyrwxcV7D3Rw4PLW6H2lPZBBrn0yQU6ObfcQT7w44rUs3fVx8coywNQICN2OPkvFZC2e2xpVF1nj2Cb9ZC0iNAhMnLbxLkFqCn0I1oziEDrQ3ki0nZA4KbMlZBmh8gZDZD"
pid = "my page id"
api = facebook.GraphAPI( at )
#args = {'fields' : 'conversations'}  #requested fields
conv = api.get_object('me?fields=id,name,conversations{messages.limit(10){created_time,message,from,id},id,link}')
##conv1 = api.get_object('me?,conversations{messages.limit(10){created_time,message,from,id},id,link}')
print conv

