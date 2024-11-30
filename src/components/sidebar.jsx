import { Link, useLocation, useNavigate } from "react-router-dom";

function Sidebar() {
  const location = useLocation();
  const navigate = useNavigate();

  // Get the user's info from localStorage (or sessionStorage)
  const user = {
    email: localStorage.getItem("email"),
    firstName: localStorage.getItem("first_name"),
    lastName: localStorage.getItem("last_name"),
  };

  const handleLogout = () => {
    // Clear the user data from localStorage (or sessionStorage)
    localStorage.removeItem("authToken");
    localStorage.removeItem("email");
    localStorage.removeItem("first_name");
    localStorage.removeItem("last_name");

    // Redirect the user to the login page after logout
    navigate("/login");
  };

  return (
    <div className="sidebar rounded-[2rem] flex flex-col w-64">
      <div className="user-info text-orange-500 text-2xl text-center m-5 rounded-lg bg-white p-5 w-100">
        <p>
          {user.firstName ? `${user.firstName} ${user.lastName}` : "Tushar"}
        </p>
        <p>{user.email ? user.email : ""}</p>
      </div>
      <div className="flex flex-col gap-16 h-full m-10 justify-start">
        <Link
          to="/"
          className={`flex items-center gap-2 text-white hover:text-yellow-500 ${
            location.pathname === "/" ? "text-yellow-500" : ""
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="lucide lucide-gauge"
          >
            <path d="m12 14 4-4" />
            <path d="M3.34 19a10 10 0 1 1 17.32 0" />
          </svg>
          Dashboard
        </Link>

        <Link
          to="/Reports"
          className={`flex items-center gap-2 text-white hover:text-yellow-500 ${
            location.pathname === "/Reports" ? "text-yellow-500" : ""
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="lucide lucide-file-text"
          >
            <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z" />
            <path d="M14 2v4a2 2 0 0 0 2 2h4" />
            <path d="M10 9H8" />
            <path d="M16 13H8" />
            <path d="M16 17H8" />
          </svg>
          Reports
        </Link>

        <Link
          to="/Settings"
          className={`flex items-center gap-2 text-white hover:text-yellow-500 ${
            location.pathname === "/Settings" ? "text-yellow-500" : ""
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            className="lucide lucide-settings"
          >
            <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z" />
            <circle cx="12" cy="12" r="3" />
          </svg>
          Settings
        </Link>

        {/* Logout Button */}
        <button
          onClick={handleLogout}
          className="flex items-center gap-2 text-white hover:text-yellow-500 mt-4"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="lucide lucide-log-out"
          >
            <path d="M17 7l5 5-5 5" />
            <path d="M3 12h14" />
          </svg>
          Logout
        </button>
      </div>
    </div>
  );
}

export default Sidebar;
