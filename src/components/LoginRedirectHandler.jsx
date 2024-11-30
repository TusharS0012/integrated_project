import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const LoginRedirectHandler = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Get the token and user details from the URL query parameters
    console.log("LoginRedirectHandler started");
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get("token");
    const email = urlParams.get("email");
    const firstName = urlParams.get("first_name");
    const lastName = urlParams.get("last_name");

    if (token && email && firstName && lastName) {
      // Store the token and user details in localStorage
      localStorage.setItem("authToken", token);
      localStorage.setItem("email", email);
      localStorage.setItem("first_name", firstName);
      localStorage.setItem("last_name", lastName);

      // Redirect to the desired page (e.g., dashboard)
      navigate("/"); // You can change this to any page you want to navigate to
    } else {
      alert("Missing token or user details in the URL.");
    }
  }, [navigate]);

  return (
    <div className="flex justify-center items-center text-6xl">LOADING!!!</div>
  );
};

export default LoginRedirectHandler;
