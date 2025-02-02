import React, {useContext, useEffect, useState} from "react"
import { useNavigate, Link } from "react-router-dom";
import { UserContext } from "../../../context/UserContext";
import { api } from "../../../api/api";
import Status from "../../../components/Status";

const StudentApplicationList = () => {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();
    const [filteredApplications, setFilteredApplications] = useState([]); 
    const [applicationStatus, setApplicationStatus] = useState("All"); 
    const [applications, setApplications] = useState([]);

    useEffect(() => {
        const filterResults = () => {
            let filtered = applications;

            if (applicationStatus !== "All") {
                filtered = filtered.filter((application) => application.application.status === applicationStatus);
            }
            
            setFilteredApplications(filtered);
        };

        filterResults();
    }, [applicationStatus, applicationStatus, applications]);

    useEffect( () => {   
        const fetchApplications = async () => {
            try {
                console.log("WEEE", user.id);
                const res = await api.getApplicationListStudent({'studentId': user.id});
                const data = await res.json();
                console.log("data", data);
                console.log("app", data.applications);
                setApplications(data.applications);
                setFilteredApplications(data.applications);
                console.log(res);
            }
            catch(error) {
                console.log(error);
            }
        }
        if(user.type !== 'student') {
            api.userLogout();
            navigate('/login');
        }
        fetchApplications();
    }, [user]);
    return (
        <div>    
            <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
                <div className="p-10 gap-4 lg:flex lg:items-center lg:justify-between">
                    <h2 className="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">My applications</h2>
                    <div className="mt-6 gap-4 space-y-4 sm:flex sm:items-center sm:space-y-0 lg:mt-0 lg:justify-end">
                        <div>
                            <label
                                htmlFor="applicationStatus"
                                className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                            >
                                Select applicationStatus
                            </label>
                            <select
                                id="applicationStatus"
                                className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                value={applicationStatus}
                                onChange={(e) => setApplicationStatus(e.target.value)}
                            >
                                <option key="All" value="All">All statuses</option>
                                <option key="Accepted" value="Accepted">Accepted</option>
                                <option key="Assessed" value="Assessed">Assessed</option>
                                <option key="Confirmed" value="Confirmed">Confirmed</option>
                                <option key="Pending" value="Pending">Pending</option>
                                <option key="Refused" value="Refused">Refused</option>
                                <option key="Rejected" value="Rejected">Rejected</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div className="px-10 mb-10">
                {filteredApplications ? (
                <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">
                                Company
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Program Name
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
                    {filteredApplications.map((application) => {
                        return (
                            <tr key={application.application.applicationId} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600">
                                <th scope="row" className="flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white">
                                    <img className="w-10 h-10 rounded-full" src={application.company.logoPath ? `/uploads/${application.company.id}/${application.company.logoPath}` : `/user.jpg`} alt="Profile"/>
                                    <div className="ps-3">
                                        <div className="text-base font-semibold">{application.company.companyName}</div>
                                        <div className="font-normal text-gray-500">{application.company.email}</div>
                                    </div>  
                                </th>
                                <td className="px-6 py-4">
                                    {application.internship.programName}
                                </td>
                                <td className="px-6 py-4">
                                    {application.internship.roleTitle}
                                </td>
                                <td className="px-6 py-4">
                                    <div className="flex items-center">
                                        <Status status={application.application.status} />
                                    </div>
                                </td>
                                <td className="px-6 py-4">
                                    <Link to={`/students/dashboard/applications/${application.application.applicationId}`}>
                                        <button
                                            type="button"
                                            className="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto"
                                        >
                                            View details
                                        </button>
                                    </Link>                               
                                </td>
                            </tr>
                        );
                    })}
                    </tbody>
                </table>) : <div className="text-center">No applications found</div>}
                
                </div>
            </div>
        </div>
    )
}

export default StudentApplicationList;