import React, { useState, useContext, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../../../context/UserContext";
import { api } from "../../../api/api";

const CompanyInternshipList = () => {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();
    const [internships, setInternships] = useState([]);
    const [filteredInternships, setFilteredInternships] = useState([]);
    const [internshipStatus, setInternshipStatus] = useState('All');
    const [internshipRole, setInternshipRole] = useState('All');
    const [possibleRoles, setPossibleRoles] = useState([]);
    useEffect( () => {   
        const fetchInternships = async () => {
            try {
                console.log("WEEE", user.id);
                const res = await api.getInternshipListCompany({"companyId": user.id});
                const data = await res.json();
                console.log("data", data);
                console.log("app", data.internships);
                setInternships(data.internshipsPreview);
                let roles = [];
                if (data.internshipsPreview) {
                    roles = [...new Set(data.internshipsPreview.map((pos) => pos.roleTitle))];
                }
                setPossibleRoles(roles);
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
    useEffect(() => {
        const filterResults = () => {
            let filtered = internships;

            if (internshipStatus !== "All") {
                filtered = filtered.filter((internship) => internship.status === internshipStatus);
            }
              

            if (internshipRole !== "All") {
                filtered = filtered.filter((internship) => internship.roleTitle === internshipRole);
            }
            console.log("filtered", filtered);
            setFilteredInternships(filtered);
        };

        filterResults();
    }, [internshipStatus, internshipRole, internships]);
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
                                        onChange={(e) => setInternshipStatus(e.target.value)}
                                        defaultValue={internshipStatus}
                                    >
                                        <option value="All">All applications</option>
                                        <option value="Ongoing">Ongoing</option>
                                        <option value="Finished">Finished</option>
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
                                        id="position-type"
                                        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                        onChange={(e) => setInternshipRole(e.target.value)}
                                    >
                                        <option key="All" value="All">All roles</option>
                                        {Array.isArray(possibleRoles) && possibleRoles.map((type) => (
                                            <option key={type} value={type}>{type}</option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                        </div>

                        {/* Internship list */}
                        <div className="mt-6 flow-root sm:mt-8">
                            <div className="divide-y divide-gray-200 dark:divide-gray-700">
                            { filteredInternships ? (filteredInternships.map((internship) => (
                                    <div
                                        key={internship.internshipId}
                                        className="relative bg-gray-50 p-5 rounded shadow grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                                        {/* Internship ID */}
                                        <div className="flex justify-center">
                                            <img className="w-10 h-10 rounded-full" src={internship.student_photoPath ? `/uploads/${internship.student_id}/${internship.student_photoPath}` : `/user.jpg`} alt="Profile"/> {/* TO DO BUT I NEED ID*/}  
                                        </div>
                                        {/* Name Surname */}
                                        <div className="flex justify-start">
                                            <div className="flex items-center gap-2 sm:justify-start">
                                                {internship.student_name}
                                            </div>
                                        </div>
                                        {/* Internship Role  */}
                                        <div className="content-center">
                                            <div className="flex items-center justify-end gap-2 sm:justify-start">
                                                <p className="text-sm text-gray-500 dark:text-gray-400">
                                                    <span className="font-medium text-gray-900 dark:text-white">
                                                        Role
                                                    </span>
                                                    : {internship.roleTitle}
                                                </p>
                                            </div>
                                        </div>

                                        {/* Position Status */}
                                        <div className="flex justify-center absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                                            <span
                                                className={`inline-flex items-center mt-3 h-5 rounded px-2.5 py-0.5 text-xs font-medium ${
                                                    internship.status === "Ongoing"
                                                        ? "bg-primary-100 text-primary-800 dark:bg-primary-900 dark:text-primary-300"
                                                        : internship.status === "Completed"
                                                        ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
                                                        : "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300"
                                                }`}
                                            >
                                                {internship.status}
                                            </span>
                                        </div>

                                        {/* View Details Button */}
                                        <div className="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                                            <Link to={`/companies/dashboard/internships/${internship.internshipId}`}>
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
                                    <p>No internships found</p>
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
