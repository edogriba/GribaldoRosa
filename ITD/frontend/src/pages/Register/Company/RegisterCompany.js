import React  from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { Link, useNavigate } from 'react-router-dom';
import { useState} from 'react';
import { api } from '../../../api/api';
import { toast } from 'react-hot-toast';

const RegisterCompany = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [companyName, setCompanyName] = useState('');
    const [description, setDescription] = useState('');
    const [location, setLocation] = useState('');
    const [logo, setLogo] = useState(null);
    const navigate = useNavigate();

    const handleLogoChange = (e) => {
      const file = e.target.files[0];
      if (file) {
        setLogo(file);
      }
    };

    const handleSubmit = async (e) => {
      e.preventDefault();

      try {      

        const formData = new FormData();
            
        formData.append('email', email);
        formData.append('password', password);
        formData.append('companyName', companyName);
        formData.append('description', description);
        formData.append('location', location);
        
        if (logo) {
            formData.append('logo', logo);
        }
        const res = await api.companyRegistration(formData);
        // Save the token to localStorage
        localStorage.setItem('access token', res.access_token);
        if (res.status === 201) {
          toast.success('Registration successful! Please login with your credentials');
          navigate('/login');
        }
        else {
          toast.error('Registration failed: ' + res.message);
        }
      } catch (error) {
        console.log('Error registering company:', error.response?.data?.message || error.message);
        toast.error('Registration failed: ' + (error.response?.data?.message || 'Please try again.'));
      }
    };
  return (
    <div>
      <Navbar/>
      {/* Form */}
      <section className="pb-10 dark:bg-gray-900">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0">
          <Link to="/" className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
            <img
              className="w-20 h-20 mt-2"
              src="/logo.png"
              alt="logo"
            />
          </Link>
          <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                Create a Company account
              </h1>
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
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    placeholder="name@company.com"
                    onChange={(e) => setEmail(e.target.value)}
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
                    placeholder="••••••••"
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>              
                {/* Company Name */}
                <div>
                  <label
                    htmlFor="companyName"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    Company Name
                  </label>
                  <input
                    type="text"
                    name="companyName"
                    id="companyName"
                    placeholder="Your company name"
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    onChange={(e) => setCompanyName(e.target.value)}
                    required
                  />
                </div>
                {/* Description */}
                <div>
                  <label
                    htmlFor="description"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    Description
                  </label>
                  <textarea
                    name="description"
                    id="description"
                    placeholder="Describe your company"
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    onChange={(e) => setDescription(e.target.value)}
                    required
                  />
                </div>
                {/* Location */}
                <div>
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
                    placeholder="Company location"
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    onChange={(e) => setLocation(e.target.value)}
                    required
                  />
                </div>
                {/* Logo (Optional) */}
                <div>
                  
                  <label
                    htmlFor="logo"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    Company Logo (Optional)
                  </label>
                  <input
                    type="file"
                    name="logo"
                    id="logo"
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    onChange={handleLogoChange}
                  />
                </div>
                <div className="flex items-start">
                  <div className="flex items-center h-5">
                    <input
                      id="terms"
                      aria-describedby="terms"
                      type="checkbox"
                      className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                      required
                    />
                  </div>
                  <div className="ml-3 text-sm">
                    <label
                      htmlFor="terms"
                      className="font-light text-gray-500 dark:text-gray-300"
                    >
                      I accept the{' '}
                      <p
                        className="font-medium text-primary-600 hover:underline dark:text-primary-500"
                        
                      >
                        Terms and Conditions
                      </p>
                    </label>
                  </div>
                </div>
                <button
                  type="submit"
                  className="w-full text-white bg-primary-600 hover:bg-primary-200 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                >
                  Create an account
                </button>
                <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                  Already have an account?{' '}
                  <Link to="/login" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                  <span className="text-sm text-primary-900 dark:text-gray-400">
                  here
                  </span>
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

export default RegisterCompany;
