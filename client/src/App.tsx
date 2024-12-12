import "./App.css";
import MainPage from "./pages/MainPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import PromptPage from "./pages/PromptPage";

function App() {
  return (
    <Router>
      <div className="font-ComfortaaX bg-black w-screen min-h-screen overflow-hidden">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/chat" element={<PromptPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
