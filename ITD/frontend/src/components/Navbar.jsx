import React from "react";
import { Link, NavLink, useLocation } from "react-router-dom";
export const Navbar = ({ isLoggedIn, onLogout }) => {
  const location = useLocation(); // Access the current location

  return (
    <nav className="border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        {/* Logo */}
        <Link to="/" className="flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
          <img src="/logo.png" className="h-12" alt="Logo" />
        </Link>

        {/* Navigation Links */}
        <div className="w-full md:block md:w-auto" id="navbar-solid-bg">
          <ul className="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700">
            {!isLoggedIn ? (
              <>
                <li>
                  <NavLink
                    to="/"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Welcome
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/about"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    About
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/login"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Login
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/register"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Register
                  </NavLink>
                </li>
              </>
            ) : (
              <>
                <li>
                  <NavLink
                    to="/students/home"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Home
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/students/update"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Update
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/students/search"
                    className={({ isActive }) =>
                      isActive ? "text-primary-500" : "text-gray-900 dark:text-white"
                    }
                  >
                    Search
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/students/dashboard/profile"
                    className={() =>
                      location.pathname.startsWith("/students/dashboard/")
                        ? "text-primary-500"
                        : "text-gray-900 dark:text-white"
                    }
                  >
                    Profile
                  </NavLink>
                </li>
                <li>
                  <button
                    onClick={onLogout}
                    className="text-red-500 hover:underline"
                  >
                    Logout
                  </button>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
