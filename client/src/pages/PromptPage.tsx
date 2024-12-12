import Message from "../components/Message";
import { useState } from "react";
import axios from "axios";

function PromptSection() {
  const [disabled, setDisabled] = useState(true);
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState<string[]>([]);
  const userMsgStyle = "mx-6 lg:ml-[auto] flex justify-end";
  const modelMsgStyle = "mx-6 flex justify-start";

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
    setDisabled(event.target.value === "");
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setMessages([...messages, inputValue]);
    axios
      .post("http://localhost:5001/api/prompt", { message: inputValue })
      .then((response) => {
        setMessages([...messages, response.data.message]);
      })
      .catch((error) => {
        console.log(error);
      });
    setInputValue("");
    setDisabled(true);
  };

  return (
    <div className="flex items-center justify-center w-screen h-screen overflow-hidden">
      <div className="overflow-hidden absolute w-[90%] h-[90%] bg-[#151515] rounded-[5px] border-solid border-[1px] border-[#006ff7] z-0 flex flex-col">
        <div className="overflow-y-auto my-2 pt-4 flex-grow">
          {messages.map((message, index) => (
            <div
              key={index}
              className={index % 2 === 0 ? userMsgStyle : modelMsgStyle}
            >
              <Message text={message} bgColor="bg-black" />
            </div>
          ))}
        </div>
        <div className="absolute bottom-0 pb-4 w-full bg-[#151515]">
          <form
            method="POST"
            className="flex items-center"
            onSubmit={handleSubmit}
          >
            <input
              type="text"
              onChange={handleInputChange}
              placeholder="How are you feeling?"
              value={inputValue}
              className="mr-[1%] outline-none ml-[2%] w-[85%] h-10 rounded-[5px] border-[1px] bg-[#151515] border-[#006FF7] text-[#006FF7] p-2"
            />
            <button
              disabled={disabled}
              type="submit"
              className="text-[#006FF7] min-w-[10%] h-10 w-[10%] bg-[#151515] rounded-[5px] border-[1px] hover:border-[2px] border-[#006FF7]"
            >
              <img
                src="/sendIcon.png"
                alt="Send"
                className="mx-auto h-[70%] w-auto"
              />
            </button>
          </form>
        </div>
      </div>
      <div className="absolute bottom-0 w-full z-10">
        <p className="text-white text-center text-[15%] xl:text-[100%] mb-3 sm:mb-[6px]">
          Note: Solace isn't a substitute for therapy, please seek professional
          help.
        </p>
      </div>
    </div>
  );
}

export default PromptSection;
