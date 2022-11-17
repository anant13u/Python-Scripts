
video_name = '!@#$%^&*()_+{}|:"<>?1234567890-=[]\;,./'

print(video_name)

encoded_name = video_name.encode()

print(encoded_name)

#   !@#$%^&*()_+{}|:"<>?1234567890-=[]\;,./
# b'!@#$%^&*()_+{}|:"<>?1234567890-=[]\\;,./'
