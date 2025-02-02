import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom'; 
import { UserContext } from '../../../context/UserContext';
import { api } from '../../../api/api';
import { toast } from 'react-hot-toast';
import GoBack from '../../../components/GoBack';

const CreateInternshipPosition = () => {
    
    const {user} = useContext(UserContext);
    const [programName, setProgramName] = useState('');
    const [roleTitle, setRoleTitle] = useState('');
    const [location, setLocation] = useState('');
    const [duration, setDuration] = useState(0);
    const [compensation, setCompensation] = useState(0);
    const [description, setDescription] = useState('');
    const [skillsRequired, setSkillsRequired] = useState('');
    const [languagesRequired, setLanguagesRequired] = useState('');
    const [companyId] = useState(user.id); // Set the companyId to the user's companyId
    const [benefits, setBenefits] = useState(''); 
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

        const newPosition = {
        programName,
        roleTitle,
        location,
        duration,
        compensation,
        description,
        skillsRequired,
        languagesRequired,
        companyId,
        benefits,
        };

    try {
        
        const response = await api.createPosition(newPosition);
        const data = await response.json();
        if (data.type !== 'created') {
            throw new Error(data.message);
        }
        toast.success('Position created successfully');
        navigate('/companies/dashboard/positions'); // Navigate to the positions list after creation
        
    } catch (error) {
        console.error('Error creating position:', error);
    
        if (error.status === 404) {
            toast.error("Session expired please login again");
            navigate("/login");
        }
    }
  };

  return (
    <section className="bg-white dark:bg-gray-900">
        <GoBack location="/companies/home"/>
                <div className="max-w-2xl px-4 py-1 mx-auto lg:py-3">
                    <h2 className="mb-4 text-xl font-bold text-gray-900 dark:text-white">Create Internship Position</h2>
                    <form onSubmit={handleSubmit}>
                        <div className="grid gap-4 mb-4 sm:grid-cols-2 sm:gap-6 sm:mb-5">
                            {/* Role Title */}
                            <div className="w-full">
                                <label htmlFor="roleTitle" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Role Title
                                </label>
                                <input
                                    type="text"
                                    name="roleTitle"
                                    id="roleTitle"
                                    placeholder='e.g. Software Developer Intern'
                                    onChange={(e) => setRoleTitle(e.target.value)}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required
                                />
                            </div>

                            {/* Program Name */}
                            <div className="w-full">
                                <label htmlFor="programName" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Program Name
                                </label>
                                <input
                                    type="text"
                                    name="programName"
                                    id="programName"
                                    placeholder='e.g. Software Engineering Internship'
                                    onChange={(e) => setProgramName(e.target.value)}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required
                                />
                            </div>

                            {/* Location */}
                            <div className="sm:col-span-2">
                                <label htmlFor="location" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Location
                                </label>
                                <input
                                    type="text"
                                    name="location"
                                    id="location"
                                    placeholder='e.g. New York, USA'
                                    onChange={(e) => setLocation(e.target.value)}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required
                                />
                            </div>

                            {/* Compensation */}
                            <div className="w-full">
                                <label htmlFor="compensation" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Compensation ($)
                                </label>
                                <input
                                    type="number"
                                    name="compensation"
                                    id="compensation"
                                    placeholder='e.g. 1000'
                                    onChange={(e) => setCompensation(parseInt(e.target.value, 10))}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required
                                />
                            </div>

                            {/* Duration */}
                            <div className="w-full">
                                <label htmlFor="duration" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Duration (Months)
                                </label>
                                <input
                                    type="number"
                                    name="duration"
                                    id="duration"
                                    placeholder='e.g. 6'
                                    onChange={(e) => setDuration(parseInt(e.target.value, 10))}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required
                                />
                            </div>

                            {/* Benefits */}
                            <div className="sm:col-span-2">
                                <label htmlFor="benefits" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Benefits
                                </label>
                                <textarea
                                    id="benefits"
                                    rows="3"
                                    placeholder='e.g. Health Insurance, Paid Apartment'
                                    className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    onChange={(e) => setBenefits(e.target.value)}
                                    required
                                ></textarea>
                            </div>

                            
                            {/* Skills Required */}
                            <div className="sm:col-span-2">
                                <label htmlFor="skillsRequired" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Skills Required
                                </label>
                                <textarea
                                    id="skillsRequired"
                                    rows="3"                                    
                                    placeholder="e.g. Python, Java, SQL"
                                    className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    onChange={(e) => setSkillsRequired(e.target.value)} 
                                    required
                                ></textarea>
                            
                            </div>{/* Description */}
                            <div className="sm:col-span-2">
                                <label htmlFor="description" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Description
                                </label>
                                <textarea
                                    id="description"
                                    rows="3"
                                    placeholder="The role is suted for students who are passionate about..."
                                    className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    onChange={(e) => setDescription(e.target.value)} 
                                    required
                                ></textarea>
                            </div>

                            {/* Languages Required */}
                            <div className="sm:col-span-2">
                                <label htmlFor="languagesRequired" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Languages Required
                                </label>
                                <textarea
                                    id="languagesRequired"
                                    rows="3"
                                    placeholder="e.g. English, French, Spanish"
                                    className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    onChange={(e) => setLanguagesRequired(e.target.value)}  
                                    required
                                ></textarea>
                            </div>
                        </div>
                    
                        <div className="flex justify-end items-center space-x-4">
                        <button
                                type="submit"
                                className="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                            >
                                Create Position
                            </button>
                            <button
                                type="button"
                                className="text-red-600 inline-flex items-center hover:text-white border border-red-600 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900"
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
                                    ></path>
                                </svg>
                                Cancel Forms
                            </button>
                        </div>
                    </form>
                </div>
            </section>
  );
};

export default CreateInternshipPosition;