import facebook
graph = facebook.GraphAPI(access_token="EAAKHIpZBSTYwBABsoF3uzBSHOW4LKSJnj5eIr6p36smKVnB57wRNPCR2XseDTIW8U5PEnchJ0tyFXYMEZCU4iH3f9nZCiLu5EMi6xHZCzJG6gpt0qljWnOV924LmLXjtfr2euyB42BdWeZCYEh7pTN7Cbn45oJSm8dtZACI6ODyZAgZCokHdf5vJw2pg5GVaJeT1vVuNMZAtHHwZDZD")
conv = graph.get_object(id='me',fields='id,name')
print conv
