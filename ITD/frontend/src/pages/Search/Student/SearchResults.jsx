import React, {useContext, useEffect, useState} from 'react';
import { UserContext } from '../../../context/UserContext';
import { Link, useNavigate } from 'react-router-dom';
import { api } from '../../../api/api';

const StudentResults = ({positions}) => {  
    const { user, userLogout } = useContext(UserContext);
    const [myApplications, setMyApplications] = useState([]);
    const navigate = useNavigate();


    if(user.type !== 'student') {
        api.userLogout();
        navigate('/login');
    }
         

    const fetchApplications = async () => {
        try {
            console.log("WEEE", user.id);
            const res = await api.getApplicationListStudent({'studentId': user.id});
            const data = await res.json();
            console.log("data", data);
            console.log("app", data.applications);
            setMyApplications(data.applications); 
            console.log("WEE", myApplications); 
            }
        catch(error) {
            console.log(error);
        }
    }
    useEffect(() => {
        console.log("Updated applications:", myApplications);
      }, [myApplications]);
   
    useEffect(() => {
        if(user.type !== 'student') {
            navigate('/login');
        }
    
        fetchApplications();
    }, [user]);
    

    if (!positions || positions.length === 0) {
        return (
            <div className="mt-10 flex justify-center items-center h-full">
            <h1>No positions found</h1>
            </div>
        );
      }

    return (
        <div>
        <section className="container mt-10 mx-auto p-6">
            <table  className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" className="px-6 py-3">
                                    Program Name
                                </th>
                                <th scope="col" className="px-6 py-3">
                                    Location
                                </th>
                                <th scope="col" className="px-6 py-3">
                                    Position
                                </th>
                                <th scope="col" className="px-6 py-3">
                                    Status
                                </th>
                                <th scope="col" className="px-6 py-3">
                                    Details
                                </th>
                            </tr>
                        </thead>
                        <tbody>
            
                {positions ? positions.map((position, index) => (
                <tr key={index} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600">
                <td className="px-6 py-4">
                    {position.programName}
                </td>
                <td className="px-6 py-4">
                    {position.location}
                </td>
                <td className="px-6 py-4">
                    {position.roleTitle}
                </td>
                <td className="px-6 py-4">
                    <div className="flex items-center">
                        <span className={`inline-flex items-center rounded bg-${position.status === "Open" ? "green" : "red" }-100 text-${position.status === "Open" ? "green" : "red" }-800 px-2.5 py-0.5 text-xs font-medium dark:bg-primary-900 dark:text-primary-300`}>
                            {position.status}
                        </span>
                    </div>
                </td>
                <td className="px-6 py-4">
                    {myApplications.some(application => application.internship.internshipPositionId === position.internshipPositionId) ? (
                    <Link to={`/students/dashboard/applications/${myApplications.find(application => application.internship.internshipPositionId === position.internshipPositionId).application.applicationId}`} className="font-medium text-primary-600 dark:text-primary-500 hover:underline">
                        <p className="font-medium text-primary-600 dark:text-primary-500 hover:underline">Already applied</p>
                    </Link>) : (
                    <Link to={`${position.internshipPositionId}`} className="font-medium text-primary-600 dark:text-primary-500 hover:underline">
                        <p className="font-medium text-primary-600 dark:text-primary-500 hover:underline">View</p>
                    </Link>
                    )}
                </td>
            </tr>
            
        )) : <h1>No positions found</h1>}
        </tbody>
        </table>
        </section>
        
        </div>
    );
};

export default StudentResults;