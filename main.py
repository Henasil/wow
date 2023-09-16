from telegram import Update, ForceReply
from telegram.ext import CommandHandler, Application, ContextTypes


class MyBot:
    def __init__(self, bot_token):
        self.application = Application.builder().token(bot_token).build()

        # Регистрируем обработчики команд
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("con", self.help))
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        print(user.mention_html())
        await update.message.reply_html(
            f"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(text="Это простой бот. Он может отвечать на текстовые сообщения.")

    async def con(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        print(user.mention_html())
        await update.message.reply_html(
            f"- Как сказать по татарски вперед? - спрашивает русский у татарина. - Алга! - говорит татарин. - А как сказать назад? - У татар нет назад, они разворачиваются и алга!",
            reply_markup=ForceReply(selective=True),
    )




if __name__ == "__main__":
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    bot = MyBot(bot_token="5783230577:AAEO7rpGOaPm1HVL7a2oiQF-tRj1iEhy8hA")