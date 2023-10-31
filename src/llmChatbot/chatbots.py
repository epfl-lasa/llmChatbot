import openai
import os
import typing as tp

DEFAULT_MODEL = "gpt-3.5-turbo"

class GptChatBot:

    API_KEY_ENV_VAR = "GPT_API_KEY"
    DFLT_SYSTEM_MSG = "You are a robotics and machine learning expert."

    @property
    def system_msg(self) -> str:
        return self._system_msg

    @system_msg.setter
    def system_msg(self, value: str) -> None:
        self._system_msg = value

    def __init__(self, system_msg: tp.Optional[str] = None) -> None:
        openai.api_key = os.getenv(self.API_KEY_ENV_VAR)
        self._history = []
        self._system_msg = self.DFLT_SYSTEM_MSG if system_msg is None else system_msg

    def ask(self, input: str,
            model: str = DEFAULT_MODEL,
            show_output: bool = False,
            force_cot: bool = False) -> str:

        # Format messages
        system_msg = [{"role": "system", "content": self._system_msg}]
        self._history.append(input)

        # Forcing chain of thought
        if force_cot:
            self._history.append("Let's thing step by step.")
        user_bot_dialogue = [{"role": "assistant", "content": self._history[i]} if i % 2 else
                             {"role": "user", "content": self._history[i]}
                             for i in range(len(self._history))]
        msgs = system_msg + user_bot_dialogue

        # GPT query... costs money
        response = openai.ChatCompletion.create(model=model, messages=msgs)

        # Check status
        status_code = response["choices"][0]["finish_reason"]
        assert status_code == "stop", f"The status code was {status_code}."

        # Save and return output
        text_response = response["choices"][0]["message"]["content"]

        if force_cot:
            text_response = "Let's think step by step.\n " + text_response
        self._history.append(text_response)

        # Show output
        if show_output:
            print(f"GPT: {text_response}")

        return text_response

    def interactive_chat(self, model: str = DEFAULT_MODEL) -> None:

        # Discussion loop
        print("Ready to chat...")
        while True:

            user_input = input("You: ")
            if user_input in ["quit", "exit", "q"]:
                break

            self.ask(user_input, show_output=True, model=model)

    def __call__(self, input: str, model: str = DEFAULT_MODEL) -> str:

        # Format messages
        system_msg = [{"role": "system", "content": self._system_msg}]
        user_input = [{"role": "assistant", "content": input}]
        msgs = system_msg + user_input

        # GPT query... costs money
        response = openai.ChatCompletion.create(model=model, messages=msgs)

        # Check status
        status_code = response["choices"][0]["finish_reason"]
        assert status_code == "stop", f"The status code was {status_code}."

        # Save and return output
        text_response = response["choices"][0]["message"]["content"]
        return text_response