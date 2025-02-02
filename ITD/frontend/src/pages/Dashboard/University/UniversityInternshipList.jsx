import React, {useContext, useState, useEffect} from "react"
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../../../context/UserContext";
import { api } from "../../../api/api";
const UniversityInternshipList = () => {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();
    const [internships, setInternships] = useState([]);
    const [internshipStatus, setInternshipStatus] = useState('All');
    useEffect( () => {   
            const fetchInternships = async () => {
                try {
                    const res = await api.getInternshipListUniversity({"universityId": user.id});
                    const data = await res.json();
                    setInternships(data.internshipsPreview);
                }
                catch(error) {
                    console.error(error);
                }
            }
            if(user.type !== 'university') {
                navigate('/login');
            }
            fetchInternships();
        }, [user, navigate]);
    return (
        <div>    
            <div>    
                <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
                    <div className="p-10 gap-4 lg:flex lg:items-center lg:justify-between">
                        <h2 className="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">My internships</h2>
                        <div className="mt-6 gap-4 space-y-4 sm:flex sm:items-center sm:space-y-0 lg:mt-0 lg:justify-end">
                            <div>
                                <label
                                    htmlFor="internshipStatus"
                                    className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                                >
                                    Select internshipStatus
                                </label>
                                <select
                                    id="internshipStatus"
                                    className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                    value={internshipStatus}
                                    onChange={(e) => setInternshipStatus(e.target.value)}
                                >
                                    <option key="All" value="All">All statuses</option>
                                    <option key="Ongoing" value="Ongoing">Ongoing</option>
                                    <option key="Finished" value="Finished">Finished</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div className="px-10 mb-10">
                    {internships ? (
                    <table  className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" className="px-6 py-3">
                                    Company
                                </th>
                                <th scope="col" className="px-6 py-3">
                                    Student
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
                        {internships.map((internship) => {
                            return (
                                <tr key={internship.internshipId} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600">
                                    <th scope="row" className="flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white">
                                        <div className="text-base font-semibold">{internship.company_name}</div>
                                    </th>
                                    <td className="px-6 py-4">
                                        {internship.student_name}
                                    </td>
                                    <td className="px-6 py-4">
                                        {internship.roleTitle}
                                    </td>
                                    <td className="px-6 py-4">
                                        <div className="flex items-center">
                                            <span className={`inline-flex items-center rounded bg-${internship.status === "Ongoing" ? "green" : "red" }-100 text-${internship.status === "Ongoing" ? "green" : "red" }-800 px-2.5 py-0.5 text-xs font-medium dark:bg-primary-900 dark:text-primary-300`}>
                                                {internship.status}
                                            </span>
                                        </div>
                                    </td>
                                    <td className="px-6 py-4">
                                        <Link to={`${internship.internshipId}`}>
                                        <p className="font-medium text-primary-600 dark:text-primary-500 hover:underline">View</p>
                                        </Link>
                                    </td>
                                </tr>
                            )
                        })}
                        </tbody>
                    </table>
                    ) : <div className="text-center">No internships found</div>}
                    </div>
                </div>
            </div>  
        </div>
    )
}

export default UniversityInternshipList;