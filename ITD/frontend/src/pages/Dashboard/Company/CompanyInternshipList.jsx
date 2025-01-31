import React, { useState, useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../../../context/UserContext";
import { api } from "../../../api/api";

const CompanyInternshipList = () => {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();
    const [internships, setInternships] = useState([]);
    const [internshipStatus, setInternshipStatus] = useState('All');

    useEffect( () => {   
        const fetchInternships = async () => {
            try {
                console.log("WEEE", user.id);
                const res = await api.getInternshipListCompany({"companyId": user.id});
                const data = await res.json();
                console.log("data", data);
                console.log("app", data.internships);
                setInternships(data.internships);
                console.log(res);
            }
            catch(error) {
                console.log(error);
            }
        }
        if(user.type !== 'company') {
            navigate('/login');
        }
        fetchInternships();
    }, []);
    return (
        <div>
            <section className="bg-white py-8 antialiased dark:bg-gray-900 md:py-16">
                <div className="mx-auto max-w-screen-xl px-4 2xl:px-0">
                    <div className="mx-auto max-w-5xl">
                        <div className="gap-4 lg:flex lg:items-center lg:justify-between">
                            <h2 className="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">My internships</h2>

                            <div className="mt-6 gap-4 space-y-4 sm:flex sm:items-center sm:space-y-0 lg:mt-0 lg:justify-end">
                                <div>
                                    <label
                                        htmlFor="order-type"
                                        className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Select order type
                                    </label>
                                    <select
                                        id="order-type"
                                        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                    >
                                        <option selected>All applications</option>
                                        <option value="ongoing">Ongoing</option>
                                        <option value="completed">Finished</option>
                                    </select>
                                </div>

                                <span className="inline-block text-gray-500 dark:text-gray-400">from</span>

                                <div>
                                    <label
                                        htmlFor="date"
                                        className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Select date
                                    </label>
                                    <select
                                        id="date"
                                        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                    >
                                        <option selected>this week</option>
                                        <option value="this month">this month</option>
                                        <option value="last 3 months">the last 3 months</option>
                                        <option value="last 6 months">the last 6 months</option>
                                        <option value="this year">this year</option>
                                    </select>
                                </div>

                                <button
                                    type="button"
                                    className="w-full rounded-lg bg-primary-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-primary-800 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 sm:w-auto"
                                >
                                    Add return request
                                </button>
                            </div>
                        </div>

                        {/* Position list */}
                        <div className="mt-6 flow-root sm:mt-8">
                            <div className="divide-y divide-gray-200 dark:divide-gray-700">
                            { Array.isArray(internships) ? (internships.map((position) => (
                                    <div
                                        key={position.id}
                                        className="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                                        {/* Position ID */}
                                        <div className="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                                            <span className="text-base font-semibold text-gray-900 hover:underline dark:text-white">
                                                #{position.id}
                                            </span>
                                        </div>

                                        {/* Position Duration */}
                                        <div className="content-center">
                                            <div className="flex items-center gap-2">
                                                <svg
                                                    className="h-4 w-4 text-gray-400"
                                                    aria-hidden="true"
                                                    xmlns="http://www.w3.org/2000/svg"
                                                    width="24"
                                                    height="24"
                                                    fill="none"
                                                    viewBox="0 0 24 24"
                                                >
                                                    <path
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z"
                                                    />
                                                </svg>
                                                <p className="text-sm font-medium text-gray-500 dark:text-gray-400">
                                                    {position.duration}
                                                </p>
                                            </div>
                                        </div>

                                        {/* Position Role  */}
                                        <div className="content-center">
                                            <div className="flex items-center justify-end gap-2 sm:justify-start">
                                                <p className="text-sm text-gray-500 dark:text-gray-400">
                                                    <span className="font-medium text-gray-900 dark:text-white">
                                                        Role
                                                    </span>
                                                    : {position.role}
                                                </p>
                                            </div>
                                        </div>

                                        {/* Position Status */}
                                        <div className="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                                            <span
                                                className={`inline-flex items-center rounded px-2.5 py-0.5 text-xs font-medium ${
                                                    position.status === "Ongoing"
                                                        ? "bg-primary-100 text-primary-800 dark:bg-primary-900 dark:text-primary-300"
                                                        : position.status === "Completed"
                                                        ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
                                                        : "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300"
                                                }`}
                                            >
                                                {position.status}
                                            </span>
                                        </div>

                                        {/* View Details Button */}
                                        <div className="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                                            <button
                                                type="button"
                                                className="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto"
                                            >
                                                View details
                                            </button>
                                        </div>
                                    </div>
                                )) ) : (
                                    <p>No internships available</p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default CompanyInternshipList;
