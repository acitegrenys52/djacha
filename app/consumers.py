from channels import Group

from app.models import Chat


def ws_add(data):
    Group("chat").add(data.reply_channel)

    last_messages = Chat.objects.all().order_by('-id')[:10:-1]

    for message in last_messages:
        data.reply_channel.send({"text": message.text})


def ws_message(data):
    message = data.content['text']

    Group("chat").send({"text": message})

    Chat(text=message).save()


def ws_disconnect(data):
    Group("chat").discard(data.reply_channel)
