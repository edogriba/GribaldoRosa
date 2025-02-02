import React, { useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import GoBack from '../../../components/GoBack';
import { UserContext } from '../../../context/UserContext';
import { api } from '../../../api/api';

const StudentUpdate = () => {
  const { user, userLogout } = useContext(UserContext);

  // Store user data in local state
  const [phoneNumber, setPhoneNumber] = useState(user?.phoneNumber || '');
  const [location, setLocation] = useState(user?.location || '');
  const [skills, setSkills] = useState(user?.skills || '');
  const [languages, setLanguages] = useState(user?.languageSpoken || '');
  const [gpa, setGpa] = useState(user?.GPA || null);
  const [degreeProgram, setDegreeProgram] = useState(user?.degreeProgram || '');
  const [graduationYear, setGraduationYear] = useState(user?.graduationYear || null);
 
  // File states (store File objects directly)
  const [CV, setCV] = useState(null);
  const [profilePicture, setProfilePicture] = useState(null);

  const navigate = useNavigate();

  // Handle file uploads by storing the raw file objects
  const handleCVUpload = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      setCV(file);
    }
  };

  const handleProfilePictureUpload = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      setProfilePicture(file);
    }
  };

  // Send form data as FormData
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const formData = new FormData();
      formData.append('phoneNumber', phoneNumber);
      formData.append('location', location);
      formData.append('skills', skills);
      formData.append('languageSpoken', languages);
      formData.append('GPA', parseFloat(gpa));
      formData.append('degreeProgram', degreeProgram);
      formData.append('graduationYear', parseInt(graduationYear));
      formData.append('studentId', user.id);
      formData.append('universityId', user.universityId);

      if (CV) {
        formData.append('CV', CV);
      }
      if (profilePicture) {
        formData.append('profilePicture', profilePicture);
      }
      await api.updateStudent(formData);
      navigate('/students/dashboard/profile');   
      window.location.reload();    
      
      


    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  useEffect(() => {
    if (!user || user.type !== 'student') {
      navigate('/login');
    }
  }, [user, navigate]);

  return (
    <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
      <Navbar user={user} onLogout={userLogout} />
      <section className="bg-white dark:bg-gray-900">
        <GoBack location="/students/home"/>
        <div className="max-w-2xl px-4 py-1 mx-auto lg:py-3">
          <h2 className="mb-4 text-xl font-bold text-gray-900 dark:text-white">
            Update Profile
          </h2>
          <form onSubmit={handleSubmit}>
            <div className="grid gap-4 mb-4 sm:grid-cols-2 sm:gap-6 sm:mb-5">
              {/* Phone Number */}
              <div className="w-full">
                <label
                  htmlFor="phoneNumber"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Phone Number
                </label>
                <input
                  type="text"
                  name="phoneNumber"
                  id="phoneNumber"
                  value={phoneNumber}
                  onChange={(e) => setPhoneNumber(e.target.value)}
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 
                             focus:border-primary-600 block w-full p-2.5 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Location */}
              <div className="w-full">
                <label
                  htmlFor="location"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Location
                </label>
                <input
                  type="text"
                  name="location"
                  id="location"
                  value={location}
                  onChange={(e) => setLocation(e.target.value)}
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 
                             focus:border-primary-600 block w-full p-2.5 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Skills */}
              <div className="sm:col-span-2">
                <label
                  htmlFor="skills"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Skills
                </label>
                <textarea
                  id="skills"
                  rows="4"
                  value={skills}
                  onChange={(e) => setSkills(e.target.value)}
                  className="block p-2.5 w-full text-sm text-gray-900 
                             bg-gray-50 rounded-lg border border-gray-300 
                             focus:ring-primary-500 focus:border-primary-500 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Profile Picture */}
              <div>
                <label
                  htmlFor="profilePicture"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Profile Picture (Optional)
                </label>
                <input
                  type="file"
                  name="profilePicture"
                  id="profilePicture"
                  onChange={handleProfilePictureUpload}
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 
                             focus:border-primary-600 block w-full p-2.5 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* CV */}
              <div>
                <label
                  htmlFor="CV"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  CV
                </label>
                <input
                  type="file"
                  name="CV"
                  id="CV"
                  onChange={handleCVUpload}
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 
                             focus:border-primary-600 block w-full p-2.5 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Languages */}
              <div className="sm:col-span-2">
                <label
                  htmlFor="languages"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Languages Spoken
                </label>
                <textarea
                  id="languages"
                  rows="4"
                  value={languages}
                  onChange={(e) => setLanguages(e.target.value)}
                  className="block p-2.5 w-full text-sm text-gray-900 
                             bg-gray-50 rounded-lg border border-gray-300 
                             focus:ring-primary-500 focus:border-primary-500 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* GPA */}
              <div className="sm:col-span-2">
                <label
                  htmlFor="gpa"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  GPA
                </label>
                <input
                  type="number"
                  step="0.01"
                  id="gpa"
                  value={gpa}
                  onChange={(e) => setGpa(e.target.value)}
                  className="block p-2.5 w-full text-sm text-gray-900 
                             bg-gray-50 rounded-lg border border-gray-300 
                             focus:ring-primary-500 focus:border-primary-500 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Graduation Year */}
              <div className="w-full">
                <label
                  htmlFor="graduationYear"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Graduation Year
                </label>
                <input
                  type="number"
                  name="graduationYear"
                  id="graduationYear"
                  value={graduationYear}
                  onChange={(e) => setGraduationYear(e.target.value)}
                  className="bg-gray-50 border border-gray-300 text-gray-900 
                             text-sm rounded-lg focus:ring-primary-600 
                             focus:border-primary-600 block w-full p-2.5 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>

              {/* Degree Program */}
              <div className="sm:col-span-2">
                <label
                  htmlFor="degreeProgram"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Degree Program
                </label>
                <input
                  id="degreeProgram"
                  value={degreeProgram}
                  onChange={(e) => setDegreeProgram(e.target.value)}
                  className="block p-2.5 w-full text-sm text-gray-900 
                             bg-gray-50 rounded-lg border border-gray-300 
                             focus:ring-primary-500 focus:border-primary-500 
                             dark:bg-gray-700 dark:border-gray-600 
                             dark:placeholder-gray-400 dark:text-white 
                             dark:focus:ring-primary-500 dark:focus:border-primary-500"
                />
              </div>
            </div>

            <div className="flex justify-end items-center space-x-4">
              <button
                type="submit"
                className="text-white bg-primary-700 hover:bg-primary-800 
                           focus:ring-4 focus:outline-none focus:ring-primary-300 
                           font-medium rounded-lg text-sm px-5 py-2.5 text-center 
                           dark:bg-primary-600 dark:hover:bg-primary-700 
                           dark:focus:ring-primary-800"
              >
                Update Profile
              </button>
              <button
                type="button"
                onClick={() => window.location.reload()}
                className="text-red-600 inline-flex items-center 
                           hover:text-white border border-red-600 
                           hover:bg-red-600 focus:ring-4 focus:outline-none 
                           focus:ring-red-300 font-medium rounded-lg 
                           text-sm px-5 py-2.5 text-center 
                           dark:border-red-500 dark:text-red-500 
                           dark:hover:text-white dark:hover:bg-red-600 
                           dark:focus:ring-red-900"
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
                  ></path>
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

export default StudentUpdate;
