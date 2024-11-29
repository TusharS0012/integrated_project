import React from "react";
import Sidebar from "../components/sidebar";
import Navbar from "../components/navbar";
import "./App.css";
import { Outlet, useLocation } from "react-router-dom";

function App() {
  const location = useLocation();
  
  return (
    <div className="bg-gray-900 p-4 w-screen h-screen overflow-hidden">
    <div className="flex flex-row gap-1 w-full h-full">
      <Sidebar />
      <div className="flex flex-col w-full">
        <Navbar />
        <Outlet/>
      </div>
    </div>
    </div>
  );
}

export default App;
