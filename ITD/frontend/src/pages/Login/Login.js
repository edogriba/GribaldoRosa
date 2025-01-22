import React, { useState } from "react";
import { Link } from 'react-router-dom';
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import { api } from '../../api/api'; 

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const dataUser = {
      email,
      password,
    };

    try {
      const res = await api.userLogin(dataUser);
      console.log("APPENA INVIATO"); // debug
      const data = await res.json();

      // Save the token to localStorage
      localStorage.setItem('token', data.token);

      // Redirect to user dashboard or another protected route
      return <Link to="/"></Link>;
    } catch (error) {
      console.error('Error registering student:', error.response?.data?.message || error.message);
      alert('Registration failed: ' + (error.response?.data?.message || 'Please try again.'));
    }
  }

  return(
    <div>
      <Navbar currentPage="login"/>
        <section className="bg-gray-50 dark:bg-gray-900">
          <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <Link to="/" className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
              <img
                className="w-20 h-20 mt-2"
                src="/logo.png"
                alt="logo"
              />
            </Link>
            <div className="w- bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
              <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                  Login
                </h1>
                {/* Form */}
                <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
                  {/* Email */}
                  <div>
                    <label
                      htmlFor="email"
                      className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >
                      Your email
                    </label>
                    <input
                      type="email"
                      name="email"
                      id="email"
                      value={email} // Bind email state
                      onChange={(e) => setEmail(e.target.value)} // Update email state
                      className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      placeholder="name@company.com"
                      required
                    />
                  </div>
                  {/* Password */}
                  <div>
                    <label
                      htmlFor="password"
                      className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >
                      Password
                    </label>
                    <input
                      type="password"
                      name="password"
                      id="password"
                      value={password} // Bind password state
                      onChange={(e) => setPassword(e.target.value)} // Update password state
                      placeholder="••••••••"
                      className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      required
                    />
                  </div>
                  {/* Submit */}
                  <button
                    type="submit"
                    className="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                  >
                    Create an account
                  </button>
                  <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                    Don't have an account?{' '}
                    <Link to="/register">
                      Register here
                    </Link>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </section>
      <Footer/>
    </div>
  );
};

export default Login;
