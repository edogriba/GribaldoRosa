import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../../api/api';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';

const RegisterStudent = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [profilePicturePath, setProfilePicturePath] = useState('');
  const [location, setLocation] = useState('');
  const [degreeProgram, setDegreeProgram] = useState('');
  const [gpa, setGpa] = useState('');
  const [graduationYear, setGraduationYear] = useState('');
  const [cvPath, setCvPath] = useState('');
  const [skills, setSkills] = useState('');
  const [languageSpoken, setLanguageSpoken] = useState('');

  const [universities, setUniversities] = useState([]); // Array to hold universities
  const [university, setUniversity] = useState(''); // Selected university ID

  useEffect(() => {
    const fetchUniversities = async () => {
      try {
        const res = await api.getUniversityList();
        const data = await res.json();

        setUniversities(data);
      } catch (error) {
        console.error('Error fetching universities:', error.message);
        alert('Failed to load universities. Please try again later.');
      }
    };

    fetchUniversities();
  }, []);
  

  const handleSubmit = async (e) => {
    e.preventDefault();

    const dataStudent = {
      email,
      password,
      firstName,
      lastName,
      phoneNumber,
      profilePicturePath,
      location,
      degreeProgram,
      GPA: parseFloat(gpa), // Ensure GPA is a number
      graduationYear: parseInt(graduationYear, 10), // Ensure graduationYear is an integer
      CVpath: cvPath,
      skills,
      languageSpoken,
      university // Ensure university ID is an integer
    };
    
    console.log("DataStudent: ", dataStudent);
    try {
      const res = await api.studentRegistration(dataStudent);
      console.log("APPENA INVIATO");
      const data = await res.json();

      // Save the token to localStorage
      localStorage.setItem('token', data.token);
      console.log("data: ", dataStudent);
      console.log("return studentRegistration(dataStudent): ", res);         // debug
      // Redirect to student dashboard or another protected route
      return <Link to="/dashboard/student"></Link>;
    } catch (error) {
      console.error('Error registering student:', error.response?.data?.message || error.message);
      alert('Registration failed: ' + (error.response?.data?.message || 'Please try again.'));
    }
  };
  
  return (
<div>
    
    <Navbar/>
    {/* Form */}
    <section className="bg-gray-50 dark:bg-gray-900">
      <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <Link to="/" className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          <img className="w-20 h-20 mt-2" src="/logo.png" alt="logo" />
        </Link>
        <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
          <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
            <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              Create a Student account
            </h1>
            <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
              {/* Email */}
              <div>
                <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Email
                </label>
                <input
                  type="email"
                  name="email"
                  id="email"
                  placeholder="name@example.com"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              {/* Password */}
              <div>
                <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Password
                </label>
                <input
                  type="password"
                  name="password"
                  id="password"
                  placeholder="••••••••"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              {/* First Name */}
              <div>
                <label htmlFor="firstName" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  First Name
                </label>
                <input
                  type="text"
                  name="firstName"
                  id="firstName"
                  placeholder="John"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                />
              </div>
              {/* Last Name */}
              <div>
                <label htmlFor="lastName" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Last Name
                </label>
                <input
                  type="text"
                  name="lastName"
                  id="lastName"
                  placeholder="Doe"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setLastName(e.target.value)}
                  required
                />
              </div>
              {/* Phone Number */}
              <div>
                <label htmlFor="phoneNumber" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Phone Number
                </label>
                <input
                  type="text"
                  name="phoneNumber"
                  id="phoneNumber"
                  placeholder="1234567890"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setPhoneNumber(e.target.value)}
                  required
                />
              </div>
              {/* Profile Picture */}
              <div>
                <label htmlFor="profilePicturePath" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Profile Picture (Optional)
                </label>
                <input
                  type="file"
                  name="profilePicturePath"
                  id="profilePicturePath"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setProfilePicturePath(e.target.value)}
                />
              </div>
              {/* Location */}
              <div>
                <label htmlFor="location" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Location
                </label>
                <input
                  type="text"
                  name="location"
                  id="location"
                  placeholder="City, Country"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setLocation(e.target.value)}
                  required
                />
              </div>
              {/* Degree Program */}
              <div>
                <label htmlFor="degreeProgram" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Degree Program
                </label>
                <input
                  type="text"
                  name="degreeProgram"
                  id="degreeProgram"
                  placeholder="e.g., Computer Science"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setDegreeProgram(e.target.value)}
                  required
                />
              </div>
              {/* GPA */}
              <div>
                <label htmlFor="GPA" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  GPA (Optional)
                </label>
                <input
                  type="number"
                  name="GPA"
                  id="GPA"
                  step="0.01"
                  placeholder="e.g., 3.5"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setGpa(e.target.value)}
                />
              </div>
              {/* Graduation Year */}
              <div>
                <label htmlFor="graduationYear" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Graduation Year
                </label>
                <input
                  type="number"
                  name="graduationYear"
                  id="graduationYear"
                  placeholder="e.g., 2025"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setGraduationYear(e.target.value)}
                  required
                />
              </div>
              {/* CV */}
              <div>
                <label htmlFor="CVpath" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  CV
                </label>
                <input
                  type="file"
                  name="CVpath"
                  id="CVpath"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setCvPath(e.target.value)}
                  required
                />
              </div>
              {/* Skills */}
              <div>
                <label htmlFor="skills" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Skills
                </label>
                <input
                  type="text"
                  name="skills"
                  id="skills"
                  placeholder="e.g., Python, SQL, React"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setSkills(e.target.value)}
                  required
                />
              </div>
              {/* Languages Spoken */}
              <div>
                <label htmlFor="languageSpoken" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Languages Spoken
                </label>
                <input
                  type="text"
                  name="languageSpoken"
                  id="languageSpoken"
                  placeholder="e.g., English, Spanish"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  onChange={(e) => setLanguageSpoken(e.target.value)}
                  required
                />
              </div>
              {/* University */}
              <div>
                <label htmlFor="university" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  University
                </label>
                <select
                  name="university"
                  id="university"
                  value={university}
                  onChange={(e) => setUniversity(e.target.value)}
                  required
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option value="" disabled>
                    Select your university
                  </option>
                  {universities.map((uni) => (
                    <option key={uni.id} value={uni.id}>
                      {uni.name}
                    </option>
                  ))}
                </select>
              </div>
              <button
                type="submit"
                className="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
              >
                Create an account
              </button>
              <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                Already have an account?{' '}
                <Link to="/login" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                  Login here
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

export default RegisterStudent;