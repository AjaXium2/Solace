function Slogan() {
  return (
    <>
      <div className="lg:my-auto overflow-hidden w-[80%] lg:w-[40%] mx-auto h-[35%] bg-[#151515] rounded-[5px] border-solid border-[1px] border-[#006ff7]">
        <img
          src="/ai-logo.svg"
          alt=""
          className="w-[40%] lg:w-[24%] h-auto mx-auto mt-[5%] md:w-[32%]"
        />
        <div className="text-center">
          <h1 className="text-white text-[300%]">Solace</h1>
          <p className="text-[90%] sm:text-[110%] md:text-[150%] lg:text-[100%] italic font-bold text-white mb-3">
            Your sanctuary in the darkest of times
          </p>
        </div>
      </div>
    </>
  );
}

export default Slogan;

/*
<div className="overflow-hidden w-[80%] min-w-[40%] lg:w-[40%] lg:mx-0 lg:ml-[10%] h-[35%] bg-[#151515] rounded-[5px] border-solid border-[1px] border-[#006ff7] mx-auto mt-[10%]">
  <img
    src="/ai-logo.svg"
    alt=""
    className="w-[40%] lg:w-[24%] h-auto mx-auto mt-[5%] md:w-[32%]"
  />
  <div className="text-center">
    <h1 className="text-white text-[300%]">Solace</h1>
    <p className="text-[100%] md:text-[150%] lg:text-[100%] italic font-bold text-white mb-3">
      Your sanctuary in the darkest of times
    </p>
  </div>
</div>
</>
*/
