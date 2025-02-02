import React, { useContext, useState, useEffect } from "react";
import { UserContext } from "../../../context/UserContext";
import { api } from "../../../api/api";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-hot-toast";

const CompanyPositionList = () => {
    const { user } = useContext(UserContext);
    const [positions, setPositions] = useState([]); 
    const [filteredPositions, setFilteredPositions] = useState([]); 
    const [positionType, setPositionType] = useState("All"); 
    const [positionAvailability, setPositionAvailability] = useState("All"); 
    const [possiblePositions, setPossiblePositions] = useState([]);
    const { navigate } = useNavigate(); 
    useEffect(() => {
        const fetchPositions = async () => {
        try {
            const res = await api.getPositionListCompany({"companyId": user.id});
            const data = await res.json();

            setPositions(data.internship_positions);
            setFilteredPositions(data.internship_positions);
            let roles = [];
            if (data.internship_positions) {
                roles = [...new Set(data.internship_positions.map((pos) => pos.roleTitle))];

            }
            setPossiblePositions(roles);
        } catch (error) {
            console.error('Error fetching positions:', error.message);
            console.log(error);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert('Failed to load positions. Please try again later.');
        }
        };

        fetchPositions();
    }, [user]);

    useEffect(() => {
        const filterResults = () => {
            let filtered = positions;

            if (positionAvailability !== "All") {
                filtered = filtered.filter((position) => position.status === positionAvailability);
            }

            if (positionType !== "All") {
                filtered = filtered.filter((position) => position.roleTitle === positionType);
            }
            
            setFilteredPositions(filtered);
        };

        filterResults();
    }, [positionType, positionAvailability, positions]);

    
    return (
        <div>
            <section className="bg-white py-8 antialiased dark:bg-gray-900 md:py-16">
                <div className="mx-auto max-w-screen-xl px-4 2xl:px-0">
                    <div className="mx-auto max-w-5xl">
                        <div className="gap-4 lg:flex lg:items-center lg:justify-between">
                            <h2 className="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">My Positions</h2>

                                <div className="mt-6 gap-4 space-y-4 sm:flex sm:items-center sm:space-y-0 lg:mt-0 lg:justify-end">
                                <div >
                                    <label
                                        htmlFor="positionAvailability"
                                        className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Select positionAvailability
                                    </label>
                                    <select
                                        id="positionAvailability"
                                        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                        value={positionAvailability}
                                        onChange={(e) => setPositionAvailability(e.target.value)}
                                    >
                                        <option key="All" value="All">All</option>
                                        <option key="Open" value="Open">Open</option>
                                        <option key="Closed" value="Closed">Closed</option>
                                    </select>
                                </div>

                                <span className="inline-block text-gray-500 dark:text-gray-400">for</span>
                                
                                <div>
                                    <label
                                        htmlFor="position-type"
                                        className="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Select position type
                                    </label>
                                    <select
                                        id="position-type"
                                        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]"
                                        value={positionType}
                                        onChange={(e) => setPositionType(e.target.value)}
                                    >
                                        <option key="All" value="All">All roles</option>
                                        {Array.isArray(possiblePositions) && possiblePositions.map((type) => (
                                            <option key={type} value={type}>{type}</option>
                                        ))}
                                    </select>
                                </div>
                                <Link to="/companies/create-position">
                                <button
                                    type="button"
                                    className="w-full rounded-lg bg-primary-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-primary-800 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 sm:w-auto"
                                >
                                    Add open position
                                </button>
                                </Link>
                            </div>
                        </div>

                        {/* Position list */}
                        <div className="mt-6 flow-root sm:mt-8">
                            <div className="divide-y divide-gray-200 dark:divide-gray-700">
                            { Array.isArray(filteredPositions) ? (filteredPositions.map((position) => (
                                <div
                                    key={position.internshipPositionId}
                                    className="relative bg-gray-50 p-5 rounded shadow grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5"
                                >
                                    {/* Position Name */}
                                    <div className="col-span-2 flex items-center sm:col-span-4 lg:col-span-1">
                                        <span className="text-base font-semibold text-gray-900 hover:underline dark:text-white">
                                            {position.programName}
                                        </span>
                                    </div>

                                    {/* Position Duration */}
                                    <div className="flex justify-center items-center">
                                        <div className="flex justify-center items-center gap-2">
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
                                                {position.duration} months
                                            </p>
                                        </div>
                                    </div>

                                    {/* Position Role */}
                                    <div className="flex items-center">
                                        <p className="text-sm text-gray-500 dark:text-gray-400">
                                            <span className="font-medium text-gray-900 dark:text-white">
                                                Role
                                            </span>
                                            : {position.roleTitle}
                                        </p>
                                    </div>

                                    {/* Position Status */}
                                    <div className="flex justify-center items-center">
                                        <span
                                            className={`inline-flex items-center rounded px-2.5 py-0.5 text-xs font-medium ${
                                                position.status === "Open"
                                                    ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
                                                    : position.status === "Closed"
                                                    ? "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300"
                                                    : "bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-300"
                                            }`}
                                        >
                                            {position.status}
                                        </span>
                                    </div>

                                    {/* View Details Button */}
                                    <div className="col-span-2 flex justify-center items-center sm:col-span-1">
                                        <Link to={`/companies/dashboard/positions/${position.internshipPositionId}`}>
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
                                    <p>No positions found</p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default CompanyPositionList;
