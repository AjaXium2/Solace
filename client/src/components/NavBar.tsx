function NavBar() {
  return (
    <div className="h-[10%] w-full bg-[#151515] shadow-lg flex items-center">
      <img
        src="/ai-logo.svg"
        alt="AI Logo"
        className="w-[13%] h-auto lg:w-[4%] m-4 md:w-[7%]"
      />
      <h1 className="text-white text-[220%] mt-[1%]">Solace</h1>
    </div>
  );
}
export default NavBar;
