import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()     #on message 함수의 파라미터 값을 message로 받아서 유저가 메세지를 받을때 형식이 메세지점 어쩌구 저쩌구 옛날엔 아니였음 무슨얘기나 봇에 잇어서 커맨드를칠떄
intents.message_content = True          #항상대기를하고잇는데 봇이 인식하면 안돼니깐 구분자로 느낌표로 쓰는데 그건 prefix단위로 정의해나갔는데 그걸 다 intents -> 어떤 기능을 할지 정의

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('?music'):
        await message.channel.send('음악 이름을 입력해주세요')

    if message.content.startswith('?search'):
        await message.channel.send('전적을 조사할 소환사이름을 알려주세요')

    if message.content.startswith('?Schedule'):
        await message.channel.send('이번달 일정입니다.')
        await message.channel.send('5월 4일  중간총회')
        await message.channel.send('5월 7일  발로란트 ')
        await message.channel.send('5월 14일 이터널리턴 ')
        await message.channel.send('5월 21일 오버워치 ')
        await message.channel.send('5월 28일 칼바람 ')
        await message.channel.send('추가로 멘토멘티 진행할 예정입니다 ')

    if message.content.startswith('?Scheadd'):
        await message.channel.send('추가할 날짜와 일을 입력해주세요')

    if message.content.startswith('?Chan'):
        await message.channel.send('변경할 채널의 인덱스르 알려주세요')
        await message.channel.send('현재 채널 목록 ...')

    if message.content.startswith('?join'):
        await message.channel.send('이름과 학번 학과 생일을 입력해주세요 각 순서에 맞게 띄어쓰기로 입력해주세요')

    if message.content.startswith('?입력'):
        await message.channel.send('인증되셨습니다')  

    if message.content.startswith('?실패'):
        await message.channel.send('명단에 없는 회원입니다. 운영진에게 문의 주시기 바랍니다')      


client.run('MTA5MjgxNDIzNjg1NTU3ODYyNA.GRO8aM.CjB2OarPrTfQVrmMWAAoA0lIOCsrI2DGnT8i7I')