import NavBar from "../components/NavBar";
import Slogan from "../components/Slogan";
import { Link } from "react-router-dom";

function MainPage() {
  return (
    <div className="w-full h-full">
      <NavBar />
      <div className="p-4 lg:flex lg:mt-[3%] xl:h-[35%]">
        <Slogan />
        <img
          src="depression1.png"
          alt=""
          className="w-[80%] mx-auto lg:ml-[3%] lg:w-[38%] lg:h-[35%] lg:h-max-[260px]"
        />
      </div>
      <Link className="flex justify-center" to="/chat">
        <button className="mb-[5%] bg-white border-solid border-2 border-[#006ff7] rounded-[5px] w-[80%] h-[7%] p-2 lg:w-[20%] text-[20px] text-[#006ff7] font-bold">
          Enter your Haven
        </button>
      </Link>
    </div>
  );
}

export default MainPage;
