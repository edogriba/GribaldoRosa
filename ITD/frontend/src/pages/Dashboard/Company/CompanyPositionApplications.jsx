import React from 'react';
import { Link } from 'react-router-dom';
import Status from '../../../components/Status';

const CompanyPositionApplications = (applications) => {
    return (
        <div>
            <div className="mt-6 flow-root sm:mt-8">
                            <div className="divide-y divide-gray-200 dark:divide-gray-700">
                            { Array.isArray(applications.applications) ? (applications.applications.map((application) => (
                                <div
                                    key={application.application.applicationId}
                                    className="relative bg-gray-50 p-5 rounded shadow grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5"
                                >
                                    {/* application Name */}
                                    <div className="col-span-2 flex items-center sm:col-span-4 lg:col-span-1">
                                        <span className="text-base font-semibold text-gray-900 hover:underline dark:text-white">
                                            {application.student.firstName || "First Name"} {application.student.lastName || "Last Name"}
                                        </span>
                                    </div>                        

                                    {/* application Role */}
                                    <div className="flex col-span-2 items-center justify-center">
                                        <p className="text-sm text-gray-500 dark:text-gray-400">
                                            <span className="font-medium text-gray-900 dark:text-white">
                                                Degree
                                            </span>
                                            : {application.student.degreeProgram || "Unknown degree program"}
                                        </p>
                                    </div>

                                    {/* Application Status */}
                                                                        
                                    <div className="flex justify-center items-center">
                                        <Status status={application.application.status}/>
                                    </div>

                                    {/* View Details Button */}
                                    <div className="col-span-2 flex justify-center items-center sm:col-span-1">
                                        <Link to={`/companies/dashboard/positions/${application.application.internshipPositionId}/applications/${application.application.applicationId}`}>
                                            <button
                                                type="button"
                                                className="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto"
                                            >
                                                View details
                                            </button>
                                        </Link>
                                    </div>
                                </div>

                                )) ) : (
                                    <p>No  available</p>
                                )}
                            </div>
                        </div>
        </div>
    );
};

export default CompanyPositionApplications;