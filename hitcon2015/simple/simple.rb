require 'net/http'
require 'json'
require 'openssl'

uri = URI.parse('http://52.69.244.164:51913')
data = {'username'=>'a','password'=>'a'}
res = Net::HTTP.post_form(uri, data)

cookie = res.response['set-cookie'].split('; ')[0]

headers = {
  'Cookie' => cookie
}

auth = cookie.split('=')[1]
auth = URI.unescape(auth)
a =  "db\":\"hitcon-ctf\""
b =  "admin\":true}" + "\x00\x00\x00\x00"

auth_ori = auth.unpack('H*')
auth_ori = [auth_ori[0][48*2,16*2]].pack('H*')

c = a.unpack('C*').zip(b.unpack('C*')).map { |a,b| a^b }.pack('C*')
c = auth_ori.unpack('C*').zip(c.unpack('C*')).map { |a,b| a^b }.pack('C*')

auth = [auth.unpack('H*')[0][0,48*2] + c.unpack('H*')[0][0,12*2]].pack('H*')

http = Net::HTTP.new(uri.host, uri.port)
req = Net::HTTP::Get.new(uri.request_uri)
req['Cookie'] = cookie.split('=')[0] + "=" + URI.escape(auth)
res = http.request(req)

puts res.body

#auth=%D2%8C%8F%BF%CD%B8W%ACa%91%84%99qd%04%5B1%BB%A2%D1%3C%C4K7%E3J%B6%06%5D%11%99%F6%93%16D%CD%CB%09%18%FD%F7%9B%EC*%8D%1D%0C%D6%E1J%92%A0O%23%C9KN%D2Mg6%A8R%A5%12
#auth=%D2%8C%8F%BF%CD%B8W%ACa%91%84%99qd%04[1%BB%A2%D1%3C%C4K7%E3J%B6%06]%11%99%F6%93%16D%CD%CB%09%18%FD%F7%9B%EC*%8D%1D%0C%D6%E4L%DD%F3%03i%9AK_%C8F7
#You're admin! The flag is hitcon{WoW_CFB_m0dE_5o_eAsY}