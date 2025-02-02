import React, { useContext } from 'react';
import { UserContext } from "../../../context/UserContext";
import { Link } from 'react-router-dom';

const StudentProfileCard = () => {
    const { user } = useContext(UserContext);
    return (
        <div className="w-full max-w-sm my-auto ml-6 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <div className="flex flex-col justify-center items-center p-10">
                <img className="w-24 h-24 mb-3 rounded-full shadow-lg" src={user.profilePicture ? `/uploads/${user.id}/${user.profilePicture}` : `/user.jpg`}  alt="Profile"/>
                <h5 className="mb-1 text-xl font-medium text-gray-900 dark:text-white">{user.email}</h5>
                <span className="text-sm text-gray-500 dark:text-gray-400">{user.type}</span>
                <div className="flex mt-4 md:mt-6">
                    <Link to="/students/update">
                    <button className="inline-flex items-center px-4 py-2 mx-2 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Modify</button>
                    </Link>
                    <a 
                            href={`/uploads/${user.id}/${user?.CV}`}
                            download
                            className="text-sm font-medium text-center text-white px-4 py-2 mx-2 bg-secondary-600 text-white rounded-lg hover:bg-secondary-700"
                        >
                            Download CV
                        </a>
                    
                </div>
            </div>
        </div>
    );
};  

export default StudentProfileCard;