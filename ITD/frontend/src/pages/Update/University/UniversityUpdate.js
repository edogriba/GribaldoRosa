import React, { useContext, useEffect, useState } from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import GoBack from '../../../components/GoBack';
import { useNavigate } from 'react-router-dom';
import { api } from '../../../api/api';
import toast from 'react-hot-toast';

const UniversityUpdate = () => {
  const { user, userLogout } = useContext(UserContext);
  const navigate = useNavigate();
  
  // Correctly using array destructuring for useState
  const [description, setDescription] = useState(user?.description || '');
  const [logo, setLogo] = useState(null);
  const [websiteURL, setWebsiteURL] = useState(user?.websiteURL || '');

  useEffect(() => {
    if (user.type !== 'university') {
      navigate('/login');
    }
  }, [user, navigate]);

  // Handle file input for logo
  const handleLogoChange = (e) => {
    const file = e.target.files[0];
    setLogo(file);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const formData = new FormData();
        formData.append('description', description);
        formData.append('websiteURL', websiteURL);
        formData.append('id', user.id);
        formData.append('location', user.address);
        formData.append('logoPath', user.logoPath? user.logoPath : null);
        if (logo) {
            formData.append('logo', logo);
        }

        const res = await api.updateUniversity(formData);
        console.log('Updated profile:', res);
        navigate('/universities/dashboard/profile');   
        window.location.reload();    
        } catch (error) {
        console.error('Error updating profile:', error);
        }
  };

  return (
    <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
      <Navbar user={user} onLogout={userLogout} />
      <section className="bg-white dark:bg-gray-900">
        <GoBack location="/universities/home"/>
        <div className="max-w-2xl px-4 py-1 mx-auto lg:py-3">
          <h2 className="mb-4 text-xl font-bold text-gray-900 dark:text-white">
            Update Profile
          </h2>
          <form onSubmit={handleSubmit}>
            <div className="grid gap-4 mb-4 sm:grid-cols-2 sm:gap-6 sm:mb-5">
              {/* Logo */}
              <div className="w-full">
                <label
                  htmlFor="logoPath"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Logo
                </label>
                <input
                  type="file"
                  id="logoPath"
                  name="logoPath"
                  onChange={handleLogoChange}
                  className="block w-full text-sm text-gray-900 border 
                             border-gray-300 rounded-lg cursor-pointer 
                             bg-gray-50 focus:outline-none dark:bg-gray-700 
                             dark:border-gray-600 dark:placeholder-gray-400"
                />
              </div>

              {/* Website URL */}
              <div className="w-full">
                <label
                  htmlFor="websiteURL"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Website URL
                </label>
                <input
                  type="text"
                  name="websiteURL"
                  id="websiteURL"
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 
                             block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  value={websiteURL}
                  onChange={(e) => setWebsiteURL(e.target.value)}
                  required
                />
              </div>

              {/* Description */}
              <div className="sm:col-span-2">
              <label
                  htmlFor="description"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Description
                </label>
                <textarea
                  type="text"
                  name="description"
                  id="description"
                  rows="4"
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 
                             block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  required>
                </textarea>
              </div>
            </div>
            <div className="flex justify-end items-center space-x-4">
              <button
                type="submit"
                className="text-white bg-primary-700 hover:bg-primary-800 
                           focus:ring-4 focus:outline-none focus:ring-primary-300 
                           font-medium rounded-lg text-sm px-5 py-2.5 
                           text-center dark:bg-primary-600 dark:hover:bg-primary-700 
                           dark:focus:ring-primary-800"
              >
                Update Profile
              </button>
              <button
                type="button"
                className="text-red-600 inline-flex items-center hover:text-white 
                           border border-red-600 hover:bg-red-600 focus:ring-4 
                           focus:outline-none focus:ring-red-300 font-medium rounded-lg 
                           text-sm px-5 py-2.5 text-center 
                           dark:border-red-500 dark:text-red-500 
                           dark:hover:text-white dark:hover:bg-red-600 
                           dark:focus:ring-red-900"
                onClick={() => window.location.reload()}
              >
                <svg
                  className="w-5 h-5 mr-1 -ml-1"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fillRule="evenodd"
                    d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                    clipRule="evenodd"
                  />
                </svg>
                Cancel Changes
              </button>
            </div>
          </form>
        </div>
      </section>
      <Footer />
    </div>
  );
};

export default UniversityUpdate;
