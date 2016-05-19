from slistener import SListener
import time, tweepy, sys

## authentication
username = 'nvJK39qoozBs2Mjc7nq7w5NCi ' ## put a valid Twitter username here
password = 'ZtFEzMdhno3zJQxR56k7XVNduUEfR6Tuc9Q3TQP12sjSIoMNTD'## put a valid Twitter password here
#auth     = tweepy.OAuthHandler(username, password)
auth     = tweepy.OAuthHandler('czem4iDX1lqroDcpSLLuFJjCA', '1KD8tfF7a3ELGi2poFTLLXORtC7KgLr3gAa9uKYxv1WAx5aNjn')
auth.set_access_token('964897591-txgnbKX5pnRn6ZES6nBuA0yVKnCVKuVoKahFgQ1r', 'BWNtGzwThchCtAe9NWTRc00Fq89ndu9Dnkx9KgljT3YpZ')
api      = tweepy.API(auth)

def main():
    track = ['trump', 'clinton']
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()