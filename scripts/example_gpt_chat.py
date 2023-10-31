from llmChatbot.chatbots import GptChatBot


def main():
    model = "gpt-3.5-turbo"
    # model = "gpt-4"
    bot = GptChatBot()
    bot.interactive_chat(model=model)


if __name__ == "__main__":
    main()