import telebot

# Bot credentials
BOT_TOKEN = "7830885491:AAGO9u-cTPje1_a6vXXMANehxlMPYEx0BG4"

# Default Group Chat ID (negative integer)
GROUP_CHAT_ID = -4726292517

# Authorized User ID (admin)
AUTHORIZED_USER_ID = 5457132722

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# Control variables
group_change_mode = False
sbot_mode = False
sbot_message = None

@bot.message_handler(content_types=['text', 'photo', 'video', 'sticker', 'document'])
def handle_messages(message):
    global GROUP_CHAT_ID, group_change_mode, sbot_mode, sbot_message

    # For the authorized user (admin)
    if message.from_user.id == AUTHORIZED_USER_ID:
        # If we are in group ID change mode, expect a new Group ID
        if group_change_mode:
            try:
                new_group_id = int(message.text.strip())
                if new_group_id < 0:
                    GROUP_CHAT_ID = new_group_id
                    group_change_mode = False
                    bot.send_message(AUTHORIZED_USER_ID, f"✅ Group ID changed to: {GROUP_CHAT_ID}")
                else:
                    bot.send_message(AUTHORIZED_USER_ID, "❌ Group ID must be a negative integer.")
            except (ValueError, AttributeError):
                bot.send_message(AUTHORIZED_USER_ID, "❌ Please send a valid group ID (negative integer).")
            return

        # SBOT mode (repeat a message)
        if sbot_mode:
            if not sbot_message:
                # The first message in SBOT mode is the message to be repeated
                sbot_message = message.text
                bot.send_message(AUTHORIZED_USER_ID, "✅ How many times do you want to repeat this message?")
            else:
                try:
                    repeat_count = int(message.text.strip())
                    if repeat_count > 0:
                        for _ in range(repeat_count):
                            bot.send_message(GROUP_CHAT_ID, sbot_message)
                        bot.send_message(AUTHORIZED_USER_ID, f"✅ Message sent {repeat_count} times.")
                    else:
                        bot.send_message(AUTHORIZED_USER_ID, "❌ The number must be greater than 0.")
                except ValueError:
                    bot.send_message(AUTHORIZED_USER_ID, "❌ Please send a valid number.")
                sbot_mode = False
                sbot_message = None
            return

        # Process admin commands
        if message.text:
            if message.text.strip().lower() == "id":
                # Do not forward "id" to the group; instead, ask for a new Group ID
                group_change_mode = True
                bot.send_message(AUTHORIZED_USER_ID, "🔄 Please send the new Group ID (negative integer).")
                return
            elif message.text.strip().lower() == "sbot":
                sbot_mode = True
                bot.send_message(AUTHORIZED_USER_ID, "✏️ Please send the message you want to repeat.")
                return
            else:
                # Forward any other text messages to the current group
                bot.send_message(GROUP_CHAT_ID, message.text)
        elif message.photo:
            bot.send_photo(GROUP_CHAT_ID, message.photo[-1].file_id)
        elif message.video:
            bot.send_video(GROUP_CHAT_ID, message.video.file_id)
        elif message.sticker:
            bot.send_sticker(GROUP_CHAT_ID, message.sticker.file_id)
        elif message.document:
            bot.send_document(GROUP_CHAT_ID, message.document.file_id)

    # For unauthorized users
    else:
        # Do not forward messages that come from the group chat
        if message.chat.id == GROUP_CHAT_ID:
            return

        sender_name = message.from_user.first_name or "Unknown"
        sender_id = message.from_user.id

        if message.text:
            bot.send_message(
                AUTHORIZED_USER_ID,
                f"📩 New message from:\nName: {sender_name}\nID: {sender_id}\nContent: {message.text}"
            )
            bot.send_message(message.chat.id, "✅ Your message has been forwarded to the admin.")
        else:
            # Forward media (photo, video, sticker, document) to the admin
            bot.send_message(
                AUTHORIZED_USER_ID,
                f"📩 New media received from:\nName: {sender_name}\nID: {sender_id}"
            )
            if message.photo:
                bot.send_photo(AUTHORIZED_USER_ID, message.photo[-1].file_id)
            elif message.video:
                bot.send_video(AUTHORIZED_USER_ID, message.video.file_id)
            elif message.sticker:
                bot.send_sticker(AUTHORIZED_USER_ID, message.sticker.file_id)
            elif message.document:
                bot.send_document(AUTHORIZED_USER_ID, message.document.file_id)

            bot.send_message(message.chat.id, "✅ Your message has been forwarded to the admin.")

print("Bot is running...")
bot.infinity_polling()
