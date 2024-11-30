import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from "./routes/App.jsx";
import Reports from "./routes/Reports.jsx";
import Settings from "./routes/Settings.jsx";
import Body from "./components/body.jsx";
import LoginRedirectHandler from "./components/LoginRedirectHandler.jsx"; // Import the new LoginRedirectHandler component

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { path: "/", element: <Body /> },
      { path: "/Reports", element: <Reports /> },
      { path: "/Settings", element: <Settings /> },
      { path: "/login-redirect", element: <LoginRedirectHandler /> }, // Add a route for login redirect
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
