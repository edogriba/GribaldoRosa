import React, { useContext } from 'react';
import { UserContext } from "../../../context/UserContext";
import { Link } from 'react-router-dom';

const UniversityProfileCard = () => {
    const { user } = useContext(UserContext);
    return (
        <div className="w-full max-w-sm my-auto ml-6 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <div className="flex flex-col justify-center items-center p-10">
                <img className="w-24 h-24 mb-3 rounded-full shadow-lg" src={user.logoPath ? `/uploads/${user.id}/${user.logoPath}` : `/user.jpg`} alt="Profile"/>
                <h5 className="mb-1 text-xl font-medium text-gray-900 dark:text-white">{user.name}</h5>
                <span className="text-sm text-gray-500 dark:text-gray-400">{user.type}</span>
                <div className="flex mt-4 md:mt-6">
                    <Link to="/universities/update">
                    <button className="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Modify</button>
                    </Link>
                </div>
            </div>
        </div>
    );
};  

export default UniversityProfileCard;