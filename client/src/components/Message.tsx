interface MessageProps {
  text: string;
  bgColor?: string;
}

function Message({ text, bgColor }: MessageProps) {
  return (
    <div
      className={`inline-block p-6 mb-3 ${bgColor} rounded-[15px] text-white`}
    >
      <p>{text}</p>
    </div>
  );
}

export default Message;
